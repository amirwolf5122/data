import os
import io
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import pytesseract
from deep_translator import GoogleTranslator
from textwrap import wrap
import time
import random
from zipfile import ZipFile
import re
# ---------- تنظیم مسیر tesseract در ویندوز ----------
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ---------- مرحله ۱: دریافت URL عکس‌های مانگا ----------
def fetch_image_urls(chapter_url):
    print("🔍 Fetching image URLs...")
    resp = requests.get(chapter_url, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    imgs = soup.find_all("img")

    urls = []
    for img in imgs:
        src = img.get("data-src") or img.get("src")
        if src and (src.endswith(".jpg") or src.endswith(".png") or src.endswith(".webp")):
            full_url = requests.compat.urljoin(chapter_url, src)
            urls.append(full_url)
    print(f"✅ Found {len(urls)} images")
    return urls

# ---------- مرحله ۲: دانلود عکس ----------
def download_image(url):
    print(f"Downloading: {url}")
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    return Image.open(io.BytesIO(resp.content))

# ---------- مرحله ۳: استخراج متن و مختصات با OCR (کادر/بلوک) ----------
def ocr_extract_text_boxes(img):
    data = pytesseract.image_to_data(img, lang="eng", output_type=pytesseract.Output.DICT)
    blocks = {}
    n_boxes = len(data['level'])

    for i in range(n_boxes):
        block_num = data['block_num'][i]  # استفاده از بلوک به جای خط
        if block_num not in blocks:
            blocks[block_num] = {
                "text": [],
                "left": data['left'][i],
                "top": data['top'][i],
                "right": data['left'][i] + data['width'][i],
                "bottom": data['top'][i] + data['height'][i],
            }

        if data['text'][i].strip():
            blocks[block_num]["text"].append(data['text'][i])
            blocks[block_num]["left"] = min(blocks[block_num]["left"], data['left'][i])
            blocks[block_num]["top"] = min(blocks[block_num]["top"], data['top'][i])
            blocks[block_num]["right"] = max(blocks[block_num]["right"], data['left'][i] + data['width'][i])
            blocks[block_num]["bottom"] = max(blocks[block_num]["bottom"], data['top'][i] + data['height'][i])

    boxes = []
    for block in blocks.values():
        if block["text"]:
            boxes.append({
                "text": " ".join(block["text"]),
                "left": block["left"],
                "top": block["top"],
                "width": block["right"] - block["left"],
                "height": block["bottom"] - block["top"],
            })

    return boxes

# ---------- ترجمه متن ----------
def translate_text(text, dest="fa"):
    if not isinstance(text, str) or not text.strip():
        return ""
    try:
        print(f"Translating: {text}")
        time.sleep(random.randint(2, 3))
        zzheaders = {
        'accept': '*/*',
        'accept-language': 'fa,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'ect': '3g',
        'origin': 'https://www.bing.com',
        'priority': 'u=1, i',
        'referer': 'https://www.bing.com/translator?from=&to=fa&setlang=fa',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"133.0.6943.127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }

        zzparams = {
        'from': '',
        'to': 'fa',
        'setlang': 'fa',
    }

        zzresponse = requests.post(
        'https://www.bing.com/translator',
        headers=zzheaders,
        data=zzparams,
    )

        zzzszda = eval(zzresponse.text.split('params_AbusePreventionHelper = ')[1].split(';')[0])
        zzdata = {
        'fromLang': 'en',
        'to': 'fa',
        'tone': 'Casual',
        'text': text,
        'token': zzzszda[1],
        'key': zzzszda[0],
    }

        zzresponse = requests.post(
        'https://www.bing.com/ttranslatev3?isVertical=1&&IG=123&IID=translator',
        headers=zzheaders,
        data=zzdata,
    )
        try:
          translated = zzresponse.json()[0]['translations'][0]['text']
        except Exception:
          translated = GoogleTranslator(source="auto", target=dest).translate(text)
        return translated
    except Exception as e:
        print("⚠️ Translation failed:", e)
        return text or ""

# ---------- تابع کمک برای نوشتن متن داخل کادر ----------
def draw_text_in_box(draw, text, box, font, fill="black", padding=5):
    x, y, w, h = box["left"], box["top"], box["width"], box["height"]

    # تابع کمکی برای گرفتن ارتفاع یک خط
    def get_line_height(fnt):
        bbox = fnt.getbbox("Ay")  # ارتفاع تقریبی خط
        return bbox[3] - bbox[1]

    line_height = get_line_height(font)

    # تقسیم متن به خطوط با wrap
    lines = []
    for paragraph in text.split("\n"):
        wrapped = wrap(paragraph, width=32)  # عدد 40 را می‌توان تنظیم کرد
        lines.extend(wrapped)

    # کاهش فونت اگر متن بیشتر از ارتفاع کادر شد
    while line_height * len(lines) > h - 2 * padding and getattr(font, "path", None):
        font_size = font.size - 1
        if font_size < 10:
            break
        font = ImageFont.truetype(font.path, font_size)
        line_height = get_line_height(font)
        lines = []
        for paragraph in text.split("\n"):
            wrapped = wrap(paragraph, width=32)
            lines.extend(wrapped)

    # پاک کردن متن اصلی
    draw.rectangle([x, y, x + w, y + h], fill="white")

    # نوشتن خطوط داخل کادر
    current_y = y + padding
    for line in lines:
        draw.text((x + padding, current_y), line, fill=fill, font=font)
        current_y += line_height

# ---------- نوشتن ترجمه روی تصویر ----------
def overlay_translated_text(img, boxes):
    img_edit = img.copy()
    draw = ImageDraw.Draw(img_edit)

    if os.path.exists("Vazirmatn-Black.ttf"):
        font = ImageFont.truetype("Vazirmatn-Black.ttf", 22)
    else:
        font = ImageFont.load_default()

    # ترجمه و نوشتن متن داخل کادر
    for box in boxes:
        eng_text = box["text"]
        tr_text = translate_text(eng_text)
        if not tr_text:
            continue
        draw_text_in_box(draw, tr_text, box, font)

    return img_edit

def get_clean_manga_title(chapter_url):
    """ استخراج اسم مانگا و شماره چپتر و پاکسازی برای نام فایل """
    resp = requests.get(chapter_url, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    title_tag = soup.find("title")
    if title_tag and title_tag.text:
        text = title_tag.text.strip()
        # حذف "- English" و سایر جداکننده‌ها
        text = re.sub(r"[-–]", "", text)  # - و – حذف شود
        text = text.replace("English", "").strip()
        # حذف همه کاراکترهای غیر حرف و عدد و نقطه
        text = re.sub(r"[^\w\.]", "", text)
        return text

    # fallback: استفاده از URL
    parts = chapter_url.strip("/").split("/")
    if parts:
        text = parts[-1].replace("-", "")
        text = re.sub(r"[^\w\.]", "", text)
        return text

    return "MangaChapter"

# ---------- اجرای فرایند و ذخیره ZIP با نام پویا ----------
def process_chapter(chapter_url):
    urls = fetch_image_urls(chapter_url)
    zip_name = f"{get_clean_manga_title(chapter_url)}.zip"
    saved_files = []

    for i, url in enumerate(urls, start=1):
        try:
            img = download_image(url)
            boxes = ocr_extract_text_boxes(img)
            img2 = overlay_translated_text(img, boxes)

            # ذخیره تصویر در همان مسیر اجرای اسکریپت
            out_path = f"page_{i:03d}.png"
            img2.save(out_path)
            saved_files.append(out_path)
            print(f"💾 Saved translated: {out_path}")
        except Exception as e:
            print(f"❌ Error on page {i}: {e}")

    # ساخت ZIP در همان مسیر
    with ZipFile(zip_name, "w") as zipf:
        for file in saved_files:
            try:
              zipf.write(file, arcname=os.path.basename(file))
              os.remove(file)  # حذف تصویر بعد از اضافه شدن به ZIP
            except Exception as e:
              print(f"❌ Error on page {e}")

    print(f"📦 All pages zipped: {zip_name}")
# ---------- اجرای برنامه ----------
if __name__ == "__main__":
    chapter_url = "https://www.mgeko.cc/reader/en/mr-zombie-chapter-123-eng-li/"
    process_chapter(chapter_url)

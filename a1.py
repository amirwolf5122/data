#pip install requests beautifulsoup4 pillow easyocr deep-translator ; sudo apt update ; sudo apt install tesseract-ocr -y
import os
import io
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
from deep_translator import GoogleTranslator
from textwrap import wrap
import time
import random
from zipfile import ZipFile
import re
import numpy as np
import easyocr  # جایگزین pytesseract

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

# ---------- مرحله ۳: استخراج متن و مختصات با EasyOCR ----------
reader = easyocr.Reader(['en'])  # می‌توانید 'fa' هم اضافه کنید

def ocr_extract_text_boxes(img):
    results = reader.readtext(np.array(img))
    boxes = []
    for (bbox, text, prob) in results:
        if not text.strip():
            continue
        (top_left, top_right, bottom_right, bottom_left) = bbox
        x = int(min([p[0] for p in bbox]))
        y = int(min([p[1] for p in bbox]))
        w = int(max([p[0] for p in bbox]) - x)
        h = int(max([p[1] for p in bbox]) - y)
        boxes.append({
            "text": text,
            "left": x,
            "top": y,
            "width": w,
            "height": h
        })
    # ادغام خطوط نزدیک به هم در یک حباب
    boxes = merge_boxes_by_vertical_proximity(boxes)
    print(f"✅ Found {len(boxes)} text boxes")
    return boxes

def merge_boxes_by_vertical_proximity(boxes, max_gap=25, min_horizontal_overlap=0.5):
    if not boxes:
        return []

    boxes = sorted(boxes, key=lambda b: b['top'])
    merged = [boxes[0]]

    for box in boxes[1:]:
        last = merged[-1]
        vertical_overlap = box['top'] <= last['top'] + last['height'] + max_gap
        horizontal_overlap = (min(last['left'] + last['width'], box['left'] + box['width']) -
                              max(last['left'], box['left'])) / min(last['width'], box['width'])
        if vertical_overlap and horizontal_overlap > min_horizontal_overlap:
            last['text'] += ' ' + box['text']
            last['left'] = min(last['left'], box['left'])
            last['top'] = min(last['top'], box['top'])
            last['width'] = max(last['left'] + last['width'], box['left'] + box['width']) - last['left']
            last['height'] = max(last['top'] + last['height'], box['top'] + box['height']) - last['top']
        else:
            merged.append(box)
    return merged


# ---------- ترجمه متن ----------
def translate_text(text, dest="fa"):
    if not isinstance(text, str) or not text.strip():
        return ""
    try:
        print(f"Translating:: {text}")
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
        try:
          zzresponse = requests.post(
        'https://www.bing.com/ttranslatev3?isVertical=1&&IG=123&IID=translator',
        headers=zzheaders,
        data=zzdata,
    )
          translated = zzresponse.json()[0]['translations'][0]['text']
        except Exception:
          time.sleep(random.randint(3, 4))
          try:
            zzresponse = requests.post(
        'https://www.bing.com/ttranslatev3?isVertical=1&&IG=123&IID=translator',
        headers=zzheaders,
        data=zzdata,
    )
            translated = zzresponse.json()[0]['translations'][0]['text']
          except Exception:
            translated = GoogleTranslator(source="auto", target=dest).translate(text)
        return translated
    except Exception as e:
        print("⚠️ Translation failed:", e)
        return text or ""

# ---------- نوشتن متن داخل کادر ----------
def draw_text_in_box(draw, text, box, font, fill="black", padding=5):
    x, y, w, h = box["left"], box["top"], box["width"], box["height"]

    def get_line_height(fnt):
        bbox = fnt.getbbox("Ay")
        return bbox[3] - bbox[1]

    line_height = get_line_height(font)
    lines = []
    for paragraph in text.split("\n"):
        wrapped = wrap(paragraph, width=32)
        lines.extend(wrapped)

    # کاهش اندازه فونت در صورت نیاز
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

    # پس‌زمینه سفید
    draw.rectangle([x, y, x + w, y + h], fill="white")

    # 📍 وسط‌چینی عمودی
    total_text_height = line_height * len(lines)
    start_y = y + (h - total_text_height) / 2

    # 🆕 اضافه‌کردن فاصله بین خطوط
    line_spacing = int(line_height * 0.3)  # حدود ۳۰٪ ارتفاع خط فاصله اضافه

    for line in lines:
        draw.text((x + padding, start_y), line, fill=fill, font=font)
        start_y += line_height + line_spacing
# ---------- نوشتن ترجمه روی تصویر ----------
def overlay_translated_text(img, boxes):
    img_edit = img.copy()
    draw = ImageDraw.Draw(img_edit)

    if os.path.exists("Vazirmatn-Black.ttf"):
        font = ImageFont.truetype("Vazirmatn-Black.ttf", 22)
    else:
        font = ImageFont.load_default()

    for box in boxes:
        eng_text = box["text"]
        tr_text = translate_text(eng_text)
        if not tr_text:
            continue
        draw_text_in_box(draw, tr_text, box, font)

    return img_edit

# ---------- استخراج عنوان مانگا ----------
def get_clean_manga_title(chapter_url):
    resp = requests.get(chapter_url, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    title_tag = soup.find("title")
    if title_tag and title_tag.text:
        text = title_tag.text.strip()
        text = re.sub(r"[-–]", "", text)
        text = text.replace("English", "").strip()
        text = re.sub(r"[^\w\.]", "", text)
        return text

    parts = chapter_url.strip("/").split("/")
    if parts:
        text = parts[-1].replace("-", "")
        text = re.sub(r"[^\w\.]", "", text)
        return text

    return "MangaChapter"

# ---------- پردازش چپتر و ذخیره ZIP ----------
def process_chapter(chapter_url):
    os.system('rm -rf *.zip ; rm -rf *.jpg')
    urls = fetch_image_urls(chapter_url)
    zip_name = f"{get_clean_manga_title(chapter_url)}.zip"
    saved_files = []

    for i, url in enumerate(urls, start=1):
        try:
            #if url == "https://imgsrv4.com/mg1/fastcdn/cdn_mangaraw/mr-zombie/chapter-123/9.jpg":
              img = download_image(url)
              boxes = ocr_extract_text_boxes(img)
              img2 = overlay_translated_text(img, boxes)

              out_path = f"page_{i:03d}.jpg"
              img2 = img2.convert("RGB")  # اطمینان از تبدیل به RGB برای JPEG
              img2.save(out_path, "JPEG", quality=95)
              saved_files.append(out_path)
              print(f"💾 Saved translated: {out_path}")
        except Exception as e:
            print(f"❌ Error on page {i}: {e}")

    with ZipFile(zip_name, "w") as zipf:
        for file in saved_files:
            try:
                zipf.write(file, arcname=os.path.basename(file))
                os.remove(file)
            except Exception as e:
                print(f"❌ Error on page {file}: {e}")

    print(f"📦 All pages zipped: {zip_name}")

# ---------- اجرای برنامه ----------
if __name__ == "__main__":
    chapter_url = "https://stonescape.xyz/series/cosmicdemon/ch-37/"
    process_chapter(chapter_url)

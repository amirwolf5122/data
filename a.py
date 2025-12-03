#helpz
@app.on(events.NewMessage(pattern=r"^(|(.*))(he_|)(راهنما استثنا منشی|exactionc|excommentc|exmarkreadc|exreactc|exanswerc|extypingc|excontactc|exgamec|exlocationc|exstickerc|exrecord-voicec|exrecord-roundc|exrecord-videoc|exvoicec|exroundc|exvideoc|exphotoc|exfilec|actionmodec|actionc|cmdc|toolhelp2|toolhelp3|toolhelp4|toolhelp5|toolhelp6|toolhelp7|funhelp2|funhelp3|funhelp4|funhelp5|mnghelp2|lovec|lovetxtc|mnghelp3|excommentc|musicc|commentc|foshc|enemyc|exanswerc|answerc|fontc|adminc|gamec|locationc|cprofilec|eprofilec|eprofiletimec|cnamec|enametimec|enamec|statustimec|statusc|راهنما پروفایل|راهنما اسم|راهنما فامیل|راهنما بیو|modehelp2|modehelp3|exmarkreadc|markreadc|help|clerkhelp|gphelp|toolhelp|funhelp|mnghelp|premiumhelp|infohelp|modehelp|exreactc|reactc)$",func=lambda e:chackcmd(e,["وضعیت", "help", "status"]) == 'text' and pattern_admin_or_self(r"^(he_|)(راهنما استثنا منشی|exactionc|actionmodec|actionc|excommentc|exmarkreadc|exreactc|exanswerc|extypingc|excontactc|exgamec|exlocationc|exstickerc|exrecord-voicec|exrecord-roundc|exrecord-videoc|exvoicec|exroundc|exvideoc|exphotoc|exfilec|cmdc|toolhelp2|toolhelp3|toolhelp4|toolhelp5|toolhelp6|toolhelp7|funhelp2|funhelp3|funhelp4|funhelp5|mnghelp2|lovec|lovetxtc|mnghelp3|excommentc|commentc|musicc|foshc|enemyc|exanswerc|answerc|fontc|adminc|gamec|locationc|cprofilec|eprofilec|eprofiletimec|cnamec|enamec|enametimec|statustimec|statusc|راهنما پروفایل|راهنما اسم|راهنما فامیل|راهنما بیو|modehelp2|modehelp3|exmarkreadc|markreadc|help|clerkhelp|gphelp|toolhelp|funhelp|mnghelp|premiumhelp|infohelp|modehelp|exreactc|reactc)$",e)))
async def help1(message):
  chatid=message.sender_id
  axdv = "@" if message.is_private or isinstance(message, events.CallbackQuery.Event) else ""
  textlen = boton["databot"]["adminrun"] if isinstance(message, events.CallbackQuery.Event) and not chatid == int(databot33["me"]) or not isinstance(message, events.CallbackQuery.Event) and not message.out else ""
  text = message.text if not isinstance(message, events.CallbackQuery.Event) else message.data.decode().split(":")[0]
  if not isinstance(message, events.CallbackQuery.Event):
    text=text.replace(str(boton["databot"]["adminrun"]),"",1)
  texthe=text.replace("he_","",1)
  text3 = message.chat_id if not isinstance(message, events.CallbackQuery.Event) else int(message.data.decode().split(":")[-1])
  if (any(cmd in boton["cmd"] for cmd in ["help", texthe]) or
texthe == "toolhelp" and any(cmd in boton["cmd"] for cmd in ["toolhelp2","toolhelp3","toolhelp4","toolhelp5","toolhelp6","toolhelp7"]) or
texthe == "funhelp" and any(cmd in boton["cmd"] for cmd in ["funhelp2","funhelp3","funhelp4","funhelp5"]) or 
texthe == "mnghelp" and any(cmd in boton["cmd"] for cmd in ["mnghelp2","mnghelp3","commentc","lovetxtc","lovec","foshc","enemyc","answerc","fontc","adminc","gamec","reactc"]) or
texthe == "premiumhelp" and any(cmd in boton["cmd"] for cmd in ["cprofilec","eprofilec","eprofiletimec","cnamec","enamec","enametimec","statusc","locationc","statustimec"]) or
texthe == "infohelp" and any(cmd in boton["cmd"] for cmd in ["راهنما پروفایل","راهنما اسم","راهنما فامیل","راهنما بیو"]) or
texthe == "modehelp" and any(cmd in boton["cmd"] for cmd in ["modehelp2","modehelp3","markreadc","musicc"]) or
texthe == "راهنما استثنا منشی" and any(cmd in boton["cmd"] for cmd in ["clerkhelp"])

):
    return
  text4=[]
  text2=""
  if text:
    if texthe =="premiumhelp":
      if databot33["getpremium"]:
        text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}statusc` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش وضعیت اکانت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}enamec` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cnamec` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش رنگ اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}eprofilec` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cprofilec` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش رنگ پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}locationc` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش مکان
"""
        if boton["panelbot"]:
          text4.append([Button.inline("statusc",
                    f'statusc:{text3}'),Button.inline("وضعیت اکانت",
                    'None')])
          text4.append([Button.inline("enamec",
                    f'enamec:{text3}'),Button.inline("ایموجی اسم",
                    'None')])
          text4.append([Button.inline("cnamec",
                    f'cnamec:{text3}'),Button.inline("رنگ اسم",
                    'None')])
          text4.append([Button.inline("eprofilec",
                    f'eprofilec:{text3}'),Button.inline("ایموجی پروفایل",
                    'None')])
          text4.append([Button.inline("cprofilec",
                    f'cprofilec:{text3}'),Button.inline("رنگ پروفایل",
                    'None')])
          text4.append([Button.inline("locationc",
                    f'locationc:{text3}'),Button.inline("مکان",
                    'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[] 
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("(premium)",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
      else:
        await edit_or_reply_message(message,"برای استفاده از این قابلیت پرمیوم نیاز است")
        return
    elif texthe =="help":
      if not "bot" in boton["onlist"]:
        text2=f"""➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}bot on`
ربات خاموش است"""
      else:
        if databot33["getpremium"]:
          text5=f"""[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}premiumhelp`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش پرمیوم
➿〰️〰️〰️〰️〰️〰️〰️➿
"""
          if boton["panelbot"]:
            text4.append([Button.inline("premiumhelp",
                    f'premiumhelp:{text3}'),Button.inline("بخش پرمیوم",
                    'None')])
        else:
          text5=""
        text2=f"""➿〰️〰️〰️〰️〰️〰️〰️➿
{text5}[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}mnghelp`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش مدیریت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}modehelp`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش مدیریت مودها
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}infohelp`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش مدیریت اطلاعات اکانت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}clerkhelp`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش مدیریت منشی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}toolhelp`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش کاربردی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}gphelp`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش گروه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}funhelp`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش سرگرمی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}status` |*| `{textlen}وضعیت`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) چک کردن وضعیت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}panel` |*| `{textlen}پنل`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پنل شیشه ای"""
        if boton["panelbot"]:
          text4.append([Button.inline("mnghelp",
                    f'mnghelp:{text3}'),Button.inline("مدیریت",
                    'None')])
          text4.append([Button.inline("modehelp",
                    f'modehelp:{text3}'),Button.inline("مدیریت مودها",
                    'None')])
          text4.append([Button.inline("infohelp",
                    f'infohelp:{text3}'),Button.inline("مدیریت اطلاعات اکانت",
                    'None')])
          text4.append([Button.inline("clerkhelp",
                    f'clerkhelp:{text3}'),Button.inline("مدیریت منشی",
                    'None')])
          text4.append([Button.inline("toolhelp",
                    f'toolhelp:{text3}'),Button.inline("کاربردی",
                    'None')])
          text4.append([Button.inline("gphelp",
                    f'gphelp:{text3}'),Button.inline("گروه",
                    'None')])
          text4.append([Button.inline("funhelp",
                    f'funhelp:{text3}'),Button.inline("سرگرمی",
                    'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.inline("بستن",
                    f'stop:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "mnghelp":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}adminc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش ادمین سلف
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}fontc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش فونت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}answerc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش متن پاسخ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}settime` <12/24>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم ساعت am-pm
 یا 24 ساعتی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}timezone` <timezone>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تغییر زمان سلف
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}reactc` <emoji> <reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ری اکشن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}block` <UserName><in pv><reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بلاک کردن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}unblock` <UserName><reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) آنبلاک کردن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}mutepv` <UserName><in pv><reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) میوت کردن از پیوی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}unmutepv` <UserName><in pv><reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) انمیوت کردن از پیوی
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}mnghelp2`➿➿
➿ツبخش مدیریت2ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("adminc",
                    f'adminc:{text3}'),Button.inline("بخش ادمین سلف",
                    'None')])
          text4.append([Button.inline("fontc",
                    f'fontc:{text3}'),Button.inline("بخش فونت",
                    'None')])
          text4.append([Button.inline("answerc",
                    f'answerc:{text3}'),Button.inline("بخش متن پاسخ",
                    'None')])
          if text=="he_"+texthe:
            text4.append([Button.url("settime",
                    "https://t.me/amirwolfself/9"),Button.inline("تنظیم ساعت am-pm",
                    'None')])
            text4.append([Button.url("timezone",
                    "https://t.me/amirwolfself/10"),Button.inline("تغییر زمان سلف",
                    'None')])
          else:
            text4.append([Button.inline("settime",
                    f'settime:{text3}'),Button.inline("تنظیم ساعت am-pm",
                    'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("timezone",
                    f'send:timezone:{text3}'),Button.inline("تغییر زمان سلف",
                    'None')])
            else:
              text4.append([Button.url("timezone",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"timezone")),Button.inline("تغییر زمان سلف",
                    'None')])
          text4.append([Button.inline("reactc",
                    f'reactc:{text3}'),Button.inline("ری اکشن",
                    'None')])
          if text=="he_"+texthe:
            text4.append([Button.url("block",
                    "https://t.me/amirwolfself/28"),Button.inline("بلاک کردن",
                    'None')])
            text4.append([Button.url("unblock",
                    "https://t.me/amirwolfself/28"),Button.inline("انبلاک کردن",
                    'None')])
            text4.append([Button.url("mutepv",
                    "https://t.me/amirwolfself/29"),Button.inline("میوت کردن پیوی",
                    'None')])
            text4.append([Button.url("unmutepv",
                    "https://t.me/amirwolfself/29"),Button.inline("انمیوت کردن پیوی",
                    'None')])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("block",
                    f'send:block:{text3}'),Button.inline("بلاک کردن",
                    'None')])
              text4.append([Button.inline("unblock",
                    f'send:unblock:{text3}'),Button.inline("انبلاک کردن",
                    'None')])
              text4.append([Button.inline("mutepv",
                    f'send:mutepv:{text3}'),Button.inline("میوت کردن پیوی",
                    'None')])
              text4.append([Button.inline("unmutepv",
                    f'send:unmutepv:{text3}'),Button.inline("انمیوت کردن پیوی",
                    'None')])
            else:
              text4.append([Button.url("block",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"block")),Button.inline("بلاک کردن",
                    'None')])
              text4.append([Button.url("unblock",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"unblock")),Button.inline("انبلاک کردن",
                    'None')])
              text4.append([Button.url("mutepv",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"mutepv")),Button.inline("میوت کردن پیوی",
                    'None')])
              text4.append([Button.url("unmutepv",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"unmutepv")),Button.inline("انمیوت کردن پیوی",
                    'None')])
          text4.append([Button.inline("(1)",
                    f'mnghelp:{text3}'),Button.inline("2",
                    f'mnghelp2:{text3}'),Button.inline("3",
                    f'mnghelp3:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[] 
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng2)",
                    f'mnghelp2:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "mnghelp2":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}join` <reply><text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) جوین کانال و گروه ریپلی رو متن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}left` <reply><text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لفت کانال و گروه ریپلی رو متن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}gamec`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش گیم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}backup data`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بکاپ گرفتن از دیتا 
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}import data` <reply><file>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ایمپورت دیتا
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}rest data`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ریست کردن دیتا
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleanpv` <num>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی پیام های پیوی به تعداد دلخواه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}commentc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش کامنت اول
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}mnghelp3`➿➿
➿ツبخش مدیریت3ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("join",
                    "https://t.me/amirwolfself/20"),Button.inline("جوین کانال",
                    'None')])
            text4.append([Button.url("left",
                    "https://t.me/amirwolfself/20"),Button.inline("لفت چنل",
                    'None')])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("join",
                    f'send:join:{text3}'),Button.inline("جوین کانال",
                    'None')])
              text4.append([Button.inline("left",
                    f'send:left:{text3}'),Button.inline("لفت چنل",
                    'None')])
            else:
              text4.append([Button.url("join",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"join")),Button.inline("جوین کانال",
                    'None')])
              text4.append([Button.url("left",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"left")),Button.inline("لفت چنل",
                    'None')])
          text4.append([Button.inline("gamec",
                    f'gamec:{text3}'),Button.inline("بخش گیم",
                    'None')])
          if text=="he_"+texthe:
            text4.append([Button.url("backup data",
                    "https://t.me/amirwolfself/17"),Button.inline("بکاپ دیتا",
                    'None')])
            text4.append([Button.url("import data",
                    "https://t.me/amirwolfself/17"),Button.inline("ایمپورت دیتا",
                    'None')])
            text4.append([Button.url("rest data",
                    "https://t.me/amirwolfself/26"),Button.inline("ریست کردن دیتا",
                    'None')])
            text4.append([Button.url("cleanpv",
                    "https://t.me/amirwolfself/21"),Button.inline("پاکسازی پیام پی",
                    'None')])
          else:
            text4.append([Button.inline("backup data",
                    f'backup data:{text3}'),Button.inline("بکاپ دیتا",
                    'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("import data",
                    f'send:import data:{text3}'),Button.inline("ایمپورت دیتا",
                    'None')])
            else:
              text4.append([Button.url("import data",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"import data")),Button.inline("ایمپورت دیتا",
                    'None')])
            text4.append([Button.inline("rest data",
                    f'rest data:{text3}'),Button.inline("ریست کردن دیتا",
                    'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("cleanpv",
                    f'send:cleanpv:{text3}'),Button.inline("پاکسازی پیام پی",
                    'None')])
            else:
              text4.append([Button.url("cleanpv",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"cleanpv")),Button.inline("پاکسازی پیام پی",
                    'None')])
          text4.append([Button.inline("commentc",
                    f'commentc:{text3}'),Button.inline("بخش کامنت اول",
                    'None')])
          text4.append([Button.inline("1",
                    f'mnghelp:{text3}'),Button.inline("(2)",
                    f'mnghelp2:{text3}'),Button.inline("3",
                    f'mnghelp3:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng3)",
                    f'mnghelp3:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "mnghelp3":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}enemyc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش دشمن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}lovec`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش عشق
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cmdc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) قفل کامند
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}setserver` <ip> <username> <password> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) انتقال سرور به سرور جدید
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تمدید زمان سلف 30 روزه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}live` <chatid>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پخش لایو
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}livekey`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم لایو
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}getsession`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) فایل سشن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delself`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف سلف
"""
      if boton["panelbot"]:
          text4.append([Button.inline("enemyc",
                    f'enemyc:{text3}'),Button.inline("بخش دشمن",
                    'None')])
          text4.append([Button.inline("lovec",
                    f'lovec:{text3}'),Button.inline("بخش عشق",
                    'None')])
          text4.append([Button.inline("cmdc",
                    f'cmdc:{text3}'),Button.inline("قفل کامند",
                    'None')])
          if text=="he_"+texthe:
            text4.append([Button.url("setserver",
                    "https://t.me/amirwolfself/137"),Button.inline("انتقال سرور",
                    'None')])
            text4.append([Button.url("live",
                    "https://t.me/amirwolfself/139"),Button.inline("پخش لایو",
                    'None')])
            text4.append([Button.url("livekey",
                    "https://t.me/amirwolfself/143"),Button.inline("تنظیم لایو",
                    'None')])
            text4.append([Button.url("getsession",
                    "https://t.me/amirwolfself/152"),Button.inline("فایل سشن",
                    'None')])
            text4.append([Button.url("delself",
                    "https://t.me/amirwolfself/153"),Button.inline("حذف سلف",
                    'None')])
          else:
            text4.append([Button.inline("setserver",
                    f'setserver:{text3}'),Button.inline("انتقال سرور",
                    'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("live",
                    f'send:live:{text3}'),Button.inline("تنظیم لایو",
                    'None')])
            else:
              text4.append([Button.url("live",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"live")),Button.inline("پخش لایو",
                    'None')])
            text4.append([Button.inline("livekey",
                    f'livekey:{text3}'),Button.inline("تنظیم لایو",
                    'None')])
            text4.append([Button.inline("getsession",
                    f'getsession:{text3}'),Button.inline("فایل سشن",
                    'None')])
            text4.append([Button.inline("delself",
                    f'delself:{text3}'),Button.inline("حذف سلف",
                    'None')])
          text4.append([Button.inline("1",
                    f'mnghelp:{text3}'),Button.inline("2",
                    f'mnghelp2:{text3}'),Button.inline("(3)",
                    f'mnghelp3:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng)",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "modehelp": 
      text2=f"""➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}quote ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت نقل قول
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}part ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت حرف به حرف
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}part2 ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت حرف به حرف2
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}strike ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن خط خورده
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}hashtag ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن هشتگ دار
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}aunderline ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن زیرخط دار
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}bold ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن ضخیم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}italic ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن کج
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}coding ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن کدینگ(قابلیت کپی)
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}coding2 ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن کدینگ2
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}modehelp2`➿➿
➿ツبخش مودها2ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("quote",
                    "https://t.me/amirwolfself/120"),Button.inline("نقل قول",
                    'None')])
            text4.append([Button.url("part",
                    "https://t.me/amirwolfself/30"),Button.inline("حرف به حرف",
                    'None')])
            text4.append([Button.url("part2",
                    "https://t.me/amirwolfself/117"),Button.inline("حرف به حرف2",
                    'None')])
            text4.append([Button.url("strike",
                    "https://t.me/amirwolfself/119"),Button.inline("متن خط خورده",
                    'None')])
            text4.append([Button.url("hashtag",
                    "https://t.me/amirwolfself/31"),Button.inline("متن هشتگ دار",
                    'None')])
            text4.append([Button.url("aunderline",
                    "https://t.me/amirwolfself/32"),Button.inline("متن زیرخط دار",
                    'None')])
            text4.append([Button.url("bold",
                    "https://t.me/amirwolfself/33"),Button.inline("متن ضخیم",
                    'None')])
            text4.append([Button.url("italic",
                    "https://t.me/amirwolfself/34"),Button.inline("متن کج",
                    'None')])
            text4.append([Button.url("coding",
                    "https://t.me/amirwolfself/35"),Button.inline("متن کدینگ",
                    'None')])
            text4.append([Button.url("coding2",
                    "https://t.me/amirwolfself/108"),Button.inline("متن کدینگ2",
                    'None')])
          else:
            text4.append([Button.inline("quote",
                    f'quote:{text3}'),Button.inline("نقل قول",
                    'None')])
            text4.append([Button.inline("part",
                    f'part:{text3}'),Button.inline("حرف به حرف",
                    'None')])
            text4.append([Button.inline("part2",
                    f'part2:{text3}'),Button.inline("حرف به حرف2",
                    'None')])
            text4.append([Button.inline("strike",
                    f'strike:{text3}'),Button.inline("متن خط خورده",
                    'None')])
            text4.append([Button.inline("hashtag",
                    f'hashtag:{text3}'),Button.inline("متن هشتگ دار",
                    'None')])
            text4.append([Button.inline("aunderline",
                    f'aunderline:{text3}'),Button.inline("متن زیرخط دار",
                    'None')])
            text4.append([Button.inline("bold",
                    f'bold:{text3}'),Button.inline("متن ضخیم",
                    'None')])
            text4.append([Button.inline("italic",
                    f'italic:{text3}'),Button.inline("متن کج",
                    'None')])
            text4.append([Button.inline("coding",
                    f'coding:{text3}'),Button.inline("متن کدینگ",
                    'None')])
            text4.append([Button.inline("coding2",
                    f'coding2:{text3}'),Button.inline("متن کدینگ2",
                    'None')])
          text4.append([Button.inline("(1)",
                    f'modehelp:{text3}'),Button.inline("2",
                    f'modehelp2:{text3}'),Button.inline("3",
                    f'modehelp3:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("(mode2)",
                    f'modehelp2:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "modehelp2":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}coding3 ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن کدینگ3
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}coding4 ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن کدینگ4
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}coding5 ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن کدینگ5
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}deleted ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن خط خورده
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}spoiler ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن اسپویلر
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}reverse ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت متن برعکس
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}mention ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت منشن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}mention2 ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت منشن2
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}online` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت آنلاین نگه داشتن اکانت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}markreadc `
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت سین
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}deltime` <off|1|60>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف خودکار پیام
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}modehelp3`➿➿
➿ツبخش مودها2ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("coding3",
                    "https://t.me/amirwolfself/110"),Button.inline("متن کدینگ3",
                    'None')])
            text4.append([Button.url("coding4",
                    "https://t.me/amirwolfself/111"),Button.inline("متن کدینگ4",
                    'None')])
            text4.append([Button.url("coding5",
                    "https://t.me/amirwolfself/112"),Button.inline("متن کدینگ5",
                    'None')])
            text4.append([Button.url("deleted",
                    "https://t.me/amirwolfself/162"),Button.inline("متن خط خورده",
                    'None')])
            text4.append([Button.url("spoiler",
                    "https://t.me/amirwolfself/36"),Button.inline("متن اسپویلر",
                    'None')])
            text4.append([Button.url("reverse",
                    "https://t.me/amirwolfself/37"),Button.inline("متن برعکس",
                    'None')])
            text4.append([Button.url("mention",
                    "https://t.me/amirwolfself/38"),Button.inline("منشن",
                    'None')])
            text4.append([Button.url("mention2",
                    "https://t.me/amirwolfself/39"),Button.inline("منشن2",
                    'None')])
            text4.append([Button.url("online",
                    "https://t.me/amirwolfself/40"),Button.inline("آنلاین نگه داشتن اکانت",
                    'None')])
          else:
            text4.append([Button.inline("coding3",
                    f'coding3:{text3}'),Button.inline("متن کدینگ3",
                    'None')])
            text4.append([Button.inline("coding4",
                    f'coding4:{text3}'),Button.inline("متن کدینگ4",
                    'None')])
            text4.append([Button.inline("coding5",
                    f'coding5:{text3}'),Button.inline("متن کدینگ5",
                    'None')])
            text4.append([Button.inline("deleted",
                    f'deleted:{text3}'),Button.inline("متن خط خورده",
                    'None')])
            text4.append([Button.inline("spoiler",
                    f'spoiler:{text3}'),Button.inline("متن اسپویلر",
                    'None')])
            text4.append([Button.inline("reverse",
                    f'reverse:{text3}'),Button.inline("متن برعکس",
                    'None')])
            text4.append([Button.inline("mention",
                    f'mention:{text3}'),Button.inline("منشن",
                    'None')])
            text4.append([Button.inline("mention2",
                    f'mention2:{text3}'),Button.inline("منشن2",
                    'None')])
            text4.append([Button.inline("online",
                    f'online:{text3}'),Button.inline("آنلاین نگه داشتن اکانت",
                    'None')])
          text4.append([Button.inline("markreadc",
                    f'markreadc:{text3}'),Button.inline("سین",
                    'None')])
          if text=="he_"+texthe:
            text4.append([Button.url("deltime",
                    "https://t.me/amirwolfself/131"),Button.inline("حذف خودکار پیام",
                    'None')])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("deltime",
                    f'send:deltime:{text3}'),Button.inline("حذف خودکار پیام",
                    'None')])
            else:
              text4.append([Button.url("deltime",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"deltime")),Button.inline("حذف خودکار پیام",
                    'None')])
          text4.append([Button.inline("1",
                    f'modehelp:{text3}'),Button.inline("(2)",
                    f'modehelp2:{text3}'),Button.inline("3",
                    f'modehelp3:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("(mode3)",
                    f'modehelp3:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "modehelp3":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}bot ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) غیرفعال کردن ربات
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}lockpv` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) قفل پیوی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}lockpv1` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) قفل پیوی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}autodon` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]})  دانلود خودکار عکس و ویدیو زماندار
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}antilogin` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]})  انتی لاگین
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delmessage` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]})  حالت حذف پیام
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}editmessage` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]})  حالت ویرایش پیام
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}netspeed` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افرایش سرعت دانلود
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}musicc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) موزیک
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}actionc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) اکشن ها
"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("bot",
                    "https://t.me/amirwolfself/42"),Button.inline("غیرفعال کردن ربات",
                    'None')])
            text4.append([Button.url("lockpv",
                    "https://t.me/amirwolfself/163"),Button.inline("قفل پیوی",
                    'None')])
            text4.append([Button.url("lockpv1",
                    "https://t.me/amirwolfself/164"),Button.inline("قفل پیوی2",
                    'None')])
            text4.append([Button.url("autodon",
                    "https://t.me/amirwolfself/113"),Button.inline("دانلود تایمدار",
                    'None')])
            text4.append([Button.url("antilogin",
                    "https://t.me/amirwolfself/121"),Button.inline("انتی لاگین",
                    'None')])
            text4.append([Button.url("delmessage",
                    "https://t.me/amirwolfself/148"),Button.inline("حالت حذف پیام",
                    'None')])
            text4.append([Button.url("editmessage",
                    "https://t.me/amirwolfself/147"),Button.inline("حالت ویرایش پیام",
                    'None')])
            text4.append([Button.url("netspeed",
                    "https://t.me/amirwolfself/151"),Button.inline("افرایش سرعت دانلود",
                    'None')])
          else:
            text4.append([Button.inline("bot",
                    f'bot:{text3}'),Button.inline("غیرفعال کردن ربات",
                    'None')])
            text4.append([Button.inline("lockpv",
                    f'lockpv:{text3}'),Button.inline("قفل پیوی",
                    'None')])
            text4.append([Button.inline("lockpv1",
                    f'lockpv1:{text3}'),Button.inline("قفل پیوی2",
                    'None')])
            text4.append([Button.inline("autodon",
                    f'autodon:{text3}'),Button.inline("دانلود تایمدار",
                    'None')])
            text4.append([Button.inline("antilogin",
                    f'antilogin:{text3}'),Button.inline("انتی لاگین",
                    'None')])
            text4.append([Button.inline("delmessage",
                    f'delmessage:{text3}'),Button.inline("حالت حذف پیام",
                    'None')])
            text4.append([Button.inline("editmessage",
                    f'editmessage:{text3}'),Button.inline("حالت ویرایش پیام",
                    'None')])
            text4.append([Button.inline("netspeed",
                    f'netspeed:{text3}'),Button.inline("افرایش سرعت دانلود",
                    'None')])
          text4.append([Button.inline("musicc",
                    f'musicc:{text3}'),Button.inline("موزیک",
                    'None')])
          text4.append([Button.inline("actionc",
                    f'actionc:{text3}'),Button.inline("اکشن ها",
                    'None')])
          text4.append([Button.inline("1",
                    f'modehelp:{text3}'),Button.inline("2",
                    f'modehelp2:{text3}'),Button.inline("(3)",
                    f'modehelp3:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("(mode)",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "infohelp":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}ساعت` <روشن|خاموش>
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}مشخصات اکانت`
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}تغییر ایدی` <متن>
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}هی ربات`
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}سازنده`
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}راهنما اسم`
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}راهنما فامیل`
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}راهنما بیو`
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}راهنما پروفایل`
"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("ساعت",
                    "https://t.me/amirwolfself/100")])
            text4.append([Button.url("تغییر ایدی",
                    "https://t.me/amirwolfself/104")])
          else:
            text4.append([Button.inline("ساعت",
                    f'ساعت:{text3}'),Button.inline(f"مشخصات اکانت",
                    f'مشخصات اکانت:{text3}')])
            text4.append([Button.inline("هی ربات",
                    f'هی ربات:{text3}'),Button.inline(f"سازنده",
                    f'سازنده:{text3}')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("تغییر ایدی",
                    f'send:تغییر ایدی:{text3}')])
            else:
              text4.append([Button.url("تغییر ایدی",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"تغییر ایدی"))])
          text4.append([Button.inline(f"〰️〰️〰️〰️〰️〰️",
                    'None')])
          text4.append([Button.inline(f"راهنما اسم",
                    f'راهنما اسم:{text3}'),Button.inline(f"راهنما فامیل",
                    f'راهنما فامیل:{text3}')])
          text4.append([Button.inline(f"راهنما بیو",
                    f'راهنما بیو:{text3}'),Button.inline(f"راهنما پروفایل",
                    f'راهنما پروفایل:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("(info)",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "toolhelp":
      text2=f"""➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}time`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ساعت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}2x2` | `{textlen}2+2`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حساب کردن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}tarikhShamci`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تاریخ شمسی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}tarikhMiladi`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تاریخ میلادی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}gpinfo`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) اطلاعات گروه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}user` <userid>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بازکردن پیوی با ایدی عددی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}id` <reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت ایدی عددی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}info` <id>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) اطلاعات فرد
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}fackecnt` <name>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) مخاطب فیک
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}gif` <name>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت گیف
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}toolhelp2`➿➿
➿ツبخش کاربردی2ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("calc",
                    "https://t.me/amirwolfself/83"),Button.inline("حساب کردن",
                    'None')])
            text4.append([Button.url("gpinfo",
                    "https://t.me/amirwolfself/52"),Button.inline("اطلاعات گروه",
                    'None')])
            text4.append([Button.url("user",
                    "https://t.me/amirwolfself/51"),Button.inline("بازکردن پیوی",
                    'None')])
            text4.append([Button.url("id",
                    "https://t.me/amirwolfself/50"),Button.inline("دریافت ایدی عددی",
                    'None')])
            text4.append([Button.url("info",
                    "https://t.me/amirwolfself/53"),Button.inline("اطلاعات فرد",
                    'None')])
            text4.append([Button.url("fackecnt",
                    "https://t.me/amirwolfself/54"),Button.inline("مخاطب فیک",
                    'None')])
            text4.append([Button.url("gif",
                    "https://t.me/amirwolfself/55"),Button.inline("دریافت گیف",
                    'None')])
          else:
            text4.append([Button.inline("time",
                    f'time:{text3}'),Button.inline("ساعت",
                    'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("calc",
                    f'send:2x2:{text3}'),Button.inline("حساب کردن",
                    'None')])
            else:
              text4.append([Button.url("calc",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"2x2")),Button.inline("حساب کردن",
                    'None')])
            text4.append([Button.inline("tarikhShamci",
                    f'tarikhShamci:{text3}'),Button.inline("تاریخ شمسی",
                    'None')])
            text4.append([Button.inline("tarikhMiladi",
                    f'tarikhMiladi:{text3}'),Button.inline("تاریخ میلادی",
                    'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("gpinfo",
                    f'send:gpinfo:{text3}'),Button.inline("اطلاعات گروه",
                    'None')])
              text4.append([Button.inline("user",
                    f'send:user:{text3}'),Button.inline("بازکردن پیوی",
                    'None')])
              text4.append([Button.inline("id",
                    f'send:id:{text3}'),Button.inline("دریافت ایدی عددی",
                    'None')])
              text4.append([Button.inline("info",
                    f'send:info:{text3}'),Button.inline("اطلاعات فرد",
                    'None')])
              text4.append([Button.inline("fackecnt",
                    f'send:fackecnt:{text3}'),Button.inline("مخاطب فیک",
                    'None')])
              text4.append([Button.inline("gif",
                    f'send:gif:{text3}'),Button.inline("دریافت گیف",
                    'None')])
            else:
              text4.append([Button.url("gpinfo",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"gpinfo")),Button.inline("اطلاعات گروه",
                    'None')])
              text4.append([Button.url("user",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"user")),Button.inline("بازکردن پیوی",
                    'None')])
              text4.append([Button.url("id",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"id")),Button.inline("دریافت ایدی عددی",
                    'None')])
              text4.append([Button.url("info",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"info")),Button.inline("اطلاعات فرد",
                    'None')])
              text4.append([Button.url("fackecnt",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"fackecnt")),Button.inline("مخاطب فیک",
                    'None')])
              text4.append([Button.url("gif",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"gif")),Button.inline("دریافت گیف",
                    'None')])
          text4.append([Button.inline("(1)",
                    f'toolhelp:{text3}'),Button.inline("2",
                    f'toolhelp2:{text3}'),Button.inline("3",
                    f'toolhelp3:{text3}'),Button.inline("4",
                    f'toolhelp4:{text3}')])
          text4.append([Button.inline("5",
                    f'toolhelp5:{text3}'),Button.inline("6",
                    f'toolhelp6:{text3}'),Button.inline("7",
                    f'toolhelp7:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("(tool2)",
                    f'toolhelp2:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "toolhelp2":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}giff` <name>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ساخت گیف
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}pic` <name>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت عکس
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}music` <name>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت آهنگ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}music2` <name>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت آهنگ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}sticker` <emoji>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت استیکر
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}apk` <name>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت برنامه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}meme` <name>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت میم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}like` <name>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ساخت متن لایک دار
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}logo` <name>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت لوگو
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}arz`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) قیمت ارز
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}arzd`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) قیمت ارز دیجیتال
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}toolhelp3`➿➿
➿ツبخش کاربردی3ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("giff",
                    "https://t.me/amirwolfself/56"),Button.inline("ساخت گیف",
                    'None')])
            text4.append([Button.url("pic",
                    "https://t.me/amirwolfself/57"),Button.inline("دریافت عکس",
                    'None')])
            text4.append([Button.url("music",
                    "https://t.me/amirwolfself/58"),Button.inline("دریافت آهنگ",
                    'None')])
            text4.append([Button.url("music2",
                    "https://t.me/amirwolfself/58"),Button.inline("دریافت آهنگ",
                    'None')])
            text4.append([Button.url("sticker",
                    "https://t.me/amirwolfself/59"),Button.inline("دریافت استیکر",
                    'None')])
            text4.append([Button.url("apk",
                    "https://t.me/amirwolfself/60"),Button.inline("دریافت برنامه",
                    'None')])
            text4.append([Button.url("meme",
                    "https://t.me/amirwolfself/61"),Button.inline("دریافت میم",
                    'None')])
            text4.append([Button.url("like",
                    "https://t.me/amirwolfself/62"),Button.inline("ساخت متن لایک دار",
                    'None')])
            text4.append([Button.url("logo",
                    "https://t.me/amirwolfself/63"),Button.inline("دریافت لوگو",
                    'None')])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("giff",
                    f'send:giff:{text3}'),Button.inline("ساخت گیف",
                    'None')])
              text4.append([Button.inline("pic",
                    f'send:pic:{text3}'),Button.inline("دریافت عکس",
                    'None')])
              text4.append([Button.inline("music",
                    f'send:music:{text3}'),Button.inline("دریافت آهنگ",
                    'None')])
              text4.append([Button.inline("music2",
                    f'send:music2:{text3}'),Button.inline("دریافت آهنگ",
                    'None')])
              text4.append([Button.inline("sticker",
                    f'send:sticker:{text3}'),Button.inline("دریافت استیکر",
                    'None')])
              text4.append([Button.inline("apk",
                    f'send:apk:{text3}'),Button.inline("دریافت برنامه",
                    'None')])
              text4.append([Button.inline("meme",
                    f'send:meme:{text3}'),Button.inline("دریافت میم",
                    'None')])
              text4.append([Button.inline("like",
                    f'send:like:{text3}'),Button.inline("ساخت متن لایک دار",
                    'None')])
              text4.append([Button.inline("logo",
                    f'send:logo:{text3}'),Button.inline("دریافت لوگو",
                    'None')])
            else:
              text4.append([Button.url("giff",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"giff")),Button.inline("ساخت گیف",
                    'None')])
              text4.append([Button.url("pic",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"pic")),Button.inline("دریافت عکس",
                    'None')])
              text4.append([Button.url("music",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"music")),Button.inline("دریافت آهنگ",
                    'None')])
              text4.append([Button.url("music2",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"music2")),Button.inline("دریافت آهنگ",
                    'None')])
              text4.append([Button.url("sticker",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"sticker")),Button.inline("دریافت استیکر",
                    'None')])
              text4.append([Button.url("apk",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"apk")),Button.inline("دریافت برنامه",
                    'None')])
              text4.append([Button.url("meme",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"meme")),Button.inline("دریافت میم",
                    'None')])
              text4.append([Button.url("like",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"like")),Button.inline("ساخت متن لایک دار",
                    'None')])
              text4.append([Button.url("logo",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"logo")),Button.inline("دریافت لوگو",
                    'None')])
            text4.append([Button.inline("arz",
                    f'arz:{text3}'),Button.inline("قیمت ارز",
                    'None')])
            text4.append([Button.inline("arzd",
                    f'arzd:{text3}'),Button.inline("قیمت ارز دیجیتال",
                    'None')])
          text4.append([Button.inline("1",
                    f'toolhelp:{text3}'),Button.inline("(2)",
                    f'toolhelp2:{text3}'),Button.inline("3",
                    f'toolhelp3:{text3}'),Button.inline("4",
                    f'toolhelp4:{text3}')])
          text4.append([Button.inline("5",
                    f'toolhelp5:{text3}'),Button.inline("6",
                    f'toolhelp6:{text3}'),Button.inline("7",
                    f'toolhelp7:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("(tool3)",
                    f'toolhelp3:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "toolhelp3":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}tala`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) قیمت طلا
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}save` <reply><Link>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) سیوکردن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}fall`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) فال
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}doz` 
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دوز
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}hokm4` 
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حکم 4 نفره
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}hokm2` 
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حکم 2 نفره
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}sang`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) سنگ کاغذ قیچی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}noghte`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بازی نقطه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}tico`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بازی تیکو
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}jamshid`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بازی جمشید
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}toolhelp4`➿➿
➿ツبخش کاربردی4ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("save",
                    "https://t.me/amirwolfself/49"),Button.inline("سیوکردن",
                    'None')])
          else:
            text4.append([Button.inline("tala",
                    f'tala:{text3}'),Button.inline("قیمت طلا",
                    'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("save",
                    f'send:save:{text3}'),Button.inline("سیوکردن",
                    'None')])
            else:
              text4.append([Button.url("save",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"save")),Button.inline("سیوکردن",
                    'None')])
            text4.append([Button.inline("fall",
                    f'fall:{text3}'),Button.inline("فال",
                    'None')])
            text4.append([Button.inline("doz",
                    f'doz:{text3}'),Button.inline("دوز",
                    'None')])
            text4.append([Button.inline("hokm4",
                    f'hokm4:{text3}'),Button.inline("حکم 4 نفره",
                    'None')])
            text4.append([Button.inline("hokm2",
                    f'hokm2:{text3}'),Button.inline("حکم 2 نفره",
                    'None')])
            text4.append([Button.inline("sang",
                    f'sang:{text3}'),Button.inline("سنگ کاغذ قیچی",
                    'None')])
            text4.append([Button.inline("noghte",
                    f'noghte:{text3}'),Button.inline("بازی نقطه",
                    'None')])
            text4.append([Button.inline("tico",
                    f'tico:{text3}'),Button.inline("بازی تیکو",
                    'None')])
            text4.append([Button.inline("jamshid",
                    f'jamshid:{text3}'),Button.inline("بازی جمشید",
                    'None')])
          text4.append([Button.inline("1",
                    f'toolhelp:{text3}'),Button.inline("2",
                    f'toolhelp2:{text3}'),Button.inline("(3)",
                    f'toolhelp3:{text3}'),Button.inline("4",
                    f'toolhelp4:{text3}')])
          text4.append([Button.inline("5",
                    f'toolhelp5:{text3}'),Button.inline("6",
                    f'toolhelp6:{text3}'),Button.inline("7",
                    f'toolhelp7:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("(tool4)",
                    f'toolhelp4:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "toolhelp4":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}gay` <name>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) درصد گی بودن فرد 
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}minrob`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بازی مین روب رو 
➿〰️〰️〰️〰️〰️〰️〰️➿ 
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}joke`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) جوک بصورت رندوم 
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}wiki` <text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) جستجو در ویکی پدیا
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}weather` اسم شهر 
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت وضعیت هوای شهر دلخواه 
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}youtube` <text> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) جستجو در یوتیوب
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}kalame` <مبتدی|ساده|متوسط|سخت|وحشتناک> 
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت بازی از ربات کلمه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}pytube` <url> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دانلود از یوتیوب حداکثر 1 گیگ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}hackgamee` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) هک گیم تلگرام
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}story` <username|id|reply|in pv|link> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دانلود استوری
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}toolhelp5`➿➿
➿ツبخش کاربردی5ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("gay",
                    "https://t.me/amirwolfself/89"),Button.inline("درصد گی",
                    'None')])
            text4.append([Button.url("wiki",
                    "https://t.me/amirwolfself/48"),Button.inline("ویکی پدیا",
                    'None')])
            text4.append([Button.url("weather",
                    "https://t.me/amirwolfself/109"),Button.inline("دریافت وضعیت هوا",
                    'None')])
            text4.append([Button.url("youtube",
                    "https://t.me/amirwolfself/88"),Button.inline("جستجو در یوتیوب",
                    'None')])
            text4.append([Button.url("kalame",
                    "https://t.me/amirwolfself/47"),Button.inline("دریافت بازی کلمه",
                    'None')])
            text4.append([Button.url("pytube",
                    "https://t.me/amirwolfself/19"),Button.inline("دانلود از یوتیوب",
                    'None')])
            text4.append([Button.url("story",
                    "https://t.me/amirwolfself/44"),Button.inline("دانلود استوری",
                    'None')])
            text4.append([Button.url("hackgamee",
                    "https://t.me/amirwolfself/157"),Button.inline("هک گیم تلگرام",
                    'None')])    
          else:
            text4.append([Button.inline("gay",
                    f'gay:{text3}'),Button.inline("درصد گی",
                    'None')])
            text4.append([Button.inline("minrob",
                    f'minrob:{text3}'),Button.inline("بازی مین روب رو",
                    'None')])
            text4.append([Button.inline("joke",
                    f'joke:{text3}'),Button.inline("جوک",
                    'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("wiki",
                    f'send:wiki:{text3}'),Button.inline("ویکی پدیا",
                    'None')])
              text4.append([Button.inline("weather",
                    f'send:weather:{text3}'),Button.inline("دریافت وضعیت هوا",
                    'None')])
              text4.append([Button.inline("youtube",
                    f'send:youtube:{text3}'),Button.inline("جستجو در یوتیوب",
                    'None')])
              text4.append([Button.inline("kalame",
                    f'send:kalame:{text3}'),Button.inline("دریافت بازی کلمه",
                    'None')])
              text4.append([Button.inline("pytube",
                    f'send:pytube:{text3}'),Button.inline("دانلود از یوتیوب",
                    'None')])
              text4.append([Button.inline("story",
                    f'send:story:{text3}'),Button.inline("دانلود استوری",
                    'None')])
            else:
              text4.append([Button.url("wiki",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"wiki")),Button.inline("ویکی پدیا",
                    'None')])
              text4.append([Button.url("weather",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"weather")),Button.inline("دریافت وضعیت هوا",
                    'None')])
              text4.append([Button.url("youtube",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"youtube")),Button.inline("جستجو در یوتیوب",
                    'None')])
              text4.append([Button.url("kalame",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"kalame")),Button.inline("دریافت بازی کلمه",
                    'None')])
              text4.append([Button.url("pytube",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"pytube")),Button.inline("دانلود از یوتیوب",
                    'None')])
              text4.append([Button.url("story",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"story")),Button.inline("دانلود استوری",
                    'None')])
            text4.append([Button.inline("hackgamee",
                    f'hackgamee:{text3}'),Button.inline("هک گیم تلگرام",
                    'None')])
          text4.append([Button.inline("1",
                    f'toolhelp:{text3}'),Button.inline("2",
                    f'toolhelp2:{text3}'),Button.inline("3",
                    f'toolhelp3:{text3}'),Button.inline("(4)",
                    f'toolhelp4:{text3}')])
          text4.append([Button.inline("5",
                    f'toolhelp5:{text3}'),Button.inline("6",
                    f'toolhelp6:{text3}'),Button.inline("7",
                    f'toolhelp7:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("(tool5)",
                    f'toolhelp5:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "toolhelp5":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}don` <reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دانلود عکس و ویدیو زماندار
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}fakecard`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) کارت فیک
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}spam` <number> <reply|text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ارسال متن به صورت جدا
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}flood` <number> <text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ارسال با یک پیام
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}meane` <text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت معنی کلمه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}rev` <text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) برعکس کردن کلمه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}fafont` <text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) فونت فارسی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}font` <text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) فونت انگلیسی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}whois` <site>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت اطلاعات دامنه
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}toolhelp6`➿➿
➿ツبخش کاربردی6ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("don",
                    "https://t.me/amirwolfself/64"),Button.inline("دانلود عکس تایمدار",
                    'None')])
            text4.append([Button.url("spam",
                    "https://t.me/amirwolfself/128"),Button.inline("اسپم",
                    'None')])
            text4.append([Button.url("flood",
                    "https://t.me/amirwolfself/66"),Button.inline("اسپم2",
                    'None')])
            text4.append([Button.url("meane",
                    "https://t.me/amirwolfself/67"),Button.inline("دریافت معنی کلمه",
                    'None')])
            text4.append([Button.url("rev",
                    "https://t.me/amirwolfself/68"),Button.inline("برعکس کردن کلمه",
                    'None')])
            text4.append([Button.url("fafont",
                    "https://t.me/amirwolfself/69"),Button.inline("فونت فارسی",
                    'None')])
            text4.append([Button.url("font",
                    "https://t.me/amirwolfself/70"),Button.inline("فونت انگلیسی",
                    'None')])
            text4.append([Button.url("whois",
                    "https://t.me/amirwolfself/71"),Button.inline("دریافت اطلاعات دامنه",
                    'None')])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("don",
                    f'send:don:{text3}'),Button.inline("دانلود عکس تایمدار",
                    'None')])
            else:
              text4.append([Button.url("don",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"don")),Button.inline("دانلود عکس تایمدار",
                    'None')])
            text4.append([Button.inline("fakecard",
                    f'fakecard:{text3}'),Button.inline("کارت فیک",
                    'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("spam",
                    f'send:spam:{text3}'),Button.inline("اسپم",
                    'None')])
              text4.append([Button.inline("flood",
                    f'send:flood:{text3}'),Button.inline("اسپم2",
                    'None')])
              text4.append([Button.inline("meane",
                    f'send:meane:{text3}'),Button.inline("دریافت معنی کلمه",
                    'None')])
              text4.append([Button.inline("rev",
                    f'send:rev:{text3}'),Button.inline("برعکس کردن کلمه",
                    'None')])
              text4.append([Button.inline("fafont",
                    f'send:fafont:{text3}'),Button.inline("فونت فارسی",
                    'None')])
              text4.append([Button.inline("font",
                    f'send:font:{text3}'),Button.inline("فونت انگلیسی",
                    'None')])
              text4.append([Button.inline("whois",
                    f'send:whois:{text3}'),Button.inline("دریافت اطلاعات دامنه",
                    'None')])
            else:
              text4.append([Button.url("spam",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"spam")),Button.inline("اسپم",
                    'None')])
              text4.append([Button.url("flood",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"flood")),Button.inline("اسپم2",
                    'None')])
              text4.append([Button.url("meane",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"meane")),Button.inline("دریافت معنی کلمه",
                    'None')])
              text4.append([Button.url("rev",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"rev")),Button.inline("برعکس کردن کلمه",
                    'None')])
              text4.append([Button.url("fafont",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"fafont")),Button.inline("فونت فارسی",
                    'None')])
              text4.append([Button.url("font",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"font")),Button.inline("فونت انگلیسی",
                    'None')])
              text4.append([Button.url("whois",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"whois")),Button.inline("دریافت اطلاعات دامنه",
                    'None')])
          text4.append([Button.inline("1",
                    f'toolhelp:{text3}'),Button.inline("2",
                    f'toolhelp2:{text3}'),Button.inline("3",
                    f'toolhelp3:{text3}'),Button.inline("4",
                    f'toolhelp4:{text3}')])
          text4.append([Button.inline("(5)",
                    f'toolhelp5:{text3}'),Button.inline("6",
                    f'toolhelp6:{text3}'),Button.inline("7",
                    f'toolhelp7:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("(tool6)",
                    f'toolhelp6:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "toolhelp6":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}sping` <site>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پینگ سایت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}eid`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) روزهای مانده تا عید
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}age` <y>/<m>/<d>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) محاسبه سن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}screen` <site>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) اسکرین شات از سایت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}proxy`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت پروکسی تلگرام
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}getv2`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت v2ray
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}insta` <Link>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دانلود از اینستاگرام
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}gpint` <Link>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دانلود از پینترست
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}gfile` <url>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تبدیل لینک مستقیم به فایل حداکثر 1 گیگ
➿〰️〰️〰️〰️〰️〰️〰️➿
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}pfile` <reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تبدیل فایل به لینک مستقیم حداکثر 1 گیگ
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}toolhelp7`➿➿
➿ツبخش کاربردی7ツ➿
➿➿➿➿➿➿➿➿""" 
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("sping",
                    "https://t.me/amirwolfself/72"),Button.inline("پینگ سایت",
                    'None')])
            text4.append([Button.url("age",
                    "https://t.me/amirwolfself/73"),Button.inline("محاسبه سن",
                    'None')])
            text4.append([Button.url("screen",
                    "https://t.me/amirwolfself/80"),Button.inline("اسکرین شات سایت",
                    'None')])
            text4.append([Button.url("insta",
                    "https://t.me/amirwolfself/74"),Button.inline("دانلود اینستاگرام",
                    'None')])
            text4.append([Button.url("gpint",
                    "https://t.me/amirwolfself/123"),Button.inline("دانلود پینترست",
                    'None')])
            text4.append([Button.url("gfile",
                    "https://t.me/amirwolfself/25"),Button.inline("لینک به فایل",
                    'None')])
            text4.append([Button.url("pfile",
                    "https://t.me/amirwolfself/24"),Button.inline("فایل به لینک",
                    'None')])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("sping",
                    f'send:don:{text3}'),Button.inline("پینگ سایت",
                    'None')])
            else:
              text4.append([Button.url("sping",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"sping")),Button.inline("پینگ سایت",
                    'None')])
            text4.append([Button.inline("eid",
                    f'eid:{text3}'),Button.inline("روز مانده تا عید",
                    'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("age",
                    f'send:age:{text3}'),Button.inline("محاسبه سن",
                    'None')])
              text4.append([Button.inline("screen",
                    f'send:screen:{text3}'),Button.inline("اسکرین شات سایت",
                    'None')])
            else:
              text4.append([Button.url("age",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"age")),Button.inline("محاسبه سن",
                    'None')])
              text4.append([Button.url("screen",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"screen")),Button.inline("اسکرین شات سایت",
                    'None')])
            text4.append([Button.inline("proxy",
                    f'proxy:{text3}'),Button.inline("دریافت پروکسی",
                    'None')])
            text4.append([Button.inline("getv2",
                    f'getv2:{text3}'),Button.inline("دریافت v2ray",
                    'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("insta",
                    f'send:insta:{text3}'),Button.inline("دانلود اینستاگرام",
                    'None')])
              text4.append([Button.inline("gpint",
                    f'send:gpint:{text3}'),Button.inline("دانلود پینترست",
                    'None')])
              text4.append([Button.inline("gfile",
                    f'send:gfile:{text3}'),Button.inline("لینک به فایل",
                    'None')])
              text4.append([Button.inline("pfile",
                    f'send:pfile:{text3}'),Button.inline("فایل به لینک",
                    'None')])
            else:
              text4.append([Button.url("insta",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"insta")),Button.inline("دانلود اینستاگرام",
                    'None')])
              text4.append([Button.url("gpint",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"gpint")),Button.inline("دانلود پینترست",
                    'None')])
              text4.append([Button.url("gfile",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"gfile")),Button.inline("لینک به فایل",
                    'None')])
              text4.append([Button.url("pfile",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"pfile")),Button.inline("فایل به لینک",
                    'None')])
          text4.append([Button.inline("1",
                    f'toolhelp:{text3}'),Button.inline("2",
                    f'toolhelp2:{text3}'),Button.inline("3",
                    f'toolhelp3:{text3}'),Button.inline("4",
                    f'toolhelp4:{text3}')])
          text4.append([Button.inline("5",
                    f'toolhelp5:{text3}'),Button.inline("(6)",
                    f'toolhelp6:{text3}'),Button.inline("7",
                    f'toolhelp7:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("(tool7)",
                    f'toolhelp7:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "toolhelp7":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}ai` <text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) openai
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}text to voice` <text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تبدیل متن به ویس زن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}text to voice2` <text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تبدیل متن به ویس مرد
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}voice to text`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تبدیل ویس به متن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}music to voice`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تبدیل اهنگ به ویس
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}photo to sticker` <reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تبدیل عکس به استیکر
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}sticker to photo` <reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تبدیل استیکر به عکس
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}sticker to gif` <reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تبدیل استیکر به گیف
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}video to mvideo` <reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تبدیل ویدیو به ویدیو مسیج
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}بگوو` <text><admin>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ارسال متن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}timing` <Time> <text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) زمان بندی
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) مثال 
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}timing 12:00:00 hi`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}ustory` <reply> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) اپلود استوری
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}screenpv` <username|id|reply|in pv>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) اسکرین شات فیک
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}tr` <reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) مترجم
"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("ai",
                    "https://t.me/amirwolfself/75"),Button.inline("openai",
                    'None')])
            text4.append([Button.url("text to voice",
                    "https://t.me/amirwolfself/76"),Button.inline("متن به ویس زن",
                    'None')])
            text4.append([Button.url("text to voice2",
                    "https://t.me/amirwolfself/76"),Button.inline("متن به ویس مرد",
                    'None')])
            text4.append([Button.url("voice to text",
                    "https://t.me/amirwolfself/159"),Button.inline("تبدیل ویس به متن",
                    'None')])
            text4.append([Button.url("music to voice",
                    "https://t.me/amirwolfself/172"),Button.inline("تبدیل اهنگ به ویس",
                    'None')])
            text4.append([Button.url("sticker to photo",
                    "https://t.me/amirwolfself/78"),Button.inline("عکس به استیکر",
                    'None')])
            text4.append([Button.url("sticker to gif",
                    "https://t.me/amirwolfself/79"),Button.inline("استیکر به گیف",
                    'None')])
            text4.append([Button.url("video to mvideo",
                    "https://t.me/amirwolfself/134"),Button.inline("ویدیو به ویدیو مسیج",
                    'None')])
            text4.append([Button.url("بگوو",
                    "https://t.me/amirwolfself/135"),Button.inline("ارسال متن",
                    'None')])
            text4.append([Button.url("timing",
                    "https://t.me/amirwolfself/82"),Button.inline("زمان بندی",
                    'None')])
            text4.append([Button.url("ustory",
                    "https://t.me/amirwolfself/127"),Button.inline("اپلود استوری",
                    'None')])
            text4.append([Button.url("screenpv",
                    "https://t.me/amirwolfself/142"),Button.inline("شات فیک",
                    'None')])
            text4.append([Button.url("tr",
                    "https://t.me/amirwolfself/158"),Button.inline("مترجم",
                    'None')])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("ai",
                    f'send:ai:{text3}'),Button.inline("openai",
                    'None')])
              text4.append([Button.inline("text to voice",
                    f'send:text to voice:{text3}'),Button.inline("متن به ویس زن",
                    'None')])
              text4.append([Button.inline("text to voice2",
                    f'send:text to voice2:{text3}'),Button.inline("متن به ویس مرد",
                    'None')])
              text4.append([Button.inline("voice to text",
                    f'send:voice to text:{text3}'),Button.inline("تبدیل ویس به متن",
                    'None')])
              text4.append([Button.inline("music to voice",
                    f'send:voice to text:{text3}'),Button.inline("تبدیل اهنگ به ویس",
                    'None')])
              text4.append([Button.inline("photo to sticker",
                    f'send:photo to sticker:{text3}'),Button.inline("عکس به استیکر",
                    'None')])
              text4.append([Button.inline("sticker to photo",
                    f'send:sticker to photo:{text3}'),Button.inline("استیکر به عکس",
                    'None')])
              text4.append([Button.inline("sticker to gif",
                    f'send:sticker to gif:{text3}'),Button.inline("استیکر به گیف",
                    'None')])
              text4.append([Button.inline("video to mvideo",
                    f'send:video to mvideo:{text3}'),Button.inline("ویدیو به ویدیو مسیج",
                    'None')])
              text4.append([Button.inline("بگوو",
                    f'send:بگوو:{text3}'),Button.inline("ارسال متن",
                    'None')])
              text4.append([Button.inline("timing",
                    f'send:timing:{text3}'),Button.inline("زمان بندی",
                    'None')])
              text4.append([Button.inline("ustory",
                    f'send:ustory:{text3}'),Button.inline("اپلود استوری",
                    'None')])
              text4.append([Button.inline("screenpv",
                    f'send:screenpv:{text3}'),Button.inline("شات فیک",
                    'None')])
              text4.append([Button.inline("tr",
                    f'send:tr:{text3}'),Button.inline("مترجم",
                    'None')])
            else:
              text4.append([Button.url("ai",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"ai")),Button.inline("openai",
                    'None')])
              text4.append([Button.url("text to voice",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"text to voice")),Button.inline("متن به ویس زن",
                    'None')])
              text4.append([Button.url("text to voice2",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"text to voice2")),Button.inline("متن به ویس مرد",
                    'None')])
              text4.append([Button.url("voice to text",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"voice to text")),Button.inline("تبدیل ویس به متن",
                    'None')])
              text4.append([Button.url("music to voice",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"music to voice")),Button.inline("تبدیل اهنگ به ویس",
                    'None')])
              text4.append([Button.url("photo to sticker",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"photo to sticker")),Button.inline("عکس به استیکر",
                    'None')])
              text4.append([Button.url("sticker to photo",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"sticker to photo")),Button.inline("استیکر به عکس",
                    'None')])
              text4.append([Button.url("sticker to gif",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"sticker to gif")),Button.inline("استیکر به گیف",
                    'None')])
              text4.append([Button.url("video to mvideo",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"video to mvideo")),Button.inline("ویدیو به ویدیو مسیج",
                    'None')])
              text4.append([Button.url("بگوو",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"بگوو")),Button.inline("ارسال متن",
                    'None')])
              text4.append([Button.url("timing",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"timing")),Button.inline("زمان بندی",
                    'None')])
              text4.append([Button.url("ustory",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"ustory")),Button.inline("اپلود استوری",
                    'None')])
              text4.append([Button.url("screenpv",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"screenpv")),Button.inline("شات فیک",
                    'None')])
              text4.append([Button.url("tr",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"tr")),Button.inline("مترجم",
                    'None')])
                    
          text4.append([Button.inline("1",
                    f'toolhelp:{text3}'),Button.inline("2",
                    f'toolhelp2:{text3}'),Button.inline("3",
                    f'toolhelp3:{text3}'),Button.inline("4",
                    f'toolhelp4:{text3}')])
          text4.append([Button.inline("5",
                    f'toolhelp5:{text3}'),Button.inline("6",
                    f'toolhelp6:{text3}'),Button.inline("(7)",
                    f'toolhelp7:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("(tool)",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "gphelp":
      text2=f"""➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}mute ` <reply><username> <admin>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) سکوت کاربر
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}unmute ` <reply><username> <admin>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف سکوت کاربر
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}ban ` <reply><username> <admin>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بن کردن کاربر
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}unban ` <reply><username> <admin>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) آزاد کردن کاربر
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}pin ` <reply> <admin>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) سنجاق
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}unpin ` <reply> <admin>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف سنجاق پیام
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}tag ` <num> <admin>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تگ به تعداد دلخواه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}clean all` <admin>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی پیام های گروه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}clean` <num> <admin>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی پیام های گروه به تعداد دلخواه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}clean me all`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی پیام های گروه
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}clean me` <num>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی پیام های گروه به تعداد دلخواه"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("mute",
                    "https://t.me/amirwolfself/92"),Button.inline("سکوت کاربر",
                    'None')])
            text4.append([Button.url("unmute",
                    "https://t.me/amirwolfself/93"),Button.inline("حذف سکوت کاربر",
                    'None')])
            text4.append([Button.url("ban",
                    "https://t.me/amirwolfself/94"),Button.inline("بن کردن کاربر",
                    'None')])
            text4.append([Button.url("unban",
                    "https://t.me/amirwolfself/95"),Button.inline("آزاد کردن کاربر",
                    'None')])
            text4.append([Button.url("pin",
                    "https://t.me/amirwolfself/96"),Button.inline("سنجاق",
                    'None')])
            text4.append([Button.url("unpin",
                    "https://t.me/amirwolfself/97"),Button.inline("حذف سنجاق",
                    'None')])
            text4.append([Button.url("tag",
                    "https://t.me/amirwolfself/98"),Button.inline("تگ",
                    'None')])
            text4.append([Button.url("clean all",
                    "https://t.me/amirwolfself/99"),Button.inline("پاکسازی پیام گروه",
                    'None')])
            text4.append([Button.url("clean",
                    "https://t.me/amirwolfself/99"),Button.inline("پاکسازی پیام گروه",
                    'None')])
            text4.append([Button.url("clean all",
                    "https://t.me/amirwolfself/130"),Button.inline("پاکسازی پیام گروه",
                    'None')])
            text4.append([Button.url("clean",
                    "https://t.me/amirwolfself/130"),Button.inline("پاکسازی پیام گروه",
                    'None')])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("mute",
                    f'send:mute:{text3}'),Button.inline("سکوت کاربر",
                    'None')])
              text4.append([Button.inline("unmute",
                    f'send:unmute:{text3}'),Button.inline("حذف سکوت کاربر",
                    'None')])
              text4.append([Button.inline("ban",
                    f'send:ban:{text3}'),Button.inline("بن کردن کاربر",
                    'None')])
              text4.append([Button.inline("unban",
                    f'send:unban:{text3}'),Button.inline("آزاد کردن کاربر",
                    'None')])
              text4.append([Button.inline("pin",
                    f'send:pin:{text3}'),Button.inline("سنجاق",
                    'None')])
              text4.append([Button.inline("unpin",
                    f'send:unpin:{text3}'),Button.inline("حذف سنجاق",
                    'None')])
              text4.append([Button.inline("tag",
                    f'send:tag:{text3}'),Button.inline("تگ",
                    'None')])
              text4.append([Button.inline("clean all",
                    f'send:clean all:{text3}'),Button.inline("پاکسازی پیام گروه",
                    'None')])
              text4.append([Button.inline("clean",
                    f'send:clean:{text3}'),Button.inline("پاکسازی پیام گروه",
                    'None')])
              text4.append([Button.inline("clean me all",
                    f'send:clean me all:{text3}'),Button.inline("پاکسازی پیام گروه",
                    'None')])
              text4.append([Button.inline("clean me",
                    f'send:clean me:{text3}'),Button.inline("پاکسازی پیام گروه",
                    'None')])
            else:
              text4.append([Button.url("mute",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"mute")),Button.inline("سکوت کاربر",
                    'None')])
              text4.append([Button.url("unmute",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"unmute")),Button.inline("حذف سکوت کاربر",
                    'None')])
              text4.append([Button.url("ban",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"ban")),Button.inline("بن کردن کاربر",
                    'None')])
              text4.append([Button.url("unban",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"unban")),Button.inline("آزاد کردن کاربر",
                    'None')])
              text4.append([Button.url("pin",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"pin")),Button.inline("سنجاق",
                    'None')])
              text4.append([Button.url("unpin",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"unpin")),Button.inline("حذف سنجاق پیام",
                    'None')])
              text4.append([Button.url("tag",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"tag")),Button.inline("تگ",
                    'None')])
              text4.append([Button.url("clean all",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"clean all")),Button.inline("پاکسازی پیام گروه",
                    'None')])
              text4.append([Button.url("clean",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"clean")),Button.inline("پاکسازی پیام گروه",
                    'None')])
              text4.append([Button.url("clean me all",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"clean me all")),Button.inline("پاکسازی پیام گروه",
                    'None')])
              text4.append([Button.url("clean me",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"clean me")),Button.inline("پاکسازی پیام گروه",
                    'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("(group)",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "funhelp":
      text2=f"""➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}ماشین`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}موتور`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}پنالتی`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}تاس`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}روانی`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}ساک`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}جق`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}عشق`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}آدم فضایی`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}موشک`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}پول`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}خزوخیل`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}روح`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}برم خونه`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}قلب`
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}funhelp2`➿➿
➿ツبخش سرگرمی2ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("ماشین",
                    f'ماشین:{text3}'),Button.inline("موتور",
                    f'موتور:{text3}'),Button.inline("پنالتی",
                    f'پنالتی:{text3}'),Button.inline("تاس",
                    f'تاس:{text3}')])
          text4.append([Button.inline("روانی",
                    f'روانی:{text3}'),Button.inline("ساک",
                    f'ساک:{text3}'),Button.inline("جق",
                    f'جق:{text3}'),Button.inline("عشق",
                    f'عشق:{text3}')])
          text4.append([Button.inline("آدم فضایی",
                    f'آدم فضایی:{text3}'),Button.inline("موشک",
                    f'موشک:{text3}'),Button.inline("پول",
                    f'پول:{text3}'),Button.inline("خزوخیل",
                    f'خزوخیل:{text3}')])
          text4.append([Button.inline("روح",
                    f'روح:{text3}'),Button.inline("برم خونه",
                    f'برم خونه:{text3}'),Button.inline("قلب",
                    f'قلب:{text3}')])
          text4.append([Button.inline("(1)",
                    f'funhelp:{text3}'),Button.inline("2",
                    f'funhelp2:{text3}'),Button.inline("3",
                    f'funhelp3:{text3}')])
          text4.append([Button.inline("4",
                    f'funhelp4:{text3}'),Button.inline("5",
                    f'funhelp5:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("(fun2)",
                    f'funhelp2:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "funhelp2":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}شکست عشقی`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}عقاب`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}حموم`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}آپدیت`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}بکشش`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}مسجد`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}کوسه`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}بارون`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}بادکنک`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}شب بخیر`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}فیشینگ`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}گل بزن`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}برم بخابم`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}غرقش کن`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}فضانورد`
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}funhelp3`➿➿
➿ツبخش سرگرمی3ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("شکست عشقی",
                    f'شکست عشقی:{text3}'),Button.inline("عقاب",
                    f'عقاب:{text3}'),Button.inline("حموم",
                    f'حموم:{text3}'),Button.inline("آپدیت",
                    f'آپدیت:{text3}')])
          text4.append([Button.inline("بکشش",
                    f'بکشش:{text3}'),Button.inline("مسجد",
                    f'مسجد:{text3}'),Button.inline("کوسه",
                    f'کوسه:{text3}'),Button.inline("بارون",
                    f'بارون:{text3}')])
          text4.append([Button.inline("بادکنک",
                    f'بادکنک:{text3}'),Button.inline("شب بخیر",
                    f'شب بخیر:{text3}'),Button.inline("فیشینگ",
                    f'فیشینگ:{text3}'),Button.inline("گل بزن",
                    f'گل بزن:{text3}')])
          text4.append([Button.inline("برم بخابم",
                    f'برم بخابم:{text3}'),Button.inline("برم خونه",
                    f'برم خونه:{text3}'),Button.inline("غرقش کن",
                    f'غرقش کن:{text3}'),Button.inline("فضانورد",
                    f'فضانورد:{text3}')])
          text4.append([Button.inline("1",
                    f'funhelp:{text3}'),Button.inline("(2)",
                    f'funhelp2:{text3}'),Button.inline("3",
                    f'funhelp3:{text3}')])
          text4.append([Button.inline("4",
                    f'funhelp4:{text3}'),Button.inline("5",
                    f'funhelp5:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("(fun3)",
                    f'funhelp3:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "funhelp3":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}بزن قدش`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}فیل`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}فاک`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}بشمار`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}بخند`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}بمیر کرونا`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}انگشت`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}جقیم`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}ریدیم`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}کیرخر`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}مکعب`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}فاک2`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}رقص`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}کاکتوس`
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}funhelp4`➿➿
➿ツبخش سرگرمی4ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("بزن قدش",
                    f'بزن قدش:{text3}'),Button.inline("فیل",
                    f'فیل:{text3}'),Button.inline("حموم",
                    f'حموم:{text3}'),Button.inline("فاک",
                    f'فاک:{text3}')])
          text4.append([Button.inline("بشمار",
                    f'بشمار:{text3}'),Button.inline("بخند",
                    f'بخند:{text3}'),Button.inline("بمیر کرونا",
                    f'بمیر کرونا:{text3}'),Button.inline("انگشت",
                    f'انگشت:{text3}')])
          text4.append([Button.inline("جقیم",
                    f'جقیم:{text3}'),Button.inline("ریدیم",
                    f'ریدیم:{text3}'),Button.inline("کیرخر",
                    f'کیرخر:{text3}'),Button.inline("مکعب",
                    f'مکعب:{text3}')])
          text4.append([Button.inline("فاک2",
                    f'فاک2:{text3}'),Button.inline("رقص",
                    f'رقص:{text3}'),Button.inline("کاکتوس",
                    f'کاکتوس:{text3}')])
          text4.append([Button.inline("1",
                    f'funhelp:{text3}'),Button.inline("2",
                    f'funhelp2:{text3}'),Button.inline("(3)",
                    f'funhelp3:{text3}')])
          text4.append([Button.inline("4",
                    f'funhelp4:{text3}'),Button.inline("5",
                    f'funhelp5:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("(fun4)",
                    f'funhelp4:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "funhelp4":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}بوس`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}تپش`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}قلبز`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}فاک3`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}سگ`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}سکسی`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}گلب`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}قلب2`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}ماشین`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}رقص2`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}بکششش`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}بکیرم2`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}زنبور`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}زنبور2`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}نخوندم`
➿〰️〰️〰️〰️〰️〰️〰️➿
➿➿➿➿➿➿➿
➿➿`{textlen}funhelp5`➿➿
➿ツبخش سرگرمی5ツ➿
➿➿➿➿➿➿➿➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("بوس",
                    f'بوس:{text3}'),Button.inline("تپش",
                    f'تپش:{text3}'),Button.inline("قلبز",
                    f'قلبز:{text3}'),Button.inline("فاک3",
                    f'فاک3:{text3}')])
          text4.append([Button.inline("سگ",
                    f'سگ:{text3}'),Button.inline("سکسی",
                    f'سکسی:{text3}'),Button.inline("گلب",
                    f'گلب:{text3}'),Button.inline("قلب2",
                    f'قلب2:{text3}')])
          text4.append([Button.inline("ماشین",
                    f'ماشین:{text3}'),Button.inline("رقص2",
                    f'رقص2:{text3}'),Button.inline("بکششش",
                    f'بکششش:{text3}'),Button.inline("بکیرم2",
                    f'بکیرم2:{text3}')])
          text4.append([Button.inline("زنبور",
                    f'زنبور:{text3}'),Button.inline("زنبور2",
                    f'زنبور2:{text3}'),Button.inline("نخوندم",
                    f'نخوندم:{text3}')])
          text4.append([Button.inline("1",
                    f'funhelp:{text3}'),Button.inline("2",
                    f'funhelp2:{text3}'),Button.inline("3",
                    f'funhelp3:{text3}')])
          text4.append([Button.inline("(4)",
                    f'funhelp4:{text3}'),Button.inline("5",
                    f'funhelp5:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("(fun5)",
                    f'funhelp5:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "funhelp5":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}هک`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}clock`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}دایناسور`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}تانک`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}دهنت سرویس`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}love3`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}کرج`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}مرگ بر امریکا`"""
      if boton["panelbot"]:
          text4.append([Button.inline("هک",
                    f'هک:{text3}'),Button.inline("clock",
                    f'clock:{text3}'),Button.inline("دایناسور",
                    f'دایناسور:{text3}')])
          text4.append([Button.inline("تانک",
                    f'تانک:{text3}'),Button.inline("دهنت سرویس",
                    f'دهنت سرویس:{text3}'),Button.inline("love3",
                    f'love3:{text3}'),Button.inline("کرج",
                    f'کرج:{text3}')])
          text4.append([Button.inline("مرگ بر امریکا",
                    f'مرگ بر امریکا:{text3}'),Button.inline("رقص2",
                    f'رقص2:{text3}')])
          text4.append([Button.inline("1",
                    f'funhelp:{text3}'),Button.inline("2",
                    f'funhelp2:{text3}'),Button.inline("3",
                    f'funhelp3:{text3}')])
          text4.append([Button.inline("4",
                    f'funhelp4:{text3}'),Button.inline("(5)",
                    f'funhelp5:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("(fun)",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "راهنما اسم":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
برای استفاده از
ساعت متن👇
`[ساعت ساده]`
ساعت فارسی متن👇
`[ساعت فارسی]`
ساعت رندوم متن👇
`[ساعت رندوم]`
ساعت ریز متن👇
`[ساعت ریز]`
ساعت درشت متن👇
`[ساعت درشت]`
روز متن👇
`[روز]`
روز به صورت انگلیسی متن👇
`[روز انگلیسی]`
تاریخ متن👇
`[تاریخ]`
تاریخ میلادی متن👇
`[تاریخ میلادی]`
استفاده کنید
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}تغییر اسم` <متن>

`{textlen}اسم` <روشن|خاموش>

`{textlen}اسم جدید`

`{textlen}حذف اسم`

`{textlen}حذف لیست اسم`

`{textlen}لیست اسم`

`{textlen}تنظیم تایم اسم`
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("تغییر اسم",
                    "https://t.me/amirwolfself/101"),Button.url("اسم <روشن|خاموش>",
                    "https://t.me/amirwolfself/114")])
            text4.append([Button.url("اسم جدید",
                    "https://t.me/amirwolfself/114"),Button.url("حذف اسم",
                    "https://t.me/amirwolfself/114")])
            text4.append([Button.url("حذف لیست اسم",
                    "https://t.me/amirwolfself/114"),Button.url("لیست اسم",
                    "https://t.me/amirwolfself/114")])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("تغییر اسم",
                    f'send:تغییر اسم:{text3}'),Button.inline("اسم <روشن|خاموش>",
                    f'اسم:{text3}')])
            else:
              text4.append([Button.url("تغییر اسم",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"تغییر اسم")),Button.inline(f"اسم <روشن|خاموش>",
                    f'اسم:{text3}')])
            text4.append([Button.inline("اسم جدید",
                    f'اسم جدید:{text3}'),Button.inline("حذف اسم",
                    f'حذف اسم:{text3}')])
            text4.append([Button.inline("حذف لیست اسم",
                    f'حذف لیست اسم:{text3}'),Button.inline(f"لیست اسم",
                    f'لیست اسم:0:{text3}')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("تنظیم تایم اسم",
                    f'send:تنظیم تایم اسم:{text3}')])
            else:
              text4.append([Button.url("تنظیم تایم اسم",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"تنظیم تایم اسم"))])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("(info)",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'infohelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe =="clerkhelp":
      text2=f"""➿〰️〰️〰️〰️〰️〰️〰️➿
{textlen}`منشی خودکار` <روشن|خاموش>
➖روشن
زمانی که افلاین شدید کار میکنه
➖خاموش
همه مدت کار میکنه

`{textlen}تنظیم منشی` <replay-channel>

`{textlen}تنظیم زمان منشی` <5-60>

`{textlen}منشی زمان` <روشن|خاموش>
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}منشی دستی` <روشن|خاموش>

خاموش -روشن کردن منشی ها
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}راهنما استثنا منشی`"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("تنظیم منشی",
                    "https://t.me/amirwolfself/129"),Button.url("منشی خودکار",
                    "https://t.me/amirwolfself/116")])
            text4.append([Button.url("منشی دستی",
                    "https://t.me/amirwolfself/116"),Button.url("تنظیم زمان منشی",
                    "https://t.me/amirwolfself/116")])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("تنظیم منشی",
                    f'send:تنظیم منشی:{text3}'),Button.inline("منشی خودکار",
                    f'منشی خودکار:{text3}')])
              text4.append([Button.inline("منشی دستی",
                    f'منشی دستی:{text3}'),Button.inline("تنظیم زمان منشی",
                    f'send:تنظیم زمان منشی:{text3}')])
            else:
              text4.append([Button.url("تنظیم منشی",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"تنظیم منشی")),Button.inline(f"منشی خودکار ",
                    f'منشی خودکار:{text3}')])
              text4.append([Button.inline(f"منشی دستی",
                    f'منشی دستی:{text3}'),Button.url("تنظیم زمان منشی",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"تنظیم زمان منشی"))])
          text4.append([Button.inline("راهنما استثنا منشی",
                    f'راهنما استثنا منشی:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("(clerk)",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'help:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe =="راهنما استثنا منشی":
      text2=f"""➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}تنظیم استثنا منشی`
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}حذف استثنا منشی`
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}لیست استثنا منشی`
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}پاکسازی استثنا منشی`
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}استثنا منشی` <هرگز|مجاز>
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("حذف استثنا منشی",
                    f'حذف استثنا منشی:{text3}'),Button.inline("تنظیم استثنا منشی",
                    f'تنظیم استثنا منشی:{text3}')])
          text4.append([Button.inline("پاکسازی استثنا منشی",
                    f'پاکسازی استثنا منشی:{text3}'),Button.inline("لیست استثنا منشی",
                    f'لیست استثنا منشی:0:{text3}')])
          text4.append([Button.inline("استثنا منشی",
                    f'استثنا منشی:{text3}'),Button.inline("منشی خودکار",
                    f'منشی خودکار:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("(clerk)",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.inline("بازگشت",
                    f'clerkhelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "راهنما فامیل":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
برای استفاده از
ساعت متن👇
`[ساعت ساده]`
ساعت فارسی متن👇
`[ساعت فارسی]`
ساعت رندوم متن👇
`[ساعت رندوم]`
ساعت ریز متن👇
`[ساعت ریز]`
ساعت درشت متن👇
`[ساعت درشت]`
روز متن👇
`[روز]`
روز به صورت انگلیسی متن👇
`[روز انگلیسی]`
تاریخ متن👇
`[تاریخ]`
تاریخ میلادی متن👇
`[تاریخ میلادی]`
استفاده کنید
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}تغییر فامیل` <متن>

`{textlen}فامیل` <روشن|خاموش>

`{textlen}فامیل جدید`

`{textlen}حذف فامیل`

`{textlen}حذف لیست فامیل`

`{textlen}لیست فامیل`

`{textlen}تنظیم تایم فامیل`
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("تغییر فامیل",
                    "https://t.me/amirwolfself/102"),Button.url(f"فامیل <روشن|خاموش>",
                    "https://t.me/amirwolfself/114")])
            text4.append([Button.url("فامیل جدید",
                    "https://t.me/amirwolfself/114"),Button.url("حذف فامیل",
                    "https://t.me/amirwolfself/114")])
            text4.append([Button.url("حذف لیست فامیل",
                    "https://t.me/amirwolfself/114"),Button.url("لیست فامیل",
                    "https://t.me/amirwolfself/114")])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("تغییر فامیل",
                    f'send:تغییر فامیل:{text3}'),Button.inline(f"فامیل <روشن|خاموش>",
                    f'فامیل:{text3}')])
            else:
              text4.append([Button.url("تغییر فامیل",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"تغییر فامیل")),Button.inline(f"فامیل <روشن|خاموش>",
                    f'فامیل:{text3}')])
            text4.append([Button.inline("فامیل جدید",
                    f'فامیل جدید:{text3}'),Button.inline("حذف فامیل",
                    f'حذف فامیل:{text3}')])
            text4.append([Button.inline("حذف لیست فامیل",
                    f'حذف لیست فامیل:{text3}'),Button.inline(f"لیست فامیل",
                    f'لیست فامیل:0:{text3}')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("تنظیم تایم فامیل",
                    f'send:تنظیم تایم فامیل:{text3}')])
            else:
              text4.append([Button.url("تنظیم تایم فامیل",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"تنظیم تایم فامیل"))])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("(info)",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'infohelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "راهنما بیو":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
برای استفاده از
ساعت متن👇
`[ساعت ساده]`
ساعت فارسی متن👇
`[ساعت فارسی]`
ساعت رندوم متن👇
`[ساعت رندوم]`
ساعت ریز متن👇
`[ساعت ریز]`
ساعت درشت متن👇
`[ساعت درشت]`
روز متن👇
`[روز]`
روز به صورت انگلیسی متن👇
`[روز انگلیسی]`
تاریخ متن👇
`[تاریخ]`
تاریخ میلادی متن👇
`[تاریخ میلادی]`
استفاده کنید
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}تغییر بیو` <متن>

`{textlen}بیو` <روشن|خاموش>

`{textlen}بیو جدید`

`{textlen}حذف بیو`

`{textlen}حذف لیست بیو`

`{textlen}لیست بیو`

`{textlen}تنظیم تایم بیو`
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("تغییر بیو",
                    "https://t.me/amirwolfself/103"),Button.url("بیو <روشن|خاموش>",
                    "https://t.me/amirwolfself/114")])
            text4.append([Button.url("بیو جدید",
                    "https://t.me/amirwolfself/114"),Button.url("حذف بیو",
                    "https://t.me/amirwolfself/114")])
            text4.append([Button.url("حذف لیست بیو",
                    "https://t.me/amirwolfself/114"),Button.url("لیست بیو",
                    "https://t.me/amirwolfself/114")])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("تغییر بیو",
                    f'send:تغییر بیو:{text3}'),Button.inline("بیو <روشن|خاموش>",
                    f'بیو:{text3}')])
            else:
              text4.append([Button.url("تغییر بیو",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"تغییر بیو")),Button.inline(f"بیو <روشن|خاموش>",
                    f'بیو:{text3}')])
            text4.append([Button.inline("بیو جدید",
                    f'بیو جدید:{text3}'),Button.inline("حذف بیو",
                    f'حذف بیو:{text3}')])
            text4.append([Button.inline("حذف لیست بیو",
                    f'حذف لیست بیو:{text3}'),Button.inline("لیست بیو",
                    f'لیست بیو:0:{text3}')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("تنظیم تایم بیو",
                    f'send:تنظیم تایم بیو:{text3}')])
            else:
              text4.append([Button.url("تنظیم تایم بیو",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"تنظیم تایم بیو"))])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("(info)",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'infohelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "راهنما پروفایل":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}تنظیم پروفایل` <ریپلی>

`{textlen}تغییر پروفایل` <ریپلی>

`{textlen}کلون پروفایل` <ریپلی>

`{textlen}حذف تعداد پروفایل ` <عدد>

`{textlen}پروفایل` <روشن|خاموش>

`{textlen}تنظیم تایم پروفایل` <12|59>

`{textlen}حالت پروفایل` <ویدیو|عکس|همه>

➿〰️〰️〰️〰️〰️〰️〰️➿
`{textlen}تنظیم حذف پروفایل ` <عدد>
عدد `-1`:
حذف کامل پروفایل گذاشتن پروفایل جدید
عدد `0`:
گذاشتن پروفایل جدید بدون حذف پروفایل
بقیه:
حذف پروفایل بعد از عدد مورد نظرتون و پروفایل جدید
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("تنظیم پروفایل",
                    "https://t.me/amirwolfself/106"),Button.url("تغییر پروفایل",
                    "https://t.me/amirwolfself/105")])
            text4.append([Button.url("کلون پروفایل",
                    "https://t.me/amirwolfself/22")])
            text4.append([Button.url("پروفایل <روشن|خاموش>",
                    "https://t.me/amirwolfself/106")])
            text4.append([Button.url("حالت پروفایل",
                    "https://t.me/amirwolfself/170")])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("تنظیم پروفایل",
                    f'send:تنظیم پروفایل:{text3}'),Button.inline("تغییر پروفایل",
                    f'send:تغییر پروفایل:{text3}')])
              text4.append([Button.inline("کلون پروفایل",
                    f'send:کلون پروفایل:{text3}'),Button.inline("حذف تعداد پروفایل",
                    f'send:حذف تعداد پروفایل:{text3}')])
              text4.append([Button.inline("تنظیم تایم پروفایل",
                    f'send:تنظیم تایم پروفایل:{text3}')]) 
            else:
              text4.append([Button.url("کلون پروفایل",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"کلون پروفایل")),Button.url("حذف تعداد پروفایل",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"حذف تعداد پروفایل"))])
              text4.append([Button.url("تنظیم پروفایل",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"تنظیم پروفایل")),Button.url("حذف تعداد پروفایل",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"حذف تعداد پروفایل"))])
              text4.append([Button.url("تنظیم تایم پروفایل",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"تنظیم تایم پروفایل"))])
            text4.append([Button.inline("پروفایل <روشن|خاموش>",
                    f'پروفایل:{text3}')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("تنظیم حذف پروفایل",
                    f'send:تنظیم حذف پروفایل:{text3}')])
            else:
              text4.append([Button.url("تنظیم حذف پروفایل",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"تنظیم حذف پروفایل"))])
            text4.append([Button.inline("حالت پروفایل",
                    f'حالت پروفایل:{text3}')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("(info)",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'infohelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "statusc":
      if databot33["getpremium"]:
        text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}chstatus` <on|off> <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) وضعیت اکانت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}addstatus` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن وضعیت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delstatus` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف وضعیت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleanstatus` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست وضعیت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}statuslist` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست وضعیت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}ststatus` <Premium><1-59>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم تایم وضعیت اکانت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}statustimec` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش زمان وضعیت اکانت
➿〰️〰️〰️〰️〰️〰️〰️➿"""
        if boton["panelbot"]:
          text4.append([Button.inline("chstatus",
                    f'chstatus:{text3}'),Button.inline("وضعیت اکانت",
                    f'None')])
          text4.append([Button.inline("addstatus",
                    f'addstatus:{text3}'),Button.inline("افزودن وضعیت",
                    f'None')])
          text4.append([Button.inline("delstatus",
                    f'delstatus:{text3}'),Button.inline("حذف وضعیت",
                    f'None')])
          text4.append([Button.inline("cleanstatus",
                    f'cleanstatus:{text3}'),Button.inline("پاکسازی لیست وضعیت",
                    f'None')])
          text4.append([Button.inline("statuslist",
                    f'statuslist:0:{text3}'),Button.inline("لیست وضعیت",
                    f'None')])
          if chatid == int(databot33["me"]):
            text4.append([Button.inline("ststatus",
                    f'send:ststatus:{text3}'),Button.inline("تنظیم تایم وضعیت اکانت",
                    f'None')])
          else:
            text4.append([Button.url("ststatus",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"ststatus")),Button.inline("تنظیم تایم وضعیت اکانت",
                    f'None')])
          text4.append([Button.inline("statustimec",
                    f'statustimec:{text3}'),Button.inline("زمان وضعیت اکانت",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("(premium)",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/122')])
          text4.append([Button.inline("بازگشت",
                    f'premiumhelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
      else:
        await edit_or_reply_message(message,"برای استفاده از این قابلیت پرمیوم نیاز است")
        return
    elif texthe == "statustimec":
      if databot33["getpremium"]:
        text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}chstatustime` <on|off> <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) زمان وضعیت 
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}addstatustime` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن زمان وضعیت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delstatustime` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف زمان وضعیت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleanstatustime` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست زمان وضعیت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}statustimelist` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست زمان وضعیت
➿〰️〰️〰️〰️〰️〰️〰️➿"""
        if boton["panelbot"]:
          text4.append([Button.inline("chstatustime",
                    f'chstatustime:{text3}'),Button.inline("زمان وضعیت",
                    f'None')])
          text4.append([Button.inline("addstatustime",
                    f'addstatustime:{text3}'),Button.inline("افزودن زمان وضعیت",
                    f'None')])
          text4.append([Button.inline("delstatustime",
                    f'delstatus:{text3}'),Button.inline("حذف زمان وضعیت",
                    f'None')])
          text4.append([Button.inline("cleanstatustime",
                    f'cleanstatustime:{text3}'),Button.inline("پاکسازی لیست زمان وضعیت",
                    f'None')])
          text4.append([Button.inline("statustimelist",
                    f'statustimelist:0:{text3}'),Button.inline("لیست زمان وضعیت",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("(premium)",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/166')])
          text4.append([Button.inline("بازگشت",
                    f'statusc:{text3}')])
          text4 = botp.build_reply_markup(text4)
      else:
        await edit_or_reply_message(message,"برای استفاده از این قابلیت پرمیوم نیاز است")
        return
    elif texthe == "locationc":
      if databot33["getpremium"]:
        text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}location` <on|off> <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) مکان
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}addlocation` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن متن مکان
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}dellocation` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف متن مکان
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleanlocation` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست مکان
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}locationlist` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست متن مکان
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}stlocation` <Premium><1-59>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم تایم مکان
➿〰️〰️〰️〰️〰️〰️〰️➿"""
        if boton["panelbot"]:
          text4.append([Button.inline("location",
                    f'location:{text3}'),Button.inline("مکان",
                    f'None')])
          text4.append([Button.inline("addlocation",
                    f'addlocation:{text3}'),Button.inline("افزودن متن مکان",
                    f'None')])
          text4.append([Button.inline("dellocation",
                    f'dellocation:{text3}'),Button.inline("حذف متن مکان",
                    f'None')])
          text4.append([Button.inline("cleanlocation",
                    f'cleanlocation:{text3}'),Button.inline("پاکسازی لیست مکان",
                    f'None')])
          text4.append([Button.inline("locationlist",
                    f'locationlist:0:{text3}'),Button.inline("لیست متن مکان",
                    f'None')])
          if chatid == int(databot33["me"]):
            text4.append([Button.inline("stlocation",
                    f'send:stlocation:{text3}'),Button.inline("تنظیم تایم مکان",
                    f'None')])
          else:
            text4.append([Button.url("stlocation",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"stlocation")),Button.inline("تنظیم تایم مکان",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("(premium)",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/150')])
          text4.append([Button.inline("بازگشت",
                    f'premiumhelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
      else:
        await edit_or_reply_message(message,"برای استفاده از این قابلیت پرمیوم نیاز است")
        return
    elif texthe == "enamec":
      if databot33["getpremium"]:
        text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}ename` <on|off> <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}addename` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delename` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleanename` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}enamelist` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}stename` <Premium><1-59>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم تایم ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}enametimec` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) زمان ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿"""
        if boton["panelbot"]:
          text4.append([Button.inline("ename",
                    f'ename:{text3}'),Button.inline("ایموجی اسم",
                    f'None')])
          text4.append([Button.inline("addename",
                    f'addename:{text3}'),Button.inline("افزودن ایموجی اسم",
                    f'None')])
          text4.append([Button.inline("delename",
                    f'delename:{text3}'),Button.inline("حذف ایموجی اسم",
                    f'None')])
          text4.append([Button.inline("cleanename",
                    f'cleanename:{text3}'),Button.inline("پاکسازی لیست ایموجی اسم",
                    f'None')])
          text4.append([Button.inline("enamelist",
                    f'enamelist:0:{text3}'),Button.inline("لیست ایموجی اسم",
                    f'None')])
          if chatid == int(databot33["me"]):
            text4.append([Button.inline("stename",
                    f'send:stename:{text3}'),Button.inline("تنظیم تایم ایموجی اسم",
                    f'None')])
          else:
            text4.append([Button.url("stename",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"stename")),Button.inline("تنظیم تایم ایموجی اسم",
                    f'None')])
          text4.append([Button.inline("enametimec",
                    f'enametimec:{text3}'),Button.inline("زمان ایموجی اسم",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("(premium)",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/167')])
          text4.append([Button.inline("بازگشت",
                    f'premiumhelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
      else:
        await edit_or_reply_message(message,"برای استفاده از این قابلیت پرمیوم نیاز است")
        return
    elif texthe == "enametimec":
      if databot33["getpremium"]:
        text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}enametime` <on|off> <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) زمان ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}addenametime` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن زمان ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delenametime` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف زمان ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleanenametime` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست زمان ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}enametimelist` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست زمان ایموجی اسم
➿〰️〰️〰️〰️〰️〰️〰️➿"""
        if boton["panelbot"]:
          text4.append([Button.inline("enametime",
                    f'enametime:{text3}'),Button.inline("زمان ایموجی اسم",
                    f'None')])
          text4.append([Button.inline("addenametime",
                    f'addenametime:{text3}'),Button.inline("افزودن زمان ایموجی اسم",
                    f'None')])
          text4.append([Button.inline("delenametime",
                    f'delenametime:{text3}'),Button.inline("حذف زمان ایموجی اسم",
                    f'None')])
          text4.append([Button.inline("cleanenametime",
                    f'cleanenametime:{text3}'),Button.inline("پاکسازی لیست زمان ایموجی اسم",
                    f'None')])
          text4.append([Button.inline("enametimelist",
                    f'enametimelist:0:{text3}'),Button.inline("لیست زمان ایموجی اسم",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("(premium)",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/124')])
          text4.append([Button.inline("بازگشت",
                    f'enamec:{text3}')])
          text4 = botp.build_reply_markup(text4)
      else:
        await edit_or_reply_message(message,"برای استفاده از این قابلیت پرمیوم نیاز است")
        return
    elif texthe == "cnamec":
      if databot33["getpremium"]:
        text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cname` <on|off> <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) رنگ اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}addcname` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن رنگ اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delcname` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف رنگ اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleancname` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست رنگ اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cnamelist` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست رنگ اسم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}stcname` <Premium><1-59>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم تایم رنگ اسم
➿〰️〰️〰️〰️〰️〰️〰️➿"""
        if boton["panelbot"]:
          text4.append([Button.inline("cname",
                    f'cname:{text3}'),Button.inline("رنگ اسم",
                    f'None')])
          text4.append([Button.inline("addcname",
                    f'addcname:{text3}'),Button.inline("افزودن رنگ اسم",
                    f'None')])
          text4.append([Button.inline("delcname",
                    f'delcname:{text3}'),Button.inline("حذف رنگ اسم",
                    f'None')])
          text4.append([Button.inline("cleancname",
                    f'cleancname:{text3}'),Button.inline("پاکسازی لیست رنگ اسم",
                    f'None')])
          text4.append([Button.inline("cnamelist",
                    f'cnamelist:0:{text3}'),Button.inline("لیست رنگ اسم",
                    f'None')])
          if chatid == int(databot33["me"]):
            text4.append([Button.inline("stcname",
                    f'send:stcname:{text3}'),Button.inline("تنظیم تایم رنگ اسم",
                    f'None')])
          else:
            text4.append([Button.url("stcname",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"stcname")),Button.inline("تنظیم تایم رنگ اسم",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("(premium)",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/124')])
          text4.append([Button.inline("بازگشت",
                    f'premiumhelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
      else:
        await edit_or_reply_message(message,"برای استفاده از این قابلیت پرمیوم نیاز است")
        return
    elif texthe == "eprofilec":
      if databot33["getpremium"]:
        text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}eprofile` <on|off> <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}addeprofile` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}deleprofile` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleaneprofile` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}eprofilelist` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}steprofile` <Premium><1-59>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم تایم ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}eprofiletimec` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) زمان ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿"""
        if boton["panelbot"]:
          text4.append([Button.inline("eprofile",
                    f'eprofile:{text3}'),Button.inline("ایموجی پروفایل",
                    f'None')])
          text4.append([Button.inline("addeprofile",
                    f'addeprofile:{text3}'),Button.inline("حذف ایموجی پروفایل",
                    f'None')])
          text4.append([Button.inline("deleprofile",
                    f'deleprofile:{text3}'),Button.inline("حذف رنگ اسم",
                    f'None')])
          text4.append([Button.inline("cleaneprofile",
                    f'cleaneprofile:{text3}'),Button.inline("پاکسازی لیست ایموجی پروفایل",
                    f'None')])
          text4.append([Button.inline("eprofilelist",
                    f'eprofilelist:0:{text3}'),Button.inline("لیست ایموجی پروفایل",
                    f'None')])
          if chatid == int(databot33["me"]):
            text4.append([Button.inline("steprofile",
                    f'send:steprofile:{text3}'),Button.inline("تنظیم تایم ایموجی پروفایل",
                    f'None')])
          else:
            text4.append([Button.url("steprofile",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"steprofile")),Button.inline("تنظیم تایم ایموجی پروفایل",
                    f'None')])
          text4.append([Button.inline("eprofiletimec",
                    f'eprofiletimec:{text3}'),Button.inline("زمان ایموجی پروفایل",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("(premium)",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/125')])
          text4.append([Button.inline("بازگشت",
                    f'premiumhelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
      else:
        await edit_or_reply_message(message,"برای استفاده از این قابلیت پرمیوم نیاز است")
        return
    elif texthe == "eprofiletimec":
      if databot33["getpremium"]:
        text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}eprofiletime` <on|off> <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) زمان ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}addeprofiletime` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن زمان ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}deleprofiletime` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف زمان ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleaneprofiletime` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست زمان ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}eprofiletimelist` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست زمان ایموجی پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿"""
        if boton["panelbot"]:
          text4.append([Button.inline("eprofiletime",
                    f'eprofiletime:{text3}'),Button.inline("زمان ایموجی پروفایل",
                    f'None')])
          text4.append([Button.inline("addeprofiletime",
                    f'addeprofiletime:{text3}'),Button.inline("حذف زمان ایموجی پروفایل",
                    f'None')])
          text4.append([Button.inline("deleprofiletime",
                    f'deleprofiletime:{text3}'),Button.inline("حذف زمان رنگ اسم",
                    f'None')])
          text4.append([Button.inline("cleaneprofiletime",
                    f'cleaneprofiletime:{text3}'),Button.inline("پاکسازی لیست زمان ایموجی پروفایل",
                    f'None')])
          text4.append([Button.inline("eprofiletimelist",
                    f'eprofiletimelist:0:{text3}'),Button.inline("لیست زمان ایموجی پروفایل",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("(premium)",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/168')])
          text4.append([Button.inline("بازگشت",
                    f'eprofilec:{text3}')])
          text4 = botp.build_reply_markup(text4)
      else:
        await edit_or_reply_message(message,"برای استفاده از این قابلیت پرمیوم نیاز است")
        return
    elif texthe == "cprofilec":
      if databot33["getpremium"]:
        text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cprofile` <on|off> <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) رنگ پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}addcprofile` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن رنگ پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delcprofile` <Premium> <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف رنگ پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleancprofile` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست رنگ پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cprofilelist` <Premium>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست رنگ پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}stcprofile` <Premium><1-59>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم تایم رنگ پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿"""
        if boton["panelbot"]:
          text4.append([Button.inline("cprofile",
                    f'cprofile:{text3}'),Button.inline("رنگ پروفایل",
                    f'None')])
          text4.append([Button.inline("addcprofile",
                    f'addcprofile:{text3}'),Button.inline("افزودن رنگ پروفایل",
                    f'None')])
          text4.append([Button.inline("delcprofile",
                    f'delcprofile:{text3}'),Button.inline("حذف رنگ پروفایل",
                    f'None')])
          text4.append([Button.inline("cleancprofile",
                    f'cleancprofile:{text3}'),Button.inline("پاکسازی لیست رنگ پروفایل",
                    f'None')])
          text4.append([Button.inline("cprofilelist",
                    f'cprofilelist:0:{text3}'),Button.inline("لیست رنگ پروفایل",
                    f'None')])
          if chatid == int(databot33["me"]):
            text4.append([Button.inline("stcprofile",
                    f'send:stcprofile:{text3}'),Button.inline("تنظیم تایم رنگ پروفایل",
                    f'None')])
          else:
            text4.append([Button.url("stcprofile",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"stcprofile")),Button.inline("تنظیم تایم رنگ پروفایل",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("(premium)",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/125')])
          text4.append([Button.inline("بازگشت",
                    f'premiumhelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
      else:
        await edit_or_reply_message(message,"برای استفاده از این قابلیت پرمیوم نیاز است")
        return
    elif texthe == "adminc":
      adminxzc=boton["databot"]["adminrun"]
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `add admin` <reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) اضافه کردن ادمین سلف
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) مثال: برای اجرا دستورات سلف
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) برای ادمین اول متن باید `{adminxzc}` بزارید
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{adminxzc}help`
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `remove admin` [reply/chat id]
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف کردن ادمین سلف
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `remove list admin`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف لیست ادمین سلف
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `list admin`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست ادمین سلف
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}setcadmin` <text>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم  دستور ران ادمین
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("add admin",
                    "https://t.me/amirwolfself/7"),Button.inline("اضافه کردن ادمین سلف",
                    'None')])
            text4.append([Button.url("remove admin",
                    "https://t.me/amirwolfself/8"),Button.inline("حذف کردن ادمین سلف",
                    'None')])
            text4.append([Button.url("setcadmin",
                    "https://t.me/amirwolfself/133"),Button.inline("تنظیم  دستور ران ادمین",
                    'None')])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("add admin",
                    f'send:add admin:{text3}'),Button.inline("اضافه کردن ادمین سلف",
                    f'None')])
              text4.append([Button.inline("remove admin",
                    f'send:remove admin:{text3}'),Button.inline("حذف کردن ادمین سلف",
                    f'None')])
              text4.append([Button.inline("remove list admin",
                    f'send:remove list admin:{text3}'),Button.inline("حذف لیست ادمین سلف",
                    f'None')])
            else:
              text4.append([Button.url("add admin",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"add admin")),Button.inline("اضافه کردن ادمین سلف",
                    f'None')])
              text4.append([Button.url("remove admin",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"remove admin")),Button.inline("حذف کردن ادمین سلف",
                    f'None')])
              text4.append([Button.url("remove list admin",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"remove list admin")),Button.inline("حذف لیست ادمین سلف",
                    f'None')])
            text4.append([Button.inline("list admin",
                    f'list admin:0:{text3}'),Button.inline("لیست ادمین سلف",
                    f'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("setcadmin",
                    f'send:setcadmin:{text3}'),Button.inline("تنظیم  دستور ران ادمین",
                    f'None')])
            else:
              text4.append([Button.url("setcadmin",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"setcadmin")),Button.inline("تنظیم  دستور ران ادمین",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng)",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'mnghelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "fontc":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}setfont` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) اضافه کردن فونت به ساعت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delfont` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف کردن فونت ساعت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}fontlist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست اسم فونت ساعت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleanfontlist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست فونت
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("setfont",
                    f'setfont:{text3}'),Button.inline("اضافه کردن فونت",
                    f'None')])
          text4.append([Button.inline("delfont",
                    f'delfont:{text3}'),Button.inline("حذف کردن فونت",
                    f'None')])
          text4.append([Button.inline("fontlist",
                    f'fontlist:0:{text3}'),Button.inline("لیست فونت",
                    f'None')])
          text4.append([Button.inline("cleanfontlist",
                    f'cleanfontlist:{text3}'),Button.inline("پاکسازی لیست فونت",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng)",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/11')])
          text4.append([Button.inline("بازگشت",
                    f'mnghelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "answerc":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}answer` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) متن و پاسخ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}setanswer` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم متن و پاسخ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delanswer`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف پاسخ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}answerlist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست پاسخ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleananswerlist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست پاسخ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exanswerc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثنا پاسخ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}answermode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم حالت پاسخ
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("answer",
                    f'answer:{text3}'),Button.inline("متن و پاسخ",
                    f'None')])
          text4.append([Button.inline("setanswer",
                    f'setanswer:{text3}'),Button.inline("تنظیم متن و پاسخ",
                    f'None')])
          if chatid == int(databot33["me"]):
            text4.append([Button.inline("delanswer",
                    f'send:delanswer:{text3}'),Button.inline("حذف پاسخ",
                    f'None')])
          else:
            text4.append([Button.url("delanswer",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"delanswer")),Button.inline("حذف پاسخ",
                    f'None')])
          text4.append([Button.inline("answerlist",
                    f'answerlist:0:{text3}'),Button.inline("لیست پاسخ",
                    f'None')])
          text4.append([Button.inline("cleananswerlist",
                    f'cleananswerlist:{text3}'),Button.inline("پاکسازی لیست پاسخ",
                    f'None')])
          text4.append([Button.inline("exanswerc",
                    f'exanswerc:{text3}'),Button.inline("استثنا پاسخ",
                    f'None')])
          if text=="he_"+texthe:
            text4.append([Button.url("answermode",
                    "https://t.me/amirwolfself/12"),Button.inline("پاکسازی لیست پاسخ",
                    'None')])
          else:
            text4.append([Button.inline("answermode",
                    f'answermode:{text3}'),Button.inline("تنظیم حالت پاسخ",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng)",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/12')])
          text4.append([Button.inline("بازگشت",
                    f'modehelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "reactc":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}react` <emoji> <reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ری اکشن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}chreact ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت ری اکشن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}setreact` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم ری اکشن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delreact` <username|id>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف ری اکشن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}reactlist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست ری اکشن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleanreactlist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست ری اکشن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exreactc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثنا ری اکشن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}reactmode` <pv|gp|all|ch>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم حالت ری اکشن
➿〰️〰️〰️〰️〰️〰️〰️➿
"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("react",
                    "https://t.me/amirwolfself/27"),Button.inline("ری اکشن",
                    'None')])
            text4.append([Button.url("chreact",
                    "https://t.me/amirwolfself/146"),Button.inline("حالت ری اکشن",
                    'None')])
            text4.append([Button.url("setreact",
                    "https://t.me/amirwolfself/146"),Button.inline("تنظیم ری اکشن",
                    'None')])
            text4.append([Button.url("delreact",
                    "https://t.me/amirwolfself/146"),Button.inline("حذف ری اکشن",
                    'None')])
            text4.append([Button.url("reactlist",
                    "https://t.me/amirwolfself/146"),Button.inline("لیست ری اکشن",
                    'None')])
            text4.append([Button.url("cleanreactlist",
                    "https://t.me/amirwolfself/146"),Button.inline("پاکسازی لیست ری اکشن",
                    'None')])
          else:
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("react",
                    f'send:react:{text3}'),Button.inline("ری اکشن",
                    f'None')])
            else:
              text4.append([Button.url("react",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"react")),Button.inline("ری اکشن",
                    f'None')])
            text4.append([Button.inline("chreact",
                    f'chreact:{text3}'),Button.inline("حالت ری اکشن",
                    f'None')])
            text4.append([Button.inline("setreact",
                    f'setreact:{text3}'),Button.inline("تنظیم ری اکشن",
                    f'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("delreact",
                    f'send:delreact:{text3}'),Button.inline("حذف ری اکشن",
                    f'None')])
            else:
              text4.append([Button.url("delreact",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"delanswer")),Button.inline("حذف ری اکشن",
                    f'None')])
            text4.append([Button.inline("reactlist",
                    f'reactlist:0:{text3}'),Button.inline("لیست ری اکشن",
                    f'None')])
            text4.append([Button.inline("cleanreactlist",
                    f'cleanreactlist:{text3}'),Button.inline("پاکسازی لیست ری اکشن",
                    f'None')])
          text4.append([Button.inline("exreactc",
                    f'exreactc:{text3}'),Button.inline("استثنا ری اکشن",
                    f'None')])
          if text=="he_"+texthe:
            text4.append([Button.url("reactmode",
                    "https://t.me/amirwolfself/146"),Button.inline("تنظیم حالت ری اکشن",
                    'None')])
          else:
            text4.append([Button.inline("reactmode",
                    f'reactmode:{text3}'),Button.inline("تنظیم حالت ری اکشن",
                    f'None')])
                    
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng)",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'mnghelp:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "gamec":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}add game` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) اضافه کردن گیم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}sleep game` [0-5] [name game]
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) زمان صبر گیم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}remove game` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف گیم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}remove list game`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف لیست گیم
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}list game`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست گیم"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("add game",
                    "https://t.me/amirwolfself/161"),Button.inline("اضافه کردن گیم",
                    'None')])
            text4.append([Button.url("sleep game",
                    "https://t.me/amirwolfself/15"),Button.inline("زمان صبر گیم",
                    'None')])
            text4.append([Button.url("remove game",
                    "https://t.me/amirwolfself/16"),Button.inline("حذف گیم",
                    'None')])
          else:
            text4.append([Button.inline("add game",
                    f'add game:{text3}'),Button.inline("اضافه کردن گیم",
                    f'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("sleep game",
                    f'send:sleep game:{text3}'),Button.inline("زمان صبر گیم",
                    f'None')])
            else:
              text4.append([Button.url("sleep game",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"sleep game")),Button.inline("زمان صبر گیم",
                    f'None')])
            text4.append([Button.inline("remove game",
                    f'remove game:{text3}'),Button.inline("حذف گیم",
                    f'None')])
            text4.append([Button.inline("remove list game",
                    f'remove list game:{text3}'),Button.inline("حذف لیست گیم",
                    f'None')])
            text4.append([Button.inline("list game",
                    f'list game:0:{text3}'),Button.inline("لیست گیم",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng2)",
                    f'mnghelp2:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'mnghelp2:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "markreadc":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}markread ` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حالت سین
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exmarkreadc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثنا سین
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}markreadmode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم حالت سین
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("markread",
                    f'markread:{text3}'),Button.inline("حالت سین",
                    f'None')])
          text4.append([Button.inline("exmarkreadc",
                    f'exmarkreadc:{text3}'),Button.inline("استثنا سین",
                    f'None')])
          text4.append([Button.inline("markreadmode",
                    f'markreadmode:{text3}'),Button.inline("تنظیم حالت سین",
                    f'None')])
                    
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("(mode2)",
                    f'modehelp2:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/41')])
          text4.append([Button.inline("بازگشت",
                    f'modehelp2:{text3}')])
          text4 = botp.build_reply_markup(text4)

    elif texthe == "musicc":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}chmusic` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) موزیک
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}video to voice`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ویدیو به موزیک
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}getmusic` <chat_id|id|username|reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) دریافت موزیک پروفایل
➿〰️〰️〰️〰️〰️〰️〰️➿

[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}stmusic` <1-59>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم تایم موزیک
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("chmusic",
                    "https://t.me/amirwolfself/165"),Button.inline("موزیک",
                    'None')])
            text4.append([Button.url("video to voice",
                    "https://t.me/amirwolfself/160"),Button.inline("ویدیو به موزیک",
                    'None')])
            text4.append([Button.url("getmusic",
                    "https://t.me/amirwolfself/169"),Button.inline("دریافت موزیک پروفایل",
                    'None')])
            text4.append([Button.url("stmusic",
                    "https://t.me/amirwolfself/165"),Button.inline("تنظیم تایم موزیک",
                    'None')])
          else:
            text4.append([Button.inline("chmusic",
                    f'chmusic:{text3}'),Button.inline("موزیک",
                    f'None')])
            if chatid == int(databot33["me"]):
              text4.append([Button.inline("video to voice",
                    f'send:video to voice:{text3}'),Button.inline("ویدیو به موزیک",
                    f'None')])
              text4.append([Button.inline("getmusic",
                    f'send:getmusic:{text3}'),Button.inline("دریافت موزیک پروفایل",
                    f'None')])
              text4.append([Button.inline("stmusic",
                    f'send:stmusic:{text3}'),Button.inline("تنظیم تایم موزیک",
                    f'None')])
            else:
              text4.append([Button.url("video to voice",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"video to voice")),Button.inline("ویدیو به موزیک",
                    f'None')])
              text4.append([Button.url("getmusic",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"getmusic")),Button.inline("دریافت موزیک پروفایل",
                    f'None')])
              text4.append([Button.url("stmusic",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"stmusic")),Button.inline("تنظیم تایم موزیک",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("(mode)",
                    f'modehelp3:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'modehelp3:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "actionc":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}actyping` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تایپ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}accontact` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) انتخاب مخاطب
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}acgame` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بازی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}aclocation` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) انتخاب لوکشین
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}acsticker` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) انتخاب استیکر
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}acrecord-voice` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ضبط صوتی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}acrecord-round` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ضبط ویدیوی گرد
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}acrecord-video` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ضبط ویدیو
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}acvoice` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ارسال صوت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}acround` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) آپلود ویدیوی گرد
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}acvideo` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) آپلود ویدیو
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}acphoto` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) آپلود عکس
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}acfile` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) آپلود فایل
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}actionmodec`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم حالت اکشن ها
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exactionc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثنا اکشن ها
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("actyping",
                    f'actyping:{text3}'),Button.inline("تایپ",
                    f'None')])
          text4.append([Button.inline("accontact",
                    f'accontact:{text3}'),Button.inline("انتخاب مخاطب",
                    f'None')])
          text4.append([Button.inline("acgame",
                    f'acgame:{text3}'),Button.inline("بازی",
                    f'None')])
          text4.append([Button.inline("aclocation",
                    f'aclocation:{text3}'),Button.inline("انتخاب لوکشین",
                    f'None')])
          text4.append([Button.inline("acsticker",
                    f'acsticker:{text3}'),Button.inline("انتخاب استیکر",
                    f'None')])
          text4.append([Button.inline("acrecord-voice",
                    f'acrecord-voice:{text3}'),Button.inline("ضبط صوتی",
                    f'None')])
          text4.append([Button.inline("acrecord-round",
                    f'acrecord-round:{text3}'),Button.inline("ضبط ویدیوی گرد‌",
                    f'None')])
          text4.append([Button.inline("acrecord-video",
                    f'acrecord-video:{text3}'),Button.inline("ضبط ویدیو",
                    f'None')])
          text4.append([Button.inline("acvoice",
                    f'acvoice:{text3}'),Button.inline("ارسال صوت",
                    f'None')])
          text4.append([Button.inline("acround",
                    f'acround:{text3}'),Button.inline("آپلود ویدیوی گرد",
                    f'None')])
          text4.append([Button.inline("acvideo",
                    f'acvideo:{text3}'),Button.inline("آپلود ویدیو",
                    f'None')])
          text4.append([Button.inline("acphoto",
                    f'acphoto:{text3}'),Button.inline("آپلود عکس",
                    f'None')])
          text4.append([Button.inline("acfile",
                    f'acfile:{text3}'),Button.inline("آپلود فایل",
                    f'None')])
          text4.append([Button.inline("actionmodec",
                    f'actionmodec:{text3}'),Button.inline("تنظیم حالت اکشن ها",
                    f'None')])
          text4.append([Button.inline("exactionc",
                    f'exactionc:{text3}'),Button.inline("استثنا اکشن ها",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("(mode)",
                    f'modehelp3:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/999')])
          text4.append([Button.inline("بازگشت",
                    f'modehelp3:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "exactionc":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}extypingc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثنا تایپ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}excontactc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثناانتخاب مخاطب
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exgamec`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثنا بازی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exlocationc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثناانتخاب لوکشین
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exstickerc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثناانتخاب استیکر
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exrecord-voicec`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثناضبط صوتی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exrecord-roundc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثناضبط ویدیوی گرد
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exrecord-videoc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثناضبط ویدیو
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exvoicec`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثناارسال صوت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exroundc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثناآپلود ویدیوی گرد
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exvideoc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثناآپلود ویدیو
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exphotoc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثناآپلود عکس
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}exfilec`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثناآپلود فایل
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("extypingc",
                    f'extypingc:{text3}'),Button.inline("استثنا تایپ",
                    f'None')])
          text4.append([Button.inline("excontactc",
                    f'excontactc:{text3}'),Button.inline("استثناانتخاب مخاطب",
                    f'None')])
          text4.append([Button.inline("exgamec",
                    f'exgamec:{text3}'),Button.inline("استثنابازی",
                    f'None')])
          text4.append([Button.inline("exlocationc",
                    f'exlocationc:{text3}'),Button.inline("استثناانتخاب لوکیشن",
                    f'None')])
          text4.append([Button.inline("exstickerc",
                    f'exstickerc:{text3}'),Button.inline("استثناانتخاب استیکر",
                    f'None')])
          text4.append([Button.inline("exrecord-voicec",
                    f'exrecord-voicec:{text3}'),Button.inline("استثناضبط صوتی",
                    f'None')])
          text4.append([Button.inline("exrecord-roundc",
                    f'exrecord-roundc:{text3}'),Button.inline("استثناضبط ویدیوی گرد‌",
                    f'None')])
          text4.append([Button.inline("exrecord-videoc",
                    f'exrecord-videoc:{text3}'),Button.inline("استثناضبط ویدیو",
                    f'None')])
          text4.append([Button.inline("exvoicec",
                    f'exvoicec:{text3}'),Button.inline("استثناارسال صوت",
                    f'None')])
          text4.append([Button.inline("exroundc",
                    f'exroundc:{text3}'),Button.inline("استثناآپلود ویدیوی گرد",
                    f'None')])
          text4.append([Button.inline("exvideoc",
                    f'exvideoc:{text3}'),Button.inline("استثناآپلود ویدیو",
                    f'None')])
          text4.append([Button.inline("exphotoc",
                    f'exphotoc:{text3}'),Button.inline("استثناآپلود عکس",
                    f'None')])
          text4.append([Button.inline("exfilec",
                    f'exfilec:{text3}'),Button.inline("استثناآپلود فایل",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("(mode)",
                    f'modehelp3:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.inline("بازگشت",
                    f'actionc:{text3}')])
          text4 = botp.build_reply_markup(text4)

    elif texthe == "actionmodec":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}typingmode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تایپ
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}contactmode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) انتخاب مخاطب
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}gamemode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بازی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}locationmode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) انتخاب لوکیشن 
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}stickermode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) انتخاب استیکر
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}record-voicemode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ضبط صوتی
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}record-roundmode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ضبط ویدیوی گرد
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}record-videomode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ضبط ویدیو
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}voicemode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) ارسال صوت
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}roundmode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) آپلود ویدیوی گرد
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}videomode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) آپلود ویدیو
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}photomode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) آپلود عکس
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}filemode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) آپلود فایل
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("typingmode",
                    f'typingmode:{text3}'),Button.inline("تایپ",
                    f'None')])
          text4.append([Button.inline("contactmode",
                    f'contactmode:{text3}'),Button.inline("انتخاب مخاطب",
                    f'None')])
          text4.append([Button.inline("gamemode",
                    f'gamemode:{text3}'),Button.inline("بازی",
                    f'None')])
          text4.append([Button.inline("locationmode",
                    f'locationmode:{text3}'),Button.inline("انتخاب لوکشین",
                    f'None')])
          text4.append([Button.inline("stickermode",
                    f'stickermode:{text3}'),Button.inline("انتخاب استیکر",
                    f'None')])
          text4.append([Button.inline("record-voicemode",
                    f'record-voicemode:{text3}'),Button.inline("ضبط صوتی",
                    f'None')])
          text4.append([Button.inline("record-roundmode",
                    f'record-roundmode:{text3}'),Button.inline("ضبط ویدیوی گرد‌",
                    f'None')])
          text4.append([Button.inline("record-videomode",
                    f'record-videomode:{text3}'),Button.inline("ضبط ویدیو",
                    f'None')])
          text4.append([Button.inline("voicemode",
                    f'voicemode:{text3}'),Button.inline("ارسال صوت",
                    f'None')])
          text4.append([Button.inline("roundmode",
                    f'roundmode:{text3}'),Button.inline("آپلود ویدیوی گرد",
                    f'None')])
          text4.append([Button.inline("videomode",
                    f'videomode:{text3}'),Button.inline("آپلود ویدیو",
                    f'None')])
          text4.append([Button.inline("photomode",
                    f'photomode:{text3}'),Button.inline("آپلود عکس",
                    f'None')])
          text4.append([Button.inline("filemode",
                    f'filemode:{text3}'),Button.inline("آپلود فایل",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("(mode)",
                    f'modehelp3:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.inline("بازگشت",
                    f'actionc:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "commentc":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}comment` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) کامنت اول
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}setcomment` [ch]
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم متن کامنت اول
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}excommentc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثنا کامنت اول
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("comment",
                    f'comment:{text3}'),Button.inline("کامنت اول",
                    f'None')])
          if chatid == int(databot33["me"]):
            text4.append([Button.inline("setcomment",
                    f'send:setcomment:{text3}'),Button.inline("تنظیم متن کامنت اول",
                    f'None')])
          else:
            text4.append([Button.url("setcomment",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"setcomment")),Button.inline("تنظیم متن کامنت اول",
                    f'None')])
          text4.append([Button.inline("excommentc",
                    f'excommentc:{text3}'),Button.inline("استثنا کامنت اول",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng2)",
                    f'mnghelp2:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/136')])
          text4.append([Button.inline("بازگشت",
                    f'mnghelp2:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe in ["excommentc","exmarkreadc","exreactc","exanswerc","extypingc","excontactc","exgamec","exlocationc","exstickerc","exrecord-voicec","exrecord-roundc","exrecord-videoc","exvoicec","exroundc","exvideoc","exphotoc","exfilec"]:
      textzlist={
      "excommentc":"کامنت اول","exmarkreadc":"سین","exreactc":"ری اکشن",
      "exanswerc":"پاسخ","extypingc":"تایپ","excontactc":"مخاطب","exgamec":"بازی",
      "exlocationc":"لوکشین","exstickerc":"استیکر","exrecord-roundc":"ضبط ویدیوی گرد",
      "exrecord-videoc":"ضبط ویدیو","exvoicec":"ارسال صوت","exroundc":"آپلود ویدیوی گرد",
      "exvideoc":"آپلود ویدیو","exphotoc":"آپلود عکس","exfilec":"آپلود فایل"}
      
      textlz=textzlist[texthe]
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}set{texthe[:-1]}` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) استثنا {textlz}
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}del{texthe[:-1]}`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف استثنا {textlz}
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}{texthe[:-1]}list`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست استثنا {textlz}
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}clean{texthe[:-1]}`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی استثنا {textlz}
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}{texthe[:-1]}` (allow|never)
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم استثنا {textlz}
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("set"+texthe[:-1],
                    f'set{texthe[:-1]}:{text3}'),Button.inline("استثنا "+textlz,
                    f'None')])
          text4.append([Button.inline("del"+texthe[:-1],
                    f'del{texthe[:-1]}:{text3}'),Button.inline("حذف استثنا "+textlz,
                    f'None')])
          text4.append([Button.inline(texthe[:-1]+"list",
                    texthe[:-1]+f'list:0:{text3}'),Button.inline("لیست استثنا "+textlz,
                    f'None')])
          text4.append([Button.inline("clean"+texthe[:-1],
                    f'clean{texthe[:-1]}:{text3}'),Button.inline("پاکسازی استثنا "+textlz,
                    f'None')])
          text4.append([Button.inline(texthe[:-1],
                    texthe[:-1]+f':{text3}'),Button.inline("تنظیم استثنا "+textlz,
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("mng",
                    f'mnghelp:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if texthe in ["extypingc","excontactc","exgamec","exlocationc","exstickerc","exrecord-voicec","exrecord-roundc","exrecord-videoc","exvoicec","exroundc","exvideoc","exphotoc","exfilec"]:
            text4.append([Button.inline("بازگشت",
                    f'exactionc:{text3}')])
          else:
            text4.append([Button.inline("بازگشت",
                    texthe[2:]+f':{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "enemyc":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}enemy` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]})  دشمن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}setenemy` <UserName><in pv><reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن کاربر به لیست دشمن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delenemy` <UserName><in pv><reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف کاربر از لیست دشمن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleanenemylist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست دشمن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}enemylist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست دشمن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}enemymode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم حالت دشمن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}foshc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش متن دشمن
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("enemy",
                    f'enemy:{text3}'),Button.inline("دشمن",
                    f'None')])
          if chatid == int(databot33["me"]):
            text4.append([Button.inline("setenemy",
                    f'send:setenemy:{text3}'),Button.inline("افزودن کاربر به لیست دشمن",
                    f'None')])
            text4.append([Button.inline("delenemy",
                    f'send:delenemy:{text3}'),Button.inline("حذف کاربر از لیست دشمن",
                    f'None')])
          else:
            text4.append([Button.url("setenemy",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"setenemy")),Button.inline("افزودن کاربر به لیست دشمن",
                    f'None')])
            text4.append([Button.url("delenemy",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"delenemy")),Button.inline("حذف کاربر از لیست دشمن",
                    f'None')])
          text4.append([Button.inline("cleanenemylist",
                    f'cleanenemylist:{text3}'),Button.inline("پاکسازی لیست دشمن",
                    f'None')])
          text4.append([Button.inline("enemylist",
                    f'enemylist:0:{text3}'),Button.inline("لیست دشمن",
                    f'None')])
          text4.append([Button.inline("enemymode",
                    f'enemymode:{text3}'),Button.inline("تنظیم حالت دشمن",
                    f'None')])
          text4.append([Button.inline("foshc",
                    f'foshc:{text3}'),Button.inline("بخش متن دشمن",
                    'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng3)",
                    f'mnghelp3:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/87')])
          text4.append([Button.inline("بازگشت",
                    f'mnghelp3:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "foshc":
      text2=f"""
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}addfosh` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن متن دلخواه به دشمن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delfosh` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف متن دلخواه از دشمن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleanfoshlist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست متن دشمن
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}foshlist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست متن دشمن"""
      if boton["panelbot"]:
          if text=="he_"+texthe:
            text4.append([Button.url("addfosh",
                    "https://t.me/amirwolfself/90"),Button.inline("افزودن متن دلخواه به دشمن",
                    'None')])
            text4.append([Button.url("delfosh",
                    "https://t.me/amirwolfself/91"),Button.inline("حذف متن دلخواه از دشمن",
                    'None')])
            text4.append([Button.url("cleanfoshlist",
                    "https://t.me/amirwolfself/91"),Button.inline("حذف متن دلخواه از دشمن",
                    'None')])
            text4.append([Button.url("foshlist",
                    "https://t.me/amirwolfself/91"),Button.inline("لیست متن دشمن",
                    'None')])
          else:
            text4.append([Button.inline("addfosh",
                    f'addfosh:{text3}'),Button.inline("افزودن متن دلخواه به دشمن",
                    f'None')])
            text4.append([Button.inline("delfosh",
                    f'delfosh:{text3}'),Button.inline("حذف متن دلخواه از دشمن",
                    f'None')])
            text4.append([Button.inline("cleanfoshlist",
                    f'cleanfoshlist:{text3}'),Button.inline("حذف متن دلخواه از دشمن",
                    f'None')])
            text4.append([Button.inline("foshlist",
                    f'foshlist:0:{text3}'),Button.inline("لیست متن دشمن",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng)",
                    f'enemyc:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          if text=="he_"+texthe:
            text4.append([Button.inline("بازگشت",
                    f'{texthe}:{text3}')])
          else:
            text4.append([Button.inline("اموزش",
                    f'he_{texthe}:{text3}')])
            text4.append([Button.inline("بازگشت",
                    f'enemyc:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "lovec":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}love` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]})  عشق
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}setlove` <UserName><in pv><reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن کاربر به لیست عشق
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}dellove` <UserName><in pv><reply>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف کاربر از لیست عشق
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleanlovelist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست عشق
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}lovelist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست عشق
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}lovemode` <pv|gp|all>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) تنظیم حالت عشق
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}lovetxtc`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) بخش متن عشق
➿〰️〰️〰️〰️〰️〰️〰️➿"""
      if boton["panelbot"]:
          text4.append([Button.inline("love",
                    f'love:{text3}'),Button.inline("عشق",
                    f'None')])
          if chatid == int(databot33["me"]):
            text4.append([Button.inline("setlove",
                    f'send:setlove:{text3}'),Button.inline("افزودن کاربر به لیست عشق",
                    f'None')])
            text4.append([Button.inline("dellove",
                    f'send:dellove:{text3}'),Button.inline("حذف کاربر از لیست عشق",
                    f'None')])
          else:
            text4.append([Button.url("setlove",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"setlove")),Button.inline("افزودن کاربر به لیست عشق",
                    f'None')])
            text4.append([Button.url("dellove",
                    "https://t.me/share/url?url="+requests.utils.quote(textlen+"dellove")),Button.inline("حذف کاربر از لیست عشق",
                    f'None')])
          text4.append([Button.inline("cleanlovelist",
                    f'cleanlovelist:{text3}'),Button.inline("پاکسازی لیست عشق",
                    f'None')])
          text4.append([Button.inline("lovelist",
                    f'lovelist:0:{text3}'),Button.inline("لیست عشق",
                    f'None')])
          text4.append([Button.inline("lovemode",
                    f'lovemode:{text3}'),Button.inline("تنظیم حالت عشق",
                    f'None')])
          text4.append([Button.inline("lovetxtc",
                    f'lovetxtc:{text3}'),Button.inline("بخش متن عشق",
                    'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng3)",
                    f'mnghelp3:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/154')])
          text4.append([Button.inline("بازگشت",
                    f'lovec:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "lovetxtc":
      text2=f"""
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}setlovetxt` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن متن دلخواه به عشق
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}dellovetxt` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف متن دلخواه از عشق
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleanlovetxtlist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی لیست متن عشق
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}lovetxtlist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست متن عشق"""
      if boton["panelbot"]:
          text4.append([Button.inline("setlovetxt",
                    f'setlovetxt:{text3}'),Button.inline("افزودن متن دلخواه به عشق",
                    f'None')])
          text4.append([Button.inline("dellovetxt",
                    f'dellovetxt:{text3}'),Button.inline("حذف متن دلخواه از عشق",
                    f'None')])
          text4.append([Button.inline("cleanlovetxtlist",
                    f'cleanlovetxtlist:{text3}'),Button.inline("حذف متن دلخواه از عشق",
                    f'None')])
          text4.append([Button.inline("lovetxtlist",
                    f'lovetxtlist:0:{text3}'),Button.inline("لیست متن عشق",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng)",
                    f'lovec:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'status:0:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/155')])
          text4.append([Button.inline("بازگشت",
                    f'lovec:{text3}')])
          text4 = botp.build_reply_markup(text4)
    elif texthe == "cmdc":
      text2=f"""
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cmd` <on|off>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) قفل کامند
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}addcmd` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) افزودن قفل کامند
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}delcmd` <ask>
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) حذف قفل کامند
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cleancmd`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) پاکسازی قفل کامند
➿〰️〰️〰️〰️〰️〰️〰️➿
[▶️](emoji/{databot33['beta']['▶️'][databot33['beta']['data']]}) `{textlen}cmdlist`
[◀️](emoji/{databot33['beta']['◀️'][databot33['beta']['data']]}) لیست قفل کامند"""
      if boton["panelbot"]:

          text4.append([Button.inline("cmd",
                    f'cmd:{text3}'),Button.inline("قفل کامند",
                    f'None')])
          text4.append([Button.inline("addcmd",
                    f'addcmd:{text3}'),Button.inline("افزودن قفل کامند",
                    f'None')])
          text4.append([Button.inline("delcmd",
                    f'delcmd:{text3}'),Button.inline("حذف قفل کامند",
                    f'None')])
          text4.append([Button.inline("cleancmd",
                    f'cleancmd:{text3}'),Button.inline("پاکسازی قفل کامند",
                    f'None')])
          text4.append([Button.inline("cmdlist",
                    f'cmdlist:0:{text3}'),Button.inline("لیست قفل کامند",
                    f'None')])
          text4.append([Button.inline("〰️〰️|help|〰️〰️",
                    'None')])
          cd=[]
          cd.append(Button.inline("Help",
                    f'help:{text3}'))
          if databot33["getpremium"]:
            cd.append(Button.inline("premium",
                    f'premiumhelp:{text3}'))
          cd.append(Button.inline("(mng3)",
                    f'mnghelp3:{text3}'))
          cd.append(Button.inline("mode",
                    f'modehelp:{text3}'))
          cd.append(Button.inline("info",
                    f'infohelp:{text3}'))
          text4.append(cd)
          text4.append([Button.inline("clerk",
                    f'clerkhelp:{text3}'),Button.inline("tool",
                    f'toolhelp:{text3}'),Button.inline("group",
                    f'gphelp:{text3}'),Button.inline("fun",
                    f'funhelp:{text3}')])
          text4.append([Button.inline("〰️〰️〰️〰️〰️〰️",
                    f'None')])
          text4.append([Button.inline("وضعیت",
                    f'وضعیت:{text3}')])
          text4.append([Button.inline("ریستارت",
                    f'ریستارت:{text3}')])
          text4.append([Button.url("اموزش",
                    'https://t.me/amirwolfself/126')])
          text4.append([Button.inline("بازگشت",
                    f'mnghelp3:{text3}')])
          text4 = botp.build_reply_markup(text4)
    ddad2=time2.split(",")
    pytz2=pytz.timezone(boton["databot"]["timezone"])
    date23=datetime.now(pytz2)
    date24=datetime.now(timezone.utc)
    las2t = pytz2.localize(datetime(int(ddad2[0]),int(ddad2[1]),int(ddad2[2]),int(ddad2[3]),int(ddad2[4])))
    
    timednow=int((date23 - las2t).total_seconds())
    d, h, m, s_ = timednow//86400, timednow%86400//3600, timednow%3600//60, timednow%60
    if d == 0:
      timednow=f"[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]}){h:02d}:{m:02d}:{s_:02d}[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})"
    else:
      timednow=f"{d} days {h:02d}:{m:02d}:{s_:02d}"
    dasdcc2=""
    version=databot33["version"]
    if databot33["getpremium"] and not databot33["beta"]["data"]:
      las2t = pytz2.localize(datetime(int(databot33["getpremium"][2]),int(databot33["getpremium"][1]),int(databot33["getpremium"][0])))
    
      timednowp=(las2t - date24)
      if timednowp.days >-1:
        dasdcc2=f"""[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️Premium[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})
[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]}){str(timednowp).split(".")[0]}[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})
"""
    timenowrun=f"""[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️Time Up[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})
[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]}){str(timednow).split(".")[0]}[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})
"""

    textzb=f"""{text2}
{dasdcc2}{timenowrun}[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️Bot[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})
[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]}){axdv}{boton['usernamebot'][0]}[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})
[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️PV[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})
[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['owner'][databot33['beta']['data']]}){axdv}amir_wolf512[➿](emoji/{databot33['beta']['owner'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})
[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})Setserver[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})
[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]}){selfrun3}/4[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})
[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️version[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[〰️](emoji/{databot33['beta']['〰️'][databot33['beta']['data']]})️[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})
[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]}){version}[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})[➿](emoji/{databot33['beta']['➿'][databot33['beta']['data']]})"""
    if texthe =="stop":
      textzb="""پنل بسته شد!"""
    await edit_or_reply_message(message,textzb,button=text4)
    raise events.StopPropagation
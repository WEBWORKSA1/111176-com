"""Generates logo/OG PNGs. Requires Pillow + Noto CJK fonts (apt install fonts-noto-cjk)."""
import glob, os
from PIL import Image, ImageDraw, ImageFont
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fonts = glob.glob("/usr/share/fonts/**/NotoSerifCJK-Bold.ttc", recursive=True) + glob.glob("/usr/share/fonts/**/NotoSansCJK-Bold.ttc", recursive=True)
serif = fonts[0]; sans = fonts[-1]
F = lambda p, s: ImageFont.truetype(p, s, index=0)
os.makedirs(f"{R}/assets/img", exist_ok=True)
im = Image.new("RGB", (512, 512), "#c8102e"); d = ImageDraw.Draw(im)
d.rectangle([0, 470, 512, 512], fill="#d4a017"); d.text((256, 240), "吉", font=F(serif, 300), fill="white", anchor="mm")
im.save(f"{R}/assets/img/logo.png"); im.resize((192, 192)).save(f"{R}/assets/img/icon-192.png")
og = Image.new("RGB", (1200, 630), "#15120f"); d = ImageDraw.Draw(og)
d.rectangle([0, 0, 1200, 12], fill="#c8102e"); d.rectangle([0, 618, 1200, 630], fill="#d4a017")
d.text((1080, 520), "福", font=F(serif, 420), fill="#2a1a14", anchor="mm")
d.text((80, 170), "111176", font=F(sans, 170), fill="#d4a017", anchor="lm")
d.text((84, 300), "Chinese Number Decoder", font=F(sans, 64), fill="white", anchor="lm")
d.text((84, 390), "Meanings · Lucky numbers · Lucky dates · Tools", font=F(sans, 38), fill="#d9d3c7", anchor="lm")
d.text((84, 470), "8 发 prosper   6 溜 smooth   9 久 lasting   4 死 avoid", font=F(sans, 34), fill="#f1b6bf", anchor="lm")
og.save(f"{R}/assets/img/og.png")
print("images ok")

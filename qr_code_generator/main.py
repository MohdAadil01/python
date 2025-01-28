import qrcode
from PIL import Image, ImageDraw, ImageFont
RESUME_LINK = "https://drive.google.com/file/d/1on0dkqxMuRDpky0H924NKQHaOJrQi6eZ/view"
CONTENT = "MOHD AADIL"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data(RESUME_LINK)
qr.make(fit=True)


fill_color = "cyan"
back_color = "white"
img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype("arial.ttf", 40)
except IOError:
    font = ImageFont.load_default()

img_width, img_height = img.size

text_width, text_height = draw.textbbox((0, 0),CONTENT, font=font)[2:]
text_x = (img_width - text_width) // 2
text_y = (img_height - text_height) // 2

draw.text((text_x, text_y), CONTENT, fill="black", font=font)

img.save("Resume.png")

print("QR code generated and saved as 'Resume.png'")
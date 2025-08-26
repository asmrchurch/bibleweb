import qrcode
import sys

# YouTube channel URL
url = "https://www.youtube.com/@asmrchurch"

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save("youtube_channel_qr.png")
print("QR code saved as youtube_channel_qr.png")
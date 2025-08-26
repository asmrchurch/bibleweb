import urllib.request
import urllib.parse

# YouTube channel URL
url = "https://www.youtube.com/@asmrchurch"

# Generate QR code using qr-server.com API
qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={urllib.parse.quote(url)}"

# Download the QR code
urllib.request.urlretrieve(qr_api_url, "youtube_channel_qr.png")
print("QR code saved as youtube_channel_qr.png")
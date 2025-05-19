import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(' ')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qrcode.png")  # Save the image to a file

print("QR code saved to my_qrcode.png")

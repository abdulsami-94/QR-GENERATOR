import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.google.com/imgres?q=funny%20monkey%20images&imgurl=https%3A%2F%2Fi.pinimg.com%2F564x%2F28%2F26%2F3c%2F28263ce44d75dd1938c1a25329f14a9f.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F19914423341748800%2F&docid=tK3TCtHqGtGtnM&tbnid=pEj07P_cozwNRM&vet=12ahUKEwigwvm22ImLAxUHsVYBHdvyB98QM3oECBoQAA..i&w=534&h=800&hcb=2&ved=2ahUKEwigwvm22ImLAxUHsVYBHdvyB98QM3oECBoQAA')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qrcode.png")  # Save the image to a file

print("QR code saved to my_qrcode.png")

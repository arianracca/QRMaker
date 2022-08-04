import pyqrcode
import png
url = input("Hola, ingrese la web de la que desea generar un código QR de ingreso en formato https://nombre.xx ")

qr_code = pyqrcode.create(url)
qr_code.png("QRURL.png",scale=5)
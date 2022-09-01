# QRcodeWebPages.py - A simple but flexible QR code maker
# Used pyqrcode, png, os
import pyqrcode
import png
import os

http = "https://www."
url_name = input("""Hola, ingrese la web de la que desea
generar un código QR.
formato: nombre.xx (sin https://www.
""")
url_link = http+url_name
url_title = input("Elija el nombre del archivo a guardar\n")
folder = input("Ingrese la ruta de acceso a la carpeta de guardado\n")
qr_img = pyqrcode.create(url_link)
#qr_img.png("./"+url_name+".png",scale=10)
qr_img.png(os.path.join(folder, url_title+".png"),scale=10)
print("Se generó el código QR de la web "+url_name)
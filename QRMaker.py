# QRcodeWebPages.py - Flexible QR code maker.
# Used pyqrcode, png, os libraries

__version__ = "1.0"

import pyqrcode
import png
import os

if __name__ == '__main__':

    http = "https://www." #Make the url easier to type,
    url_name = input("""Hola, ingrese la web para
generar un código QR.
formato: nombre.xx (sin https://www.
""")

    url_link = http+url_name #Compose the full url with https://www. and the input.
    url_title = input("Elija el nombre del archivo a guardar\n")
    px = int(input("Elija la medida de la imagen del QR\n(Referencia: 10 = 370x370px\n"))
    #Set the dimensions of the image file
    folder = input("Ingrese la ruta de acceso a la carpeta de guardado\n")
    qr_img = pyqrcode.create(url_link) #Make the QR code

    format = input("Elija el formato de exportación: 1.SVG 2.PNG")
    if format == "1": #Save svg file
        print("Seleccionado: SVG")
        qr_img.svg(os.path.join(folder, url_title+".svg"),scale=px)
    else: #Save png file
        print("Seleccionado: PNG")
        qr_img.png(os.path.join(folder, url_title+".png"),scale=px)

print("Se generó el código QR de la web "+url_name)
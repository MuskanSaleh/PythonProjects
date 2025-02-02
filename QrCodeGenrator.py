#Customize way or basic properties ko kese chng kr k we  made of qr code generator
import qrcode 
#used for formatting of qr code
from PIL import Image
import qrcode.constants
#For chnging functionalities and error ko cancel
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4)
qr.add_data("https://www.linkedin.com/in/muskan-saleh-731b59231/")
qr.make(fit = True)
img = qr.make_image(fill_color = 'white',back_color = 'black')
img.save("My_linkedIn.png")

#Simple way to generate  qr code
#import qrcode as qr
#helps to make qr code
# qr.make("https://www.linkedin.com/in/muskan-saleh-731b59231/")
#saves qr code in png format
# img.save("Mylinkedin.png")
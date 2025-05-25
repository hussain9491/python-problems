import qrcode 

data = "https://e-commerce03.vercel.app/"
qr = qrcode.make(data)
qr.save("qrcode.png")
print("QR code saved successfully")


#pip install qrcode[pil]  #install this package 
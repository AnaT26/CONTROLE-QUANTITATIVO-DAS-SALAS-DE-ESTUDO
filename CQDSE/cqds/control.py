import qrcode
quantidade = 50
img = qrcode.make(quantidade)
img.save("sala304.jpg")
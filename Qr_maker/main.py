import qrcode



url=input("Enter your Url: ").strip()
ad=r"C:\Users\Sneha\OneDrive\Documents\AMAN_DEVELOPER\Python.projects\Qr_maker\qrcode.png"

qr=qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(ad)
print("Done✅🙂")



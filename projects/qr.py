import qrcode 

data = input("Enter the text or url: ").strip()
filename = input("Enter file name : ").strip()# to remove blank space if provided
qr = qrcode.QRCode(box_size = 10 , border = 4 )
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color = 'black' , back_color = 'white')
image.save(filename)
print(f'qr code saved as {filename}')

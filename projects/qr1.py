import qrcode

# Take input from user
data = input("Enter text or URL for QR Code: ")
filename = input("Enter file name (with .png): ")

# Generate QR code
img = qrcode.make(data)

# Save the QR code
img.save(filename)

print("QR Code generated and saved as", filename)
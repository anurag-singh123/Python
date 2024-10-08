# Importing library
import qrcode

# Data to be encoded
data = 'linkedin.com/in/anurag-singh-aa59a31b3'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('MyQRCode1.png')

import cv2

# configurable parameters
source = "Rabbit.jpeg"
destination = 'newImage.png'
scale_percent = 50

# read the image
image = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# calculate new dimensions
new_width = int(image.shape[1] * scale_percent / 100)   #image.shape[1] → width (number of columns, i.e., pixels horizontally)
new_height = int(image.shape[0] * scale_percent / 100) #image.shape[0] → height (number of rows, i.e., pixels vertically)

# resize image correctly
output = cv2.resize(image, (new_width, new_height))

# save resized image
cv2.imwrite(destination, output)

print("Image resized successfully!")

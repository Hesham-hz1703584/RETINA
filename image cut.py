import cv2

# Load image, convert to grayscale, and find edges
image = cv2.imread('D:/Hesham/HBKU/RA/Rertina/Hesham_Test_ImData_Anant-20221128T151617Z-001/Hesham_Test_ImData_Anant/HBK000229000001_Retinal_Left_1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]

# Find contour and sort by contour area
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

# Find bounding box and extract ROI
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    ROI = image[y:y+h, x:x+w]
    break

cv2.imshow('ROI',ROI)
cv2.imwrite('ROI222.png',ROI)
cv2.waitKey()

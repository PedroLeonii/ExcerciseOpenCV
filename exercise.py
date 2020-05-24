import cv2,imutils


img = cv2.imread("tetramini.jpg")
(h,w,d) = img.shape

cv2.imshow("immagine",img)


#FILTRI
grayimg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("immagine scala di grigi",grayimg)



cv2.waitKey(0)
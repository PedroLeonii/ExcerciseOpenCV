import cv2,imutils


img = cv2.imread("tetramini.jpg")
(h,w,d) = img.shape

cv2.imshow("immagine",img)


#FILTRI
grayimg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("immagine scala di grigi",grayimg)

edgesimg = cv2.Canny(img,50,150)
cv2.imshow("immagine bordi", edgesimg)


imgblur = cv2.GaussianBlur(img,(11,11),0)
cv2.imshow("immagine filtro gaussian blur",imgblur)


cv2.waitKey(0)
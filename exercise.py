
import cv2 , imutils


img = cv2.imread("tetramini.jpg")
(h,w,d) = img.shape

cv2.imshow("immagine",img)

#OPERAZIONI


#FILTRI
grayimg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("immagine scala di grigi",grayimg)

edgesimg = cv2.Canny(img,50,150)
cv2.imshow("immagine bordi", edgesimg)


imgblur = cv2.GaussianBlur(img,(11,11),0)
cv2.imshow("immagine filtro gaussian blur",imgblur)

tresholdimg = cv2.threshold(grayimg,240,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("immagine sogliata",tresholdimg)

erodedimg = tresholdimg.copy()
erodedimg = cv2.erode(erodedimg,None,iterations= 7)
cv2.imshow("immagine erosa",erodedimg)

#RICONOSCIMENTO CONTORNI
countours = cv2.findContours(tresholdimg.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
countours = imutils.grab_contours(countours)

countoursimg = img.copy();

for cnt in countours:
    cv2.drawContours(countoursimg,[cnt],-1,(0,0,0),3)

cv2.putText(countoursimg, "Trovati {} oggetti".format(len(countours)), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
cv2.imshow("contorni immagine", countoursimg)

cv2.waitKey(0)
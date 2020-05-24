
import cv2 , imutils



img1 = cv2.imread("papa.jpg")
(h,w) = img1.shape[0:2]
cv2.imshow("immagine corona",img1)

#OPERAZIONI
center = (w // 2, h // 2)
method = cv2.getRotationMatrix2D(center,-180, 1.0)


partOfImg = img1[30:180, 10:300]
cv2.imshow("parte di immagine", partOfImg)

rotatedimg = cv2.warpAffine(img1,method,(w,h))
cv2.imshow("immagine ruotata 180 ",rotatedimg)


rotatedimg2 = imutils.rotate_bound(img1, -95)
cv2.imshow("immagine 1 ruotata 95 ", rotatedimg2)

scala = 300.0 / w;
newSize = (300, int(h * scala))

resizedimg = cv2.resize(img1, newSize)
cv2.imshow("immagine ridimensionata", resizedimg)

cv2.rectangle(img1, (400, 200), (420, 100), (0, 0, 255), 2)
cv2.circle(img1, (100, 130), 30, (0, 0, 255), -1)
cv2.line(img1, (50, 300), (300, 300), (0, 0, 255), 4)
cv2.putText(img1, "Ciao mondo", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
cv2.imshow("immagine colorata", img1)


img = cv2.imread("tetramini.jpg")
cv2.imshow("immagine",img)

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
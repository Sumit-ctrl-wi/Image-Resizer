import cv2

source="bholenath3.jpeg"
destination='newimage1.png'
scale_percent=50
src=cv2.imread(source,cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",src)
width=int(src.shape[1]*scale_percent/100)
height=int(src.shape[0]*scale_percent/100)
dsize=(width,height)
output=cv2.resize(src,dsize)
cv2.imwrite('newimage.jpeg',output)
# cv2.waitKey(0)

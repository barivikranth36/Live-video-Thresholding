import cv2

cap = cv2.VideoCapture(0)       #Capturing Video from camera no. 0
if cap.isOpened():
    ret, frame = cap.read()
    print(ret)

else:
    ret = False

while ret:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    o = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 51, 2)
    # prxint(type(ret))
    # print(ret)
    cv2.imshow('Preview',o)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
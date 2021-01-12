import cv2
import numpy as np



def process(frame,bg):
	r,g,b=frame[:,:,0],frame[:,:,1],frame[:,:,2]
	br,bg,bb=bg[:,:,0],bg[:,:,1],bg[:,:,2]
	r=r.astype("uint8")
	g=g.astype("uint8")
	b=b.astype("uint8")
	br=br.astype("uint8")
	bg=bg.astype("uint8")
	bb=bb.astype("uint8")
	mask=(abs((r*0.241+g*0.691+b*0.068)-(br*0.241+bg*0.691+bb*0.068))>80).astype("uint8").reshape(frame.shape[:2]+(1,))
	f=frame*mask
	# f=cv2.filter2D(f,-1,np.ones((3,3),np.float32)/9)# Feather
	return f



cap=cv2.VideoCapture(0)
bg=cap.read()[1]



while True:
	_,frame=cap.read()
	cv2.imshow("Cap",frame)
	p=process(frame,bg)
	cv2.imshow("Person",p)
	if (cv2.waitKey(1)&0xff==27):
		break



cap.release()
# % -*- coding: utf-8 -*-

import cv2
import pickle
#from hostel.models import *
import datetime
import os
#print(os.listdir('ml_code/database'))
label=list(os.listdir('ml_code/database'))

"""def fun(stud_id,date,status):
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="investigation"
        )

    mycursor = mydb.cursor()
    sql="SELECT * FROM studentgrievence_student_attendance WHERE st_id={} and date='{}'".format(stud_id,date)
    #print(sql)
    #val=
    mycursor.execute(sql)
    if len(mycursor.fetchall())==0:
        mycursor = mydb.cursor()
        sql = "insert into studentgrievence_student_attendance(st_id, date, status)values(%s,%s,%s)"
        val = (stud_id,date,status)
        mycursor.execute(sql, val)
        mydb.commit()
    else:
        pass"""

 
def face_recognize(status):
	base_dir="ml_code/"
    # create objects
	cam = cv2.VideoCapture(0)
    #model = cv2.createFisherFaceRecognizer()
    #model = cv2.face.FisherFaceRecognizer_create()
	model = cv2.face.LBPHFaceRecognizer_create()
	faceD = cv2.CascadeClassifier(base_dir+"haarcascade_frontalface_default.xml")

	f= open(base_dir+"cand.txt","w")
	f.write("")
	f.close()
	i=0
	flag=0

	f=open(base_dir+"candt.txt", "r")
	contents =f.read()
	print(contents)



	with open(base_dir+'model.pkl', 'rb') as f:
			ids = pickle.load(f)
	model.read(base_dir+'model.xml')
	cnt=0
	uid="null"
	while (cam.isOpened()):
		ret, frame = cam.read()
		if not(ret):
			continue
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = faceD.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			face = gray[y:y+h,x:x+w]
			face = cv2.resize(face,(130,100))
			result = model.predict(face)
			print(label)
			print(result)
			print("prediction:",label[int(result[0])])
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #uid=ids[result[0]]
			uid=label[int(result[0])]
			time= datetime.datetime.now()
			print(uid)
			print(time)
			print(status)
			if result[1]<70:
            

                #cv2.putText(frame,'{}'.format(ids[result[0]]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
                
                
				flag=1
			else:
				uid="null"
				

        #cv2.imshow("video", frame)
        #print(ids[result[0]])
		cnt+=1
		if flag==1 or cnt>30:
            #fun(str(uid),str(time)[:10],str("attendance_marked"))
			cam.release()
			cv2.destroyAllWindows()
			#user=wattendence(studentname=uid,date=)
			break
	return uid

#face_recognize("entry")


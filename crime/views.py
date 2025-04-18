from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from  django.core.files.storage import FileSystemStorage
from django.conf import settings

from ml_code.create_db import create_data
from ml_code.train_db import train_faces
from ml_code.face_recognition import face_recognize
from .models import *


#encryption algotithms
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import base64

def encrypt(data):
	data=data.encode("utf8")
	key = get_random_bytes(16)
	cipher = AES.new(key, AES.MODE_EAX)
	ciphertext = cipher.encrypt(data)
	nonce = cipher.nonce
	key=base64.b64encode(key)
	ciphertext=base64.b64encode(ciphertext)
	nonce=base64.b64encode(nonce)
	print(key,"\n",ciphertext,"\n",nonce)
	return key.decode("utf8"),ciphertext.decode("utf8"),nonce.decode("utf8")
	
def decrypt(key,ciphertext,nonce):
	key=base64.b64decode(key)
	ciphertext=base64.b64decode(ciphertext)
	nonce=base64.b64decode(nonce)
	cipher = AES.new(key, AES.MODE_EAX, nonce)
	data = cipher.decrypt(ciphertext)
	return data.decode("utf8")

def first(request):
    return render(request,'index.html')
    
    
    
def index(request):
    return render(request,'index.html')    

def index(request):
    return render(request,'index.html')
    
        

def reg(request):
    return render(request,'register.html')    
    
    
def addreg(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        password=request.POST.get('password')
        user=register(name=name,email=email,phone=phone,address=address,password=password)
        user.save()
        return render(request,'register.html')


def stud(request):
    return render(request,'studreg.html')    
    
    
def addstud(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        mothername=request.POST.get('mothername')
        fathername=request.POST.get('fathername')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        myfile = request.FILES['id_proof']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        password=request.POST.get('password')
        user=student_reg(name=name,email=email,phone=phone,mothername=mothername,fathername=fathername,gender=gender,age=age,id_proof=filename,password=password,status="pending")
        user.save()
    return render(request,'studreg.html')
                

def login(request):
    return render(request,'login.html')    
            
        
def dash(request):
    return render(request,'admin/index.html')    

        
def dashdept(request):
    return render(request,'department/index.html')                   
        
def logint(request):
    email = request. POST.get('email')
    password = request.POST.get('password')
   # print(email)
    if email == 'admin@gmail.com' and password == 'admin':
        request.session['logintdetail'] = email
        request.session['logint'] = 'admin'
        print ("ello")
        return render(request, 'admin/index.html')

    elif register.objects.filter(email=email,password=password).exists():
        userdetails=register.objects.get(email=email, password=password)
        request.session['uid'] = userdetails.id
        
        return render(request,'index.html')  


    elif department.objects.filter(email=email,password=password).exists():
            userdetails=department.objects.get(email=email, password=password)
            request.session['did'] = userdetails.id
            
            return render(request,'department/index.html')       
            
            

    elif student_reg.objects.filter(email=email,password=password,status="accepted").exists():
            userdetails=student_reg.objects.get(email=email, password=password)
            request.session['sid'] = userdetails.id
            
            return render(request,'index.html')       
                    
        
    else:
        return render(request, 'login.html', {'status': 'INVALID USERID OR PASSWORD'})           
  


def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)  

def addcomplaint(request):
    if request.method == 'POST':
        subject=request.POST.get('subject')
        description=request.POST.get('description')
       
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        emp=complaint(userid_id=request.session['uid'],subject=subject,description=description,image=filename,status="pending")    
        emp.save()
    return render(request,'complaint.html')
  
 
 
def adddept(request):
    if request.method == 'POST':
        department_name=request.POST.get('department_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
       
      
        emp=department(department_name=department_name,email=email,password=password)    
        emp.save()
    return render(request,'admin/adddepatment.html') 
    
    
    
def viewusers(request):
    sel=register.objects.all()
    return render(request,'admin/viewusers.html',{'res':sel})           

def viewdept(request):
    sel=department.objects.all()
    return render(request,'admin/viewdepartment.html',{'res':sel})      


def viewcompts(request):
    sel=complaint.objects.filter(id=request.session['uid'])
    return render(request,'viewcom.html',{'res':sel})     



def addstation(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('email')
        location=request.POST.get('email')
        password=request.POST.get('password')
       
      
        emp=station(name=name,email=email,phone=phone,location=location,password=password)    
        emp.save()
    return render(request,'department/policestation.html') 
                        
    
def addcriminal(request):
	if request.method == 'POST':
		name=request.POST.get('name')
		description=request.POST.get('description')
		myfile = request.FILES['image']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name,myfile)
		emp=criminal(dept_id=request.session['did'],name=name,description=description,image=filename)    
		emp.save()
		user=criminal.objects.get(name=name)
		create_data(str(user.id))
		train_faces()
	return render(request,'department/criminals.html') 

def viewcrimfilter(request):
    if request.method == 'POST':
        sel=criminal.objects.filter(name=request.POST.get('name'))
        return render(request,'department/viewcriminals.html',{'res':sel})
    
    
def viewcriminal(request):
    sel=criminal.objects.all()
    return render(request,'department/viewcriminals.html',{'res':sel})   




def viewcriminalprofile(request):
    criminal_id=face_recognize("entry")
    if criminal_id=="null":
        return render(request,'department/profile.html',{'res':criminal_id})
    print("detected criminal is:",criminal_id)
    sel=criminal.objects.get(id=criminal_id)
    return render(request,'department/profile.html',{'res':sel})  
     

def viewcomp(request):
    sel=complaint.objects.all().values('id','userid__name','userid__address','subject','image','description','status')
    return render(request,'department/viewcomp.html',{'res':sel})      


def useraccept(request,id):
    sel=complaint.objects.get(id=id)
    sel.status='accepted'
    sel.save()  
    return render(request,'department/viewcomp.html')
    
    
def userreject(request,id):
    sel=complaint.objects.get(id=id)
    sel.status='rejected'
    sel.save()  
    return render(request,'department/viewcomp.html')    
    

def crimi(request):
    sel=criminal.objects.filter(id=request.session['uid'])
    return render(request,'viewcrimi.html',{'res':sel})        
    
    
    
def viewwstud(request):
    sel=student_reg.objects.all()
    return render(request,'department/viewstudent.html',{'res':sel})      


def studaccept(request,id):
    sel=student_reg.objects.get(id=id)
    sel.status='accepted'
    sel.save()  
    return render(request,'department/viewstudent.html')
    
    
def studreject(request,id):
    sel=student_reg.objects.get(id=id)
    sel.status='rejected'
    sel.save()  
    return render(request,'department/viewstudent.html')      
    
    
    
    
def addfir(request):
    if request.method == 'POST':
        case_no=request.POST.get('case_no')
        description=request.POST.get('description')
        victim_details=request.POST.get('victim_details')
        data=victim_details

        key,ciphertext,nonce=encrypt(data)
        date=request.POST.get('date')
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        
        uploadfile = request.FILES['image1']
        fs1 = FileSystemStorage()
        filename1 = fs1.save(uploadfile.name,uploadfile)
        
        
        emp=fir(case_no=case_no,description=description,date=date,victim_details=ciphertext,image=filename,image1=filename1,privatekey=key,publickey=nonce)    
        emp.save()
		
    return render(request,'department/addfirs.html') 
 


def viewstudfir(request):
    sel=fir.objects.all()
    return render(request,'viewstudfir.html',{'res':sel})

def viewstudfirfilter(request):
	if request.method == 'POST':
		sel=fir.objects.filter(case_no=request.POST.get('name'),date=request.POST.get('date'))
		return render(request,'viewstudfir.html',{'res':sel})


def viewfirr(request):
    sel=fir.objects.all()
    dat=list()
    for i in sel:
         data=decrypt(i.privatekey.encode("utf8"),i.victim_details.encode("utf8"),i.publickey.encode("utf8"))
         dat.append({'case_no':i.case_no,'victim_details':data,'description':i.description,'date':i.date,'image':i.image,'image1':i.image})
         #print(data)
    return render(request,'admin/viewfir.html',{'res':dat})
	
def viewfirrfilter(request):
    sel=fir.objects.filter()
    return render(request,'admin/viewfir.html',{'res':sel})
  
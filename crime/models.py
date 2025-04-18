from django.db import models


class register(models.Model):
    id = models.IntegerField(primary_key = True)
    name=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    email=models.CharField(max_length=150)  
    phone=models.CharField(max_length=150)  
    password=models.CharField(max_length=150)  
    
    
    
class complaint(models.Model):
    id = models.IntegerField(primary_key = True)
    userid=models.ForeignKey(register,on_delete=models.DO_NOTHING)
    subject=models.CharField(max_length=150)
    description=models.CharField(max_length=150)  
    image=models.CharField(max_length=150)  
    status=models.CharField(max_length=150)      
    
    
    
class department(models.Model):
    id = models.IntegerField(primary_key = True)
    department_name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)  





class criminal(models.Model):
    id = models.IntegerField(primary_key = True)
    name=models.CharField(max_length=150)
    description=models.CharField(max_length=150)
    dept_id=models.CharField(max_length=150)
    image=models.CharField(max_length=150)

class student_reg(models.Model):
    id = models.IntegerField(primary_key = True)
    name=models.CharField(max_length=150)
    fathername=models.CharField(max_length=150)
    mothername=models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    age=models.CharField(max_length=150)
    id_proof=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    email=models.CharField(max_length=150)  
    phone=models.CharField(max_length=150)  
    password=models.CharField(max_length=150)  
    

class fir(models.Model):
    id = models.IntegerField(primary_key = True)
    case_no=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    description=models.CharField(max_length=150)  
    image=models.CharField(max_length=150)  
    image1=models.CharField(max_length=150)  
    victim_details=models.CharField(max_length=150)  
    privatekey=models.CharField(max_length=150)  
    publickey=models.CharField(max_length=150)  
    
         
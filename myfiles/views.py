from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def home(malumot):
    return render(malumot, 'asosiy.html')

def salom(malumot):
    ws = Teach.objects.all()
    return render(malumot, 'Oqituvchilar.html', {'ustoz':ws})

def salom1(malumot):
    if 'iddd' in malumot.POST:
        name = malumot.POST.get('ismi')
        fam = malumot.POST.get('familyasi')
        yosh = malumot.POST.get('yoshi')
        sana = malumot.POST.get('kuni')
        fan_id = malumot.POST.get('fani')
        fan = Fan.objects.get(id=fan_id)
        id_raqam = malumot.POST.get('iddd')
        Student(id=id_raqam,ism=name, fam=fam, yosh=yosh, sana=sana, fan=fan).save()

    elif 'ismi' in malumot.POST:
        name = malumot.POST.get('ismi')
        fam = malumot.POST.get('familyasi')
        yosh = malumot.POST.get('yoshi')
        sana = malumot.POST.get('kuni')
        fan_id = malumot.POST.get('fani')
        fan = Fan.objects.get(id=fan_id)
        Student(ism=name,fam=fam,yosh=yosh,sana=sana,fan=fan).save()
    s = Student.objects.all()
    return render(malumot, 'Oquvchilar.html', {'stu':s})

def talaba_qoshish(malumot):
    fanlar = Fan.objects.all()
    return render(malumot,'add_student.html',{'fans':fanlar})

def delete_student(malumot,sss):
    talaba = Student.objects.get(id=sss).delete()
    s = Student.objects.all()
    return render(malumot,'Oquvchilar.html',{'stu':s})

def update_teacher(malumot,id):
    teacher = Student.objects.get(id=id)
    fanlar = Fan.objects.all()
    return render(malumot,'update_teacher.html',{'teacher':teacher,'fans':fanlar})
"""
CRUD
C --- CREATE
R --- READ
A --- ADD
U --- UPDATE
D --- DELETE


"""
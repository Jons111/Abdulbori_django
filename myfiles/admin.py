from django.contrib import admin
from myfiles.models import Student, Fan, Teach, Fans


# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','ism','fam','fan','sana','yosh']

admin.site.register(Student,AdminStudent)

class AdminFan(admin.ModelAdmin):
        list_display = ['id','nomi']
admin.site.register(Fan,AdminFan)



class AdminTeach(admin.ModelAdmin):
    list_display = ['id','ism','fam','fan','sana','yosh']

admin.site.register(Teach,AdminTeach)

class AdminFans(admin.ModelAdmin):
        list_display = ['id','nomi']
admin.site.register(Fans,AdminFans)
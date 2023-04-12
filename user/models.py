from django.db import models
from datetime import datetime,timedelta

class Language(models.Model):
    name=models.CharField(max_length=50)
    month_to_learn=models.IntegerField()

    def save(self,*args,**kwargs):
        if self.name == 'java script':
            self.name='Java Script'
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.name} - {self.month_to_learn}'


class AbstractPerson(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    phone_number=models.CharField(max_length=13)

    def save(self,*args,**kwargs):
        if not self.phone_number.startswith('+996'):
            self.phone_number="+996"+self.phone_number[1:]
        super().save(*args,**kwargs)

    class Meta:
        abstract=True


class Student(AbstractPerson):
    work_study_place=models.CharField(max_length=50,blank=True,null=True)
    has_own_notebook=models.BooleanField()
    preferred_os=models.CharField(verbose_name="выборка",choices=(
        ('windows','Windows'),
        ("macos",'MacOS'),
        ('linux','Linux')
    ))


class Mentor(AbstractPerson):
    main_work=models.CharField(max_length=50,blank=True,null=True)
    experience=models.DateField()
    students=models.ManyToManyField(Student,related_name='mentors',through='Course')


class Course(models.Model):
    name=models.CharField(max_length=50)
    language=models.ForeignKey(Language,on_delete=models.CASCADE,related_name='courses')
    date_started=models.DateField()
    mentor=models.ForeignKey(Mentor,on_delete=models.CASCADE,related_name='courses')
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='courses')

    def get_end_date(self):
        return self.date_started+timedelta(days=30.5*self.language.month_to_learn)

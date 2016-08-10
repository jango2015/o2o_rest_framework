from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DepartmentModel(models.Model):
    user=models.OneToOneField(User)
    company=models.ForeignKey(User, related_name='departments')
    department_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=15,)
    contacter=models.CharField(max_length=20)
    description=models.TextField(blank=True,null=True)

    class Meta:
        abstract=True





class Post(models.Model):
    title=models.CharField(max_length=100)
    department=models.ForeignKey(User,verbose_name='post_infos',help_text='your department',)
    date=models.DateField()
    description=models.CharField(max_length=200)
    is_varified=models.BooleanField(default=False)
    reason_of_deny=models.TextField(max_length=300,blank=True,null=True)

    class Meta:
        abstract = True

BUSSINESS_TYPE=(('CS','computer science'),('EE','electric engnieer'))
class Department(DepartmentModel):

    bussiness_area=models.CharField(max_length=3,choices=BUSSINESS_TYPE)

    def __str__(self):
        return self.user.username


STATE=(('BJ','BJ'),('TJ','TJ'))
CITY=(('HD','HD'),('BH','BH'))
BUSSINESS_TYPE=(('CS','computer science'),('EE','electric engnieer'))
AREAR_TYPE=(('CS','computer science'),('EE','electric engnieer'))


class RecruitmentInformation(Post):

    begin_date=models.DateField()
    end_date=models.DateField()
    salary=models.PositiveIntegerField()
    major_area=models.CharField(max_length=2,choices=AREAR_TYPE)
    state=models.CharField(max_length=2,choices=STATE)
    city=models.CharField(max_length=2,choices=CITY)

    def __str__(self):
        return self.title
from django.db import models

from django.contrib.auth.models import User

from o2o_rest_framwork.department_model.models import RecruitmentInformation


STATUS=(('w','waiting'),('a','approving'),('d','denied'),('s','start'),('f','finishing'),('c','complaining'))
class Order(models.Model):

    date=models.DateField()
    recruitment=models.ForeignKey(RecruitmentInformation)
    applier=models.ForeignKey(User)
    status=models.CharField(max_length=3,choices=STATUS,default='w') # W: means waiting be a validate application,a means it's approving~
    is_engineer_review=models.BooleanField(default=False)
    is_department_review=models.BooleanField(default=False)

    class Meta:
        abstract = True

class ApplicationManager(models.Manager):

    'will override the original one'
    # def all(self):
    #     qs = super(ApplicationManager,self).all()
    #     return qs

    def filter_by_company(self,user):

        qs = super(ApplicationManager,self).filter(recruitment__department__department__company=user)
        return qs

    def filter_by_department(self,user):

        qs = super(ApplicationManager,self).filter(recruitment__department=user)
        return qs




class Application(Order):

    applier_message=models.TextField()
    complain_reason = models.TextField(null=True,blank=True)

    objects = ApplicationManager()

    def __str__(self):
        return 'application'+str(self.id)


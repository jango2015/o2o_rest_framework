from django.db import models
from django.contrib.auth.models import User

BUSSINESS_TYPE=(('CS','computer science'),('EE','electric engnieer'))

class Enterprise(models.Model):
    user=models.OneToOneField(User)
    company_name=models.CharField(max_length=50)
    permit_id=models.CharField(max_length=30)
    website=models.URLField(blank=True,null=True)
    phone=models.CharField(max_length=15,)
    contacter=models.CharField(max_length=20)
    permit_img=models.FileField(upload_to='permitImg')
    bank_name=models.CharField(max_length=90)
    money_amount=models.IntegerField(default=0)
    account_bank_name=models.CharField(max_length=200)
    bank_permit_img=models.FileField(upload_to='BankImg')
    company_telphone=models.CharField(max_length=16)
    is_approved=models.BooleanField(default=False)
    description=models.TextField(blank=True,null=True)

    class Meta:
        abstract=True


    def get_review_score(self):
        '''
        return a review score
        '''
        return

    def get_all_comment(self):

        return
    def get_credit(self):
        return





class Company(Enterprise):

    bussiness_area=models.CharField(max_length=3,choices=BUSSINESS_TYPE)

    def __str__(self):
        return self.user.username

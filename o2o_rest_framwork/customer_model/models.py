from django.db import models
from django.contrib.auth.models import User
# Create your models here.




# abstract level
class CustomerModel(models.Model):

    user = models.OneToOneField(User)
    phone=models.CharField(max_length=15)
    dob=models.DateField()
    ssn=models.CharField(max_length=20)
    description=models.CharField(max_length=200)

    class Meta:
        abstract=True


    def get_review_score(self):
        '''
        return a review score
        '''
        return

    def get_all_comment(self):

        return



MAJOR_TYPE=(('CS','computer science'),
            ('EE','electric engnieer')
            )
DEGREE_TYPES=(
    ('H','Highschool'),
    ('B','Banchler'),
    ('M','Master'),
    ('P','PHD'),
    )

class Engineer(CustomerModel):

    major = models.CharField(max_length=5, choices = MAJOR_TYPE  )
    degree = models.CharField(max_length=5, choices = DEGREE_TYPES )


    def __str__(self):
        return self.user.username


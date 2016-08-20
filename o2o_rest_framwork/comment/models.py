from django.db import models
from django import forms
from django.contrib.auth.models import User
from o2o_rest_framwork.order_model.models import Application
# Create your models here.

class CommentModel(models.Model):
    application=models.ForeignKey(Application,related_name='comments')
    starts=models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5)),default=3)
    review=models.CharField(null=True,max_length=300,blank=True)
    from_user = models.OneToOneField(User,related_name='senders')
    to_user = models.OneToOneField(User,related_name='receivers')
    date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Comment(CommentModel):

    def __str__(self):

        return 'comment form '+ str(self.from_user) + ' to ' + str(self.to_user)+ ''+ str(self.application)




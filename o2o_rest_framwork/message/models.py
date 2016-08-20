from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MessageModel(models.Model):
    from_user=models.ForeignKey(User,related_name='sender')
    to_user=models.ForeignKey(User,related_name='receiver')
    time=models.DateTimeField(auto_now_add=True)
    content=models.TextField(max_length=1000)
    is_read=models.BooleanField(default=False)

    class Meta:
        abstract = True


class Messagemanager(models.Manager):

    def get_number_of_unread_message(self,user):

        num = Message.objects.filter(to_user=user,is_read=False).count()

        return num

class Message(MessageModel):

    objects = Messagemanager()

    def __str__(self):

        return "message"+str(self.from_user.username)+'to'+str(self.to_user.username)+'id:'+str(self.id)




from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from .models import *
from django.dispatch import receiver


# SENDER IS A USER HERE

@receiver(user_logged_in,sender=User)
def loggedin_successful(sender,request,user,**kwargs):
    print("-------------------")
    print("loggin signal")
    print("Sender: ", sender)
    print("Request: ",request)
    print("User: ",user)
    print(f'kwargs:{kwargs}')



@receiver(user_login_failed)
def loggedin_failed(sender,request,credentials,**kwargs):
    print("-------------------")
    print("loggin signal")
    print("Sender: ", sender)
    print("Request: ",request)
    print("User: ",credentials)
    print(f'kwargs:{kwargs}')



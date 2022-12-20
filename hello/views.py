""" Hello Views """
from django.http import HttpResponse

def home(_):
    """ Home """
    return HttpResponse("Hello, Django!")

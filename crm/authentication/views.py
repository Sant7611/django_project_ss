from django.shortcuts import render, redirect
from django.http import HttpResponse
import json



class Student():
    def __init__(self, name, standard, age):
        self.name= name
        self.standard= standard
        self.age=age

    # def introduce(self):
    #     return f'My name is {self.name}. i am {self.age} years old. I study in {self.standard}'

stu1 = Student('santosh', 'bachelors', 23)
stu_json = json.dumps(stu1.__dict__)



#reutnr content type a plain text
def plain_text(request):
    # return HttpResponse(f'My name is santosh Bohara {type(request)} ', content_type='text/plain')
    return HttpResponse(f'My name is santosh Bohara {type(request)} ')

def json_text(request):
    # return HttpResponse(stu_json,content_type='application/json' )
    return HttpResponse(stu_json )

def image_return(request):
    return HttpResponse('this is video file', content_type='video/mp4')

def html_render(request):
    return HttpResponse('<h1>Hello my name is Santosh</h1>', content_type='text/html')

from django.shortcuts import render

from ninja  import NinjaAPI, Schema,ModelSchema
from .models import Framework

api = NinjaAPI()

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    
    
class FrameworkSchema(ModelSchema):
    class Meta:
        model = Framework
        fields = ['name','language']

@api.get("/hello")
def hello(request ,name:str ="stranger"):
    return{'greetings': 'Hello(name)'}

@api.get("/user",response=UserSchema)
def user(request):
    return request.user


@api.get("/frameworks",response=list[FrameworkSchema])
def frameworks(request):
    return Framework.objects.all()


@api.post("/frameworks",response=FrameworkSchema)
def create_frameworks(request,payload:FrameworkSchema):
    frameworks=Framework.objects.create(**payload.dict())
    return frameworks
    


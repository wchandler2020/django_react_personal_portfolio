from django.shortcuts import render
from rest_framework import generics
from .models import Hero, Experience, About
from .serializers import HeroSerializer, ExperienceSerializer, AboutSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class HeroView(generics.CreateAPIView):
    queryset =Hero.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = HeroSerializer
    
class ExperienceView(generics.CreateAPIView):
    queryset =Experience.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = ExperienceSerializer
    
class AboutView(generics.CreateAPIView):
    queryset =About.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = About

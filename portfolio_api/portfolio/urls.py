from django.urls import path
from portfolio import views as portfoli_views

urlpatterns = [
    path('user/hero', portfoli_views.HeroView.as_view()),
    path('user/experience', portfoli_views.ExperienceView.as_view()),
    path('user/about', portfoli_views.AboutView.as_view())
]

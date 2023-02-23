from django.urls import path
# from Users.views import homePage
from .views import *


urlpatterns =[
    path('', homePage, name="home_page"),
    path('home/', homePage1, name="Home_Page1"),
    path('listStatic/', listEventsStatic, name="Events-listS"),
    path('listD/', listEvents, name="Events-list"),

]
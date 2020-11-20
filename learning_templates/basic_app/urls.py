from django.conf.urls import url
from basic_app import views

#TEMPLATE TAGGING
#We need to set our application name a variable(app_name) and defined it as a GLOBAL VARIABLE
app_name = 'basic_app'

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    ]

from django.conf.urls import url
from main_list.views import *


urlpatterns = [

url(r'^$', PostMysql.as_view(), name='index'),
url(r'^main_list/$', PostApache.as_view(), name='apache'),
url(r'^main_list/$', PostServer.as_view(), name='server'),

]

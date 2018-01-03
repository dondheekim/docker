from django.conf.urls import url
from blog.views import *
from blog import views
#날짜와 관련된 제네릭 뷰 정의
urlpatterns = [
    #/blog/ 요청을 처리할 뷰 클래스를 PostLV로 정의. 패턴이름은 blog:index
    url(r'^$', PostLV.as_view(), name='index'),
    
    url(r'^post/(?P<pk>[0-9]+)/comment/$', add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', comment_remove, name='comment_remove'),

    #/blog/post/ 요청을 처리할 뷰 클래스를 PostLV로 정의. 패턴이름은 blog:list
    url(r'^post/$', PostLV.as_view(), name='post_list'),

    #/blog/post/영단어 요청을 처리할 뷰 클래스를 PostDV로 정의. 패턴이름은 blog:detail
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    #/blog/archive 요청을 처리할 뷰 클래스를 PostAV로 정의. 패턴이름은 blog:archive
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),

    #/blog/4자리숫자 요청을 처리할 뷰 클래스를 PostYAV로 정의. 패턴이름은 blog:post_year_archive'
    url(r'^post/(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    #/blog/4자리숫자/3자리소문자 요청을 처리할 뷰 클래스를 PostMAV로 정의. 패턴이름은 blog:post_month_archive'
    url(r'^post/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),

    #/blog/4자리숫자/3자리소문자 /1~2숫자소문자 요청을 처리할 뷰 클래스를 PostDAV로 정의. 패턴이름은 blog:post_day_archive'
    url(r'^post/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    #/blog/today 요청을 처리할 뷰 클래스를 PostTAV로 정의. 패턴이름은 blog:post_today_archive'
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),

    url(r'^add/$', PostCreateView.as_view(), name="add", ),

    url(r'^change/$', PostChangeLV.as_view(), name="change", ),

    url(r'^(?P<pk>[0-9]+)/update/$', PostUpdateView.as_view(), name="update", ),

    url(r'^(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name="delete", ),

]

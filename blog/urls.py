from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^api/$',views.android,name='android'),
	url(r'^api2/$',views.newPostFromAndroid, name='newPostFromAndroid'),
	url(r'^posts/$',views.displayAndroid,name='displayAndroid'),
	url(r'^searchapi/$',views.search,name='search'),
    	
]
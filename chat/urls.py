from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page$', views.pages, name='pages'),
    url(r'^comments$', views.comments, name='comments'),
    url(r'^chat$', views.chat, name='chat'),
    url(r'^logout_us$', views.logout_us, name='logout_us'),
    url(r'^chatbootstrap$', views.chatbootstrap, name='chatbootstrap'),
    url(r'^messages$', views.messages, name='messages'),
    url(r'^choice_page$', views.choice_page, name='choice_page')
]
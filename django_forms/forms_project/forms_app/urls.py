from django.conf.urls import url
from forms_app import views

app_name = 'forms_app'

urlpatterns = [
    url(r'list', views.TopicListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.TopicDetailView.as_view(), name='detail'),
    url(r'^newtopic$', views.TopicCreateView.as_view(), name='create'),
    url(r'updatetopic/(?P<pk>\d+)/$', views.TopicUpdateView.as_view(), name='update'),
    url(r'deletetopic/(?P<pk>\d+)/$', views.TopicDeleteView.as_view(), name='delete'),
]

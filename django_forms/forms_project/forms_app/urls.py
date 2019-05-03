from django.conf.urls import url
from forms_app import views

app_name = 'forms_app'

urlpatterns = [
    url(r'list', views.TopicListView.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', views.TopicDetailView.as_view(), name='detail'),
    url(r'createview', views.TopicCreateView.as_view(), name='create'),
]

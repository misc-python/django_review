from django.conf.urls import url
from forms_app import views

app_name = 'forms_app'

urlpatterns = [
    url('list', views.TopicListView.as_view(), name='list'),
]

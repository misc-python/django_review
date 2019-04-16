from django.shortcuts import render
from forms_app.models import Topic, Webpage, AccessRecord
# Create your views here.


def home_view(request):
    return render(request, 'forms_app/index.html', {'message': 'hello~'})


def form_view(request):
    topic = Topic.objects.all()
    topic_dict = {'topic': topic}

    return render(request, 'forms_app/forms.html', context=topic_dict)

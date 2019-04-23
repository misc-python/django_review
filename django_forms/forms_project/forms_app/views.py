from django.shortcuts import render
from forms_app.models import Topic, Webpage, AccessRecord
from forms_app.forms import FormName, FormNewPerson
from . import forms
# Create your views here.


def home_view(request):
    """Home page."""
    context = {
        "text": "this is for django filter",
        "number": 150,
    }
    return render(request, 'forms_app/index.html', context=context)


def newPerson_view(request):
    """To access the newPerson form (unrealted to django's User model)."""
    form = forms.FormNewPerson()
    if request.method == "POST":
        form = forms.FormNewPerson(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home_view(request)
        else:
            print('Error from invalid newPerson form.')

    return render(request, 'forms_app/newPerson.html', {'form': form})


def show_form_view(request):
    """To show all data in Topic model."""
    topic = Topic.objects.all()
    topic_dict = {'topic': topic}

    return render(request, 'forms_app/show_forms.html', context=topic_dict)


def testform_view(request):
    """Test form not linked to a model."""
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('form is valid')
            print("Name: ", form.cleaned_data['name'])
            print("Email: ", form.cleaned_data['email'])
            print("Message: ", form.cleaned_data['text'])

    return render(request, 'forms_app/testforms.html', {'form': form})


def userprofile_view(request):
    """Extension of django's User model."""
    form = forms.FormUserProfileInfo()

    return render(request, 'forms_app/userform.html', {'form': form})






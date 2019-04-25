from django.shortcuts import render
from forms_app.models import Topic, Webpage, AccessRecord
from forms_app.forms import FormName
from . import forms


def home_view(request):
    """Home page."""
    context = {
        "text": "this is for django filter",
        "number": 150,
    }
    return render(request, 'forms_app/index.html', context=context)


def show_topic(request):
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

    if request.method == "POST":
        form = forms.FormUserProfileInfo(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home_view(request)
        else:
            print('Error updating UserProfile Form.')

    return render(request, 'forms_app/userform.html', {'form': form})


def register(request):
    """To process registration page."""
    registered = False

    if request.method == "POST":
        user_form = forms.FormUser(data=request.POST)
        profile_form = forms.FormUserProfileInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # To hash the password:
            user.set_password(user.password)

            user.save()

            profile = profile_form.save(commit=False)

            # To set up one-to-one relationship:
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = forms.FormUser
        profile_form = forms.FormUserProfileInfo

    return render(request, 'forms_app/registration.html', 
        {'user_form': user_form,
         'profile_form': profile_form,
         'registered': registered,
        })




from django.shortcuts import render
from .models import Topic, Webpage, AccessRecord
from . import forms

# For login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# CBV:
from django.views.generic import View, TemplateView, ListView, DetailView

# CRUD:
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class CBView(View):
    def get(self, request):
        return HttpResponse('Basic class-based view')


class CBVTemplate(TemplateView):
    template_name = 'forms_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = 'hello TemplateView with context injection'
        context['number'] = 123
        return context


class TopicListView(ListView):
    model = Topic
    # this will return an object "topic_list", but we will change the object name
    context_object_name = 'topic'


class TopicDetailView(DetailView):
    context_object_name = 'topic'
    model = Topic
    template_name = 'forms_app/topic_detail.html'


class TopicCreateView(CreateView):
    fields = ('top_name', 'description')
    model = Topic


class TopicUpdateView(UpdateView):
    fields = ('top_name', 'description')
    model = Topic


class TopicDeleteView(DeleteView):
    model = Topic
    success_url = reverse_lazy("forms_app:list")


def home_view(request):
    """Home page."""
    context = {
        "text": "this is for django filter",
        "number": 150,
    }
    return render(request, 'forms_app/index.html', context=context)
    # return HttpResponse('this is http response.')


@login_required
def show_topic(request):
    """To show all data in Topic model."""
    topic = Topic.objects.all()
    topic_dict = {'topic': topic}

    return render(request, 'forms_app/show_topics.html', context=topic_dict)


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


def login_view(request):
    """To allow user to log in."""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            print('user email and password match.')
            if user.is_active:
                print('user is active.')
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Account not active.')
        else:
            print('Login failed. Username: {} and password: {}'.format(username, password))
            return HttpResponse('Invalid login.')
    else:
        return render(request, 'forms_app/login.html', {})


@login_required
def logout_view(request):
    """To allow user to log out."""
    logout(request)
    return HttpResponse('You are logged out.')








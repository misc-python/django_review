from django.contrib import admin
from forms_app.models import NewPerson
from forms_app.models import Topic, Webpage, AccessRecord, UserProfileInfo


admin.site.register(UserProfileInfo)
admin.site.register(NewPerson)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)

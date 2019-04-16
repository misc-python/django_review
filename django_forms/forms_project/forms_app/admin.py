from django.contrib import admin
from forms_app.models import User
from forms_app.models import Topic, Webpage, AccessRecord


admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)

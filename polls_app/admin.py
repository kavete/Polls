from django.contrib import admin
from polls_app.models import Question, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
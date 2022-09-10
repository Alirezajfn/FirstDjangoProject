from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = [(None, {'fields': ['question_text']}),
              ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
              ]


admin.site.register(Question, QuestionAdmin)
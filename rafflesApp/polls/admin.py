from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['questionText']}),
        ('Date info',   {'fields': ['pubDate']})
    ]

    list_display = ('questionText', 'pubDate', 'wasPublishedRecently')
    list_filter = ['pubDate']
    search_fields = ['questionText']
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)

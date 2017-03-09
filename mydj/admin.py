from django.contrib import admin

# Register your models here.
from mydj.models import *


@admin.register(Author,Publisher,Book,Items,Answers,ItemAnswer,Subject)
class AuthorAdmin(admin.ModelAdmin):
    pass

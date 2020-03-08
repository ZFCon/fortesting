from django.contrib import admin

from .models import *
from .forms import TestForm


class TestAdmin(admin.ModelAdmin):
    form = TestForm
admin.site.register(Test, TestAdmin)
admin.site.register(Country)
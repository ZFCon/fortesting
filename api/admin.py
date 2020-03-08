from django.contrib import admin
from django.forms import ModelForm


from .models import *

from django.utils.translation import gettext_lazy as _


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        actions_selection_counter = True
        date_hierarchy = 'timestamp'
        # labels = {
        #     'name': _('Writer'),
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }

class PersonAdmin(admin.ModelAdmin):
    form = PersonForm
    search_fields = ('name', )

def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)
    short_description = "Mark selected GEGs as Active"

class GEGAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"content": ("number",)}
    list_filter = ['email', 'first', 'last', 'is_active', 'birth']
    # filter = ['first', 'birth']
    list_display = ['email', 'first', 'last', 'is_active', 'colored_name']
    list_editable = ['is_active']
    # list_select_related = ('people')
    search_fields = ['first', 'last']
    raw_id_fields = ("people",)
    save_as = True
    actions = [make_active]
    
    fieldsets = (
        ("Main details", {
            'classes': ('wide', 'extrapretty'),
            'fields': ('first', 'last', 'email', 'color_code')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('birth', 'is_active', 'people', 'number', ('content')),
        }),
    )
    # autocomplete_fields = ['people']



class MembershipInline(admin.StackedInline):
    model = Membership

class SessionAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


admin.site.register(Person, PersonAdmin)
admin.site.register(GEG, GEGAdmin)
admin.site.register(Membership)
admin.site.register(Session, SessionAdmin)
from django.contrib import admin

from .models import Job, Contact

admin.site.register(Contact)


# The inline model should have a ForeignKey to the parent model
class ContactInline(admin.TabularInline):
    model = Contact


@admin.register(Job)  # form model admin
class JobAdmin(admin.ModelAdmin):
    # 'list_display' sets fields to be displayed on the admin page
    list_display = ['company_name', 'position', 'cv', 'cover_letter', 'response', 'date_applied', 'followup1',
                    'followup2', 'followup3']
    # makes a field editable in the admin page
    list_editable = ['cv', 'cover_letter', 'response']
    # shows a filter section on the admin site
    list_filter = ['company_name', 'position', 'cv', 'cover_letter']
    inlines = [ContactInline]

# The inline model should have a ForeignKey to the parent model

# class JobInline(admin.StackedInline):
#     model = Job


# class ExtendedJobInAdmin(JobAdmin):
#     inlines = JobAdmin.inlines + [JobInline]


# @admin.register(Contact)  # form model admin
# class ContactAdmin(admin.ModelAdmin):
#     inlines = [JobInline]


# admin.site.unregister(Job)
# admin.site.register(Job, ExtendedJobInAdmin)

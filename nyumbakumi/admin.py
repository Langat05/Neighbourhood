from django.contrib import admin
from .models import neighbourhood, Profile, Authorities, healthservices, Health



class HealthAdmin(admin.ModelAdmin):
    filter_horizontal =['healthservices']

# Register your models here.
admin.site.register(neighbourhood)
admin.site.register(Profile)
admin.site.register(Authorities)
admin.site.register(Health,HealthAdmin)
from django.contrib import admin
from . models import Objectives, Instructions

@admin.register(Objectives)
class ObjectivesAdmin(admin.ModelAdmin):
    list_display = ['objective_description','pk','id']

@admin.register(Instructions)
class InstructionsAdmin(admin.ModelAdmin):
    list_display = ['objective','step','pk','id']
    ordering = ('step',)


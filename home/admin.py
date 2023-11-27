from django.contrib import admin
from .models import Skill, Project, Experience, Contact
# Register your models here.

admin.site.register(Skill)  
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Contact)
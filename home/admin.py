from django.contrib import admin
from .models import Skill, Project, Experience, Contact, ProjectImage
# Register your models here.

admin.site.register(Skill)  
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Contact)
admin.site.register(ProjectImage)
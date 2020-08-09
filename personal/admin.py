from django.contrib import admin
from .models import about,projects,education,skillset,skills,awardandcertifications,interest, organizations,worksamples,resume
# Register your models here.
admin.site.register(about)
admin.site.register(projects)
admin.site.register(education)
admin.site.register(skillset)
admin.site.register(skills)
admin.site.register(awardandcertifications)
admin.site.register(interest)
admin.site.register(organizations)
admin.site.register(worksamples)
admin.site.register(resume)
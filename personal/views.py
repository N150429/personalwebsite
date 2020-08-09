from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import about,projects,education,skillset,skills,interest,awardandcertifications,organizations,worksamples,resume
from django.template import loader
# Create your views here.
def home(request):
	res = resume.objects.all()
	profile = about.objects.filter(id=1)
	work = worksamples.objects.all()
	org = organizations.objects.all()
	awards=awardandcertifications.objects.all()
	intr = interest.objects.all()
	skill=skills.objects.all()
	stds = education.objects.all()
	data = about.objects.all()
	proj = projects.objects.all()
	template = loader.get_template('base.html')
	context = {
	'data':data,
	'projects':proj,
	'education':stds,
	'skills':skill,
	'interest':intr,
	'awards':awards,
	'orgs':org,
	'works':work,
	'profile':profile,
	'file':res
	}
	return HttpResponse(template.render(context,request))

from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import RegisteredUser, Paper, Review

from .forms import RegisteredUserForm, PaperForm, ReviewForm

def home(request):
	title = '' # no nice welcome msg for anon users
	#if request.user.is_authenticated():
	#	title = "Welcome %s" %(request.user) #Displays a personalised welcome msg

	#gonna add a form here apparently
	context = {
		"title": title,
	}
	return render(request, "home.html", context)

def registration(request):
	form = RegisteredUserForm(request.POST or None)
	context = {
		# "title": title,
		"form": form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#print instance.id
		context = {
		#"title": "Thank You"
	}

	return render(request, "registration/registration_form.html", context)

def paper_sub(request):
	if request.method == 'POST':
		form = PaperForm(request.POST, request.FILES)
		if form.is_valid():
			new_paper = Paper(paper_file = request.FILES['paper_file'])
			new_paper.save

			# Redirect to the document list after POST
			return HttpResponseRedirect(reverse('ProjectX.papers.views.paper_sub'))

	else:
		form = PaperForm() #empty unbound form
		# Load documents for the list page
		paper_list = Paper.objects.all()
		# Render list page with the documents and the form
		return render_to_response(
			'paper_sub.html',
			{'paper_list': paper_list, 'form': form},
			context_instance=RequestContext(request)
			)

def review_sub(request):
	form = ReviewForm(request.POST or None)
	context = {
		# "title": title,
		"form": form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#print instance.id
		context = {
		#"title": "Thank You"
	}

	return render(request, 'review_sub.html', context)

def about(request):
	return render(request, "about.html", {})
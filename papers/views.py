from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Paper, Review, MyUser

from .forms import PaperForm, ReviewForm, RegisterForm, LoginForm

def home(request):
	title = '' # no nice welcome msg for anon users
	#if request.user.is_authenticated():
	#	title = "Welcome %s" %(request.user) #Displays a personalised welcome msg

	#gonna add a form here apparently
	context = {
		"title": title,
	}
	return render(request, "home.html", context)

# -----------------------needs to be commented out if you want to create a new superuser
def registration(request):

	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password2']
		new_user = MyUser()
		new_user.username = username
		new_user.email = email
		new_user.set_password
		new_user.save()
		# return redirect('login')
		return HttpResponseRedirect(reverse('login'))

	context = {
		"form": form,
		"action_value": "",
		"submit_btn_value": "Register"
	}
	return render(request, "registration.html", context)

def paper_sub(request):
	if request.method == 'POST':
		form = PaperForm(request.POST, request.FILES)
		if form.is_valid():
			new_paper = Paper(paper_file = request.FILES['paper_file'])
			new_paper.save

			# Redirect to the document list after POST
			return HttpResponseRedirect(reverse('paper_sub'))

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

def auth_login(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():						#Make sure that user is there
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		#print username, password
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
	context = {"form": form}
	return render(request, 'login.html', context)

def auth_logout(request):
	logout(request)
	#return HttpResponseRedirect('/')
	return render(request, 'logout.html')


def index(request):
    paper_list = Paper.objects.order_by('-Paper_SubmissionDate')[:5] # Need to adjust this !
    context = {'paper_list': paper_list}
    return render(request, 'papers/index.html', context)



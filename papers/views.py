from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import CommitteeMember, Paper, Reviewer, Review, Author

from .forms import CommitteeMemberForm, PaperForm, ReviewerForm, ReviewForm, AuthorForm

def home(request):
	title = '' # no nice welcome msg for anon users
	#if request.user.is_authenticated():
	#	title = "Welcome %s" %(request.user) #Displays a personalised welcome msg

	#gonna add a form here apparently
	context = {
		"title": title,
	}
	return render(request, "home.html", context)

def cm_reg(request):
	form = CommitteeMemberForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# print instance.cm_id
		# print instance.cm_name
		# print instance.cm_surnam
		# print instance.cm_institution
		# print instance.cm_email

	context = {
		"form": form
	}
	return render(request, "cm_reg.html", context)

def reviewer_reg(request):
	form = ReviewerForm
	context = {
		"form": form,
	}
	return render(request, "reviewer_reg.html", context)

def author_reg(request):
	form = AuthorForm
	context = {
		"form": form,
	}
	return render(request, "author_reg.html", context)

def index(request):
    paper_list = Paper.objects.order_by('-Paper_SubmissionDate')[:5] # Need to adjust this !
    context = {'paper_list': paper_list}
    return render(request, 'papers/index.html', context)


def paper(request, paper_code):
    question = get_object_or_404(Paper, pk=paper_code)
    return render(request, 'papers/paper.html', {'paper': paper})


def review(request, paper_code):
    return HttpResponse("You're reviewing paper %s." % paper_code)
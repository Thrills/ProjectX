from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Paper


def index(request):
    paper_list = Paper.objects.order_by('-Paper_SubmissionDate')[:5] # Need to adjust this !
    context = {'paper_list': paper_list}
    return render(request, 'papers/index.html', context)


def paper(request, paper_code):
    question = get_object_or_404(Paper, pk=paper_code)
    return render(request, 'papers/paper.html', {'paper': paper})


def review(request, paper_code):
    return HttpResponse("You're reviewing paper %s." % paper_code)
from django.shortcuts import render
from django.http import HttpResponse

from first_app.models import Question

def index(request):
	latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_questoin_list}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	return HttpResponse("You are looking at question %s." % question_id)

def result(request, question_id):
	return HttpResponse("You are looking at the results of question %s" % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting at %s" % question_id)
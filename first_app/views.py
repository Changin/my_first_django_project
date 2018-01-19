from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from first_app.models import Choice, Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'first_app/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request, 'first_app/detail.html', {'question' : question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#설문 폼을 다시 보여준다
		return render(request, 'first_app/detail.html', {
			'question' : question,
			'error_message' : "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('first_app:result', args=(question.id,)))

def result(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'first_app/results.html', {'question':question})
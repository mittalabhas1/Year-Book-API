from django.shortcuts import render
from django.views import generic

from Questions.models import Questions, Answers

class IndexView(generic.ListView):
	model = Questions
	template_name = "Questions/index.html"
	context_object_name = "list_of_questions"

class QuestionView(generic.DetailView):
	model = Questions
	template_name = "Questions/question.html"
	context_object_name = "ques"

def saveAnswer(request):
	"""
	Controls the answer post mechanism.
	Redirects to ques:index for success, otherwise to ques:question with 'qid' again.
	"""
	try:
		user = User.objects.get(pk=request.POST['uid'])
		question = Questions.objects.get(pk=request.POST['qid'])
		answer = Answers.objects.create(uid=user, qid=question, answer=request.POST['answer'])
		answer.save()
	except ValidationError as e:
		return HttpResponseRedirect(reverse(
			'ques:question', args=(request.POST['qid'],)
		))
	else:
		return HttpResponseRedirect(reverse('ques:index'))
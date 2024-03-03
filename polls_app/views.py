from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic
from polls_app.models import Choice, Question
from django.utils import timezone
import datetime
# Create your views here.

# def index(request):
#     latest_questions = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_questions])
#     template = loader.get_template("polls_app/index.html")
#     context = {
#         'latest_questions_list': latest_questions
#     }
#     return HttpResponse(template.render(context, request))


# def details(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls_app/details.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls_app/results.html', {'question': question})

def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls_app/details.html', { 'question': question, 'error-message': "You did not select a choice" })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls_app:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = "polls_app/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    

class DetailView(generic.DetailView):
    model = Question
    template_name ="polls_app/details.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name ="polls_app/results.html"
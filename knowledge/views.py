from django.shortcuts import render, get_object_or_404

from knowledge.models import Question, Response


def knowledge_index(request,
               template='django_knowledge/index.html'):

    questions = Question.objects.can_view(request.user)

    return render(request, template, {'questions': questions})


def knowledge_list(request,
              tags=None,
              template='django_knowledge/list.html'):

    questions = Question.objects.can_view(request.user)

    return render(request, template, {'questions': questions})


def knowledge_thread(request,
                question_id,
                slug=None,
                template='django_knowledge/thread.html'):

    question = get_object_or_404(
      Question.objects.can_view(request.user), 
      id=question_id)

    return render(request, template, {'question': question})


def knowledge_ask(request,
             template='django_knowledge/ask.html'):

    return render(request, template, {'form': 'form'})

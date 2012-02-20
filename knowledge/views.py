from django.shortcuts import render, redirect, get_object_or_404

from knowledge.models import Question, Response
from knowledge import settings


def knowledge_index(request,
                    template='django_knowledge/index.html',
                    BASE=settings.BASE_TEMPLATE):

    questions = Question.objects.can_view(request.user)

    return render(request, template, {
        'questions': questions,
        'BASE': BASE
    })


def knowledge_list(request,
                   tags=None,
                   template='django_knowledge/list.html',
                   BASE=settings.BASE_TEMPLATE):

    questions = Question.objects.can_view(request.user)

    return render(request, template, {
        'questions': questions,
        'BASE': BASE
    })


def knowledge_thread(request,
                     question_id,
                     slug=None,
                     template='django_knowledge/thread.html',
                     BASE=settings.BASE_TEMPLATE):

    question = get_object_or_404(
        Question.objects.can_view(request.user),
        id=question_id)

    if request.path != question.get_absolute_url():
        return redirect(question.get_absolute_url(), permanent=True)

    return render(request, template, {
        'question': question,
        'BASE': BASE
    })


def knowledge_ask(request,
                  template='django_knowledge/ask.html',
                  BASE=settings.BASE_TEMPLATE):

    return render(request, template, {
        'form': 'form',
        'BASE': BASE
    })

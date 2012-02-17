from django.shortcuts import render, get_object_or_404

from desk.models import Question, Response


def desk_index(request, 
                template='django_desk/index.html'):
    questions = Question.objects.all()
    return render(request, template, {'questions': questions})

def desk_list(request, 
                tags=None, template='django_desk/list.html'):
    questions = Question.objects.all()
    return render(request, template, {'questions': questions})

def desk_thread(request, question_id, 
                slug=None, template='django_desk/thread.html'):
    question = get_object_or_404(Question, id=question_id)
    return render(request, template, {'question': question})

def desk_ask(request, 
                template='django_desk/ask.html'):
    return render(request, template, {'form': 'form'})
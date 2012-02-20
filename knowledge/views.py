from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from knowledge.models import Question, Response, Category
from knowledge.forms import QuestionForm, ResponseForm
from knowledge.utils import paginate
from knowledge import settings


def knowledge_index(request,
                    template='django_knowledge/index.html',
                    BASE=settings.BASE_TEMPLATE):

    questions = Question.objects.can_view(request.user)[0:20]

    return render(request, template, {
        'questions': questions,
        'categories': Category.objects.all(),
        'BASE': BASE
    })


def knowledge_list(request,
                   category_slug=None,
                   template='django_knowledge/list.html',
                   Form=QuestionForm,
                   BASE=settings.BASE_TEMPLATE):

    search = request.GET.get('search', None)
    questions = Question.objects.can_view(request.user)

    if search:
        questions = questions.filter(
            Q(title__icontains=search) | Q(body__icontains=search)
        )

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        questions = questions.filter(categories=category)

    paginator, questions = paginate(questions, 50, 
            request.GET.get('page', '1'))

    return render(request, template, {
        'request': request,
        'search': search,
        'questions': questions,
        'category': category,
        'categories': Category.objects.all(),
        'form': Form(request.user),
        'BASE': BASE
    })


def knowledge_thread(request,
                     question_id,
                     slug=None,
                     template='django_knowledge/thread.html',
                     Form=ResponseForm,
                     BASE=settings.BASE_TEMPLATE):

    question = get_object_or_404(
        Question.objects.can_view(request.user),
        id=question_id)

    responses = question.get_responses(request.user)

    if request.path != question.get_absolute_url():
        return redirect(question.get_absolute_url(), permanent=True)

    if request.method == 'POST':
        form = Form(request.user, question, request.POST)
        if form.is_valid():
            response = form.save()
            return redirect(question.get_absolute_url())
    else:
        form = Form(request.user, question)

    return render(request, template, {
        'question': question,
        'responses': responses,
        'form': form,
        'categories': Category.objects.all(),
        'BASE': BASE
    })


def knowledge_ask(request,
                  template='django_knowledge/ask.html',
                  Form=QuestionForm,
                  BASE=settings.BASE_TEMPLATE):

    if request.method == 'POST':
        form = Form(request.user, request.POST)
        if form.is_valid():
            question = form.save()
            return redirect(question.get_absolute_url())
    else:
        form = Form(request.user)

    return render(request, template, {
        'form': form,
        'categories': Category.objects.all(),
        'BASE': BASE
    })

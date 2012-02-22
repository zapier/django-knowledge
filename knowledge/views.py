from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, NoReverseMatch
from django.db.models import Q

from knowledge.models import Question, Response, Category
from knowledge.forms import QuestionForm, ResponseForm
from knowledge.utils import paginate
from knowledge import settings

ALLOWED_MODS = {
    'question': [
        'private',
        'public', 'delete',
        'clear_accepted'
    ],
    'response': [
        'internal', 'inherit',
        'private', 'public',
        'delete', 'accept'
    ]
}


def get_my_questions(request):
    if request.user.is_anonymous():
        return None
    else:
        return Question.objects.can_view(request.user)\
                                    .filter(user=request.user)

def knowledge_index(request,
                    template='django_knowledge/index.html'):

    questions = Question.objects.can_view(request.user)[0:20]

    return render(request, template, {
        'request': request,
        'questions': questions,
        'my_questions': get_my_questions(request),
        'categories': Category.objects.all()
    })


def knowledge_list(request,
                   category_slug=None,
                   template='django_knowledge/list.html',
                   Form=QuestionForm):

    search = request.GET.get('title', None)
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
        'my_questions': get_my_questions(request),
        'category': category,
        'categories': Category.objects.all(),
        'form': Form(request.user, initial={'title': search})  # prefill title
    })


def knowledge_thread(request,
                     question_id,
                     slug=None,
                     template='django_knowledge/thread.html',
                     Form=ResponseForm):

    question = get_object_or_404(
        Question.objects.can_view(request.user),
        id=question_id)

    responses = question.get_responses(request.user)

    if request.path != question.get_absolute_url():
        return redirect(question.get_absolute_url(), permanent=True)

    if request.method == 'POST':
        form = Form(request.user, question, request.POST)
        if form and form.is_valid():
            response = form.save()
            return redirect(question.get_absolute_url())
    else:
        form = Form(request.user, question)

    return render(request, template, {
        'request': request,
        'question': question,
        'my_questions': get_my_questions(request),
        'responses': responses,
        'allowed_mods': ALLOWED_MODS,
        'form': form,
        'categories': Category.objects.all()
    })


def knowledge_moderate(
        request,
        lookup_id,
        model,
        mod,
        allowed_mods=ALLOWED_MODS):

    """
    An easy to extend method to moderate questions
    and responses in a vaguely RESTful way.

    Usage:
        /knowledge/moderate/question/1/inherit/     -> 404
        /knowledge/moderate/question/1/public/      -> 200

        /knowledge/moderate/response/3/notreal/     -> 404
        /knowledge/moderate/response/3/inherit/     -> 200

    """

    if model == 'question':
        Model, perm = Question, 'change_question'
    elif model == 'response':
        Model, perm = Response, 'change_response'
    else:
        raise Http404

    if not request.user.has_perm(perm):
        raise Http404

    if mod not in allowed_mods[model]:
        raise Http404

    instance = get_object_or_404(
        Model.objects.can_view(request.user),
        id=lookup_id)

    func = getattr(instance, mod)
    if callable(func):
        func()

    try:
        return redirect((
            instance if instance.is_question else instance.question
        ).get_absolute_url())
    except NoReverseMatch, e:
        # if we delete an instance...
        return redirect(reverse('knowledge_index'))


def knowledge_ask(request,
                  template='django_knowledge/ask.html',
                  Form=QuestionForm):

    if request.method == 'POST':
        form = Form(request.user, request.POST)
        if form and form.is_valid():
            question = form.save()
            return redirect(question.get_absolute_url())
    else:
        form = Form(request.user)

    return render(request, template, {
        'request': request,
        'my_questions': get_my_questions(request),
        'form': form,
        'categories': Category.objects.all()
    })

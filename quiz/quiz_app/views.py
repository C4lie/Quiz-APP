from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Question, QuizResult
from django.contrib.auth.models import User

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_app/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'quiz_app/quiz_detail.html', {'quiz': quiz, 'questions': questions})

from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_app/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'quiz_app/quiz_detail.html', {'quiz': quiz, 'questions': questions})

def quiz_submit(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    score = 0
    total = questions.count()

    if request.method == 'POST':
        for question in questions:
            selected_answer = request.POST.get(f'q{question.id}')
            if selected_answer == question.correct_answer:
                score += 1

    percentage = (score / total) * 100 if total > 0 else 0
    return render(request, 'quiz_app/quiz_result.html', {'quiz': quiz, 'score': score, 'total': total, 'percentage': percentage})


from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .models import Course, Enrollment, Question, Submission


@login_required
def course_details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = course.lesson_set.prefetch_related('questions__choice_set').all().order_by('order')
    return render(
        request,
        'onlinecourse/course_details_bootstrap.html',
        {'course': course, 'lessons': lessons},
    )


@login_required
def submit(request, course_id):
    if request.method != 'POST':
        raise Http404('Only POST is supported for exam submission.')

    course = get_object_or_404(Course, pk=course_id)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)

    selected_choice_ids = []
    for key, value in request.POST.items():
        if key.startswith('question-'):
            selected_choice_ids.extend(request.POST.getlist(key))

    submission = Submission.objects.create(enrollment=enrollment)
    if selected_choice_ids:
        submission.choices.add(*selected_choice_ids)

    return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)


@login_required
def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id, enrollment__course=course)

    selected_choices = submission.choices.select_related('question').all()
    questions = Question.objects.filter(lesson__course=course).distinct()

    total_grade = sum(question.grade for question in questions)
    earned_grade = 0
    correct_choices = []

    for question in questions:
        correct_ids = set(question.choice_set.filter(is_correct=True).values_list('id', flat=True))
        chosen_ids = set(selected_choices.filter(question=question).values_list('id', flat=True))
        if correct_ids == chosen_ids:
            earned_grade += question.grade
        correct_choices.extend(question.choice_set.filter(is_correct=True))

    grade_percent = int((earned_grade / total_grade) * 100) if total_grade else 0

    context = {
        'course': course,
        'submission': submission,
        'grade': grade_percent,
        'earned_grade': earned_grade,
        'total_grade': total_grade,
        'correct_answers': correct_choices,
        'selected_choices': selected_choices,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)

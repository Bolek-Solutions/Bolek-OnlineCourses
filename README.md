# 🛒 Bolek-Shop | Capstone IBM Project

Welcome to **Bolek-Shop**, the comprehensive Capstone full-stack e-commerce application developed for the final IBM certification project. This platform integrates a modern web front-end with a robust Django microservice backend architecture, featuring an innovative automated examination/assessment module that dynamically links educational resources with course metrics.

---

## 🚀 Key Features

* **Modular Course & Assessment Engine:** Built dynamically with strict Django database models enabling programmatic evaluation metrics.
* **Intuitive Nested Stacked Admin Layouts:** Designed to provide administrators with single-pane orchestration over courses, lessons, nested questions, and response keys.
* **Dynamic Grading & Evaluation System:** Evaluates multi-select and single-choice responses via bitwise intersection algorithms, ensuring immediate scoring feedback, margin-of-error protection, and clear success metrics.
* **Production-Grade Bootstrap Theme:** Sleek user dashboards with responsive card grids, fluid multi-step layouts, and immediate accessibility parameters across global break-points.

---

## 📂 Project Structure & Architecture

The application is structured logically to separate backend orchestration, routing architectures, and presentation templates.

```text
Bolek-Shop/
│
├── manage.py                        # Django project orchestration gateway
├── web_project/                     # Core project configuration directory
│   ├── __init__.py
│   ├── settings.py                  # Global configurations and engine hooks
│   ├── urls.py                      # Global URL routing manifest
│   └── wsgi.py
│
└── onlinecourse/                    # Core feature application engine
    ├── admin.py                     # ChoiceInline, QuestionInline, and customized stacked forms
    ├── models.py                    # Database schemas (Course, Lesson, Question, Choice, Submission)
    ├── urls.py                      # Parameterized local endpoint rules
    ├── views.py                     # Controller and analytics grading logic
    └── templates/
        └── onlinecourse/
            ├── course_details_bootstrap.html # Responsive evaluation intake template
            └── exam_result_bootstrap.html    # Contextual KPIs and exam summary dashboard

```

---

## 🛠️ Complete Implementation Deliverables

### 1. Database Specifications (Models)

**File Path:** `onlinecourse/models.py`

```python
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(null=False, max_length=150, default="online course")
    image = models.ImageField(upload_to='course_images/', blank=True)
    description = models.CharField(max_length=1000)
    pub_date = models.DateField(null=False)
    users = models.ManyToManyField(User, through='Enrollment')

    def __str__(self):
        return f"Course: {self.name}"

class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Lesson: {self.title}"

class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [(AUDIT, 'Audit'), (HONOR, 'Honor')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(default=now)
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)
    rating = models.FloatField(default=5.0)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.name}"

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=500, default="Enter assessment question text")
    grade = models.IntegerField(default=1)

    def __str__(self):
        return f"Q: {self.question_text[:50]} (Points: {self.grade})"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Choice: {self.choice_text[:30]} ({'Correct' if self.is_correct else 'Incorrect'})"

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='submissions')
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f"Submission #{self.id} for {self.enrollment.user.username}"

```

### 2. Admin Configurations

**File Path:** `onlinecourse/admin.py`

```python
from django.contrib import admin
from .models import Course, Lesson, Enrollment, Question, Choice, Submission

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'lesson', 'grade')
    search_fields = ['question_text']

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title', 'course', 'order']
    search_fields = ['title']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    search_fields = ['name', 'description']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)

```

### 3. Course Details Assessment Interface

**File Path:** `onlinecourse/templates/onlinecourse/course_details_bootstrap.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ course.name }}</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body class="bg-light">
<div class="container mt-5 mb-5">
    <div class="card shadow-sm border-0 mb-4">
        <div class="card-body bg-primary text-white rounded-top">
            <h1 class="card-title font-weight-bold mb-2">{{ course.name }}</h1>
            <p class="card-text lead">{{ course.description }}</p>
        </div>
    </div>

    <form action="{% url 'onlinecourse:submit' course.id %}" method="post">
        {% csrf_token %}
        {% for lesson in course.lesson_set.all %}
            <div class="card shadow-sm border-0 mb-4">
                <div class="card-header bg-dark text-white font-weight-bold">
                    Lesson {{ forloop.counter }}: {{ lesson.title }}
                </div>
                <div class="card-body bg-white">
                    <p class="text-muted mb-4">{{ lesson.content }}</p>

                    {% if lesson.questions.all %}
                        <h5 class="text-secondary border-bottom pb-2 mb-3">Lesson Assessment</h5>
                        {% for question in lesson.questions.all %}
                            <div class="card mb-3 border-light bg-light">
                                <div class="card-body">
                                    <h6 class="card-title font-weight-bold text-dark">
                                        Q{{ forloop.counter }}: {{ question.question_text }}
                                        <span class="badge badge-info float-right">{{ question.grade }} Points</span>
                                    </h6>
                                    <div class="mt-3">
                                        {% for choice in question.choices.all %}
                                            <div class="custom-control custom-checkbox my-2">
                                                <input type="checkbox" name="choice_{{ choice.id }}" value="{{ choice.id }}" id="choice_{{ choice.id }}" class="custom-control-input">
                                                <label class="custom-control-label text-secondary" for="choice_{{ choice.id }}">
                                                    {{ choice.choice_text }}
                                                </label>
                                            </div>
                                        {% endfor %}
                                    </div>
                                </div>
                            </div>
                        {% endfor %}
                    {% else %}
                        <div class="alert alert-light text-muted py-2 border">No evaluations configured for this lesson.</div>
                    {% endif %}
                </div>
            </div>
        {% empty %}
            <div class="alert alert-warning">No syllabus items loaded for this course profile.</div>
        {% endfor %}

        {% if course.lesson_set.all %}
            <div class="text-right mt-4">
                <button type="submit" class="btn btn-success btn-lg px-5 shadow-sm">Submit Examination</button>
            </div>
        {% endif %}
    </form>
</div>
</body>
</html>

```

### 4. Controller & Examination Analytics Routing (Views)

**File Path:** `onlinecourse/views.py`

```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Lesson, Enrollment, Question, Choice, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment = Enrollment.objects.filter(user=request.user, course=course).first()
    
    if not enrollment:
        enrollment = Enrollment.objects.create(user=request.user, course=course)

    if request.method == 'POST':
        selected_choice_ids = []
        for key, value in request.POST.items():
            if key.startswith('choice_'):
                selected_choice_ids.append(int(value))

        if not selected_choice_ids:
            return HttpResponseRedirect(reverse('onlinecourse:course_details', args=(course.id,)))

        submission = Submission.objects.create(enrollment=enrollment)
        selected_choices = Choice.objects.filter(id__in=selected_choice_ids)
        submission.choices.set(selected_choices)
        submission.save()

        return HttpResponseRedirect(reverse('onlinecourse:show_exam_result', args=(course.id, submission.id)))
    
    return HttpResponseRedirect(reverse('onlinecourse:course_details', args=(course.id,)))

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    total_score = 0
    earned_score = 0
    question_results = []

    lessons = Lesson.objects.filter(course=course)
    questions = Question.objects.filter(lesson__in=lessons)

    for question in questions:
        total_score += question.grade
        all_choices = question.choices.all()
        correct_choices = all_choices.filter(is_correct=True)
        user_choices = submission.choices.filter(question=question)
        
        correct_ids = set(correct_choices.values_list('id', flat=True))
        user_ids = set(user_choices.values_list('id', flat=True))
        
        is_question_correct = (correct_ids == user_ids) and len(correct_ids) > 0
        
        if is_question_correct:
            earned_score += question.grade

        question_results.append({
            'question': question,
            'all_choices': all_choices,
            'user_choices': user_choices,
            'correct_choices': correct_choices,
            'is_correct': is_question_correct
        })

    percentage = (earned_score / total_score) * 100 if total_score > 0 else 0
    passed = percentage >= 80

    context = {
        'course': course,
        'submission': submission,
        'earned_score': earned_score,
        'total_score': total_score,
        'percentage': round(percentage, 1),
        'passed': passed,
        'question_results': question_results
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)

```

### 5. Routing Profiles (URLs)

**File Path:** `onlinecourse/urls.py`

```python
from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]

```

### 6. Post-Examination Analytics Dashboard

**File Path:** `onlinecourse/templates/onlinecourse/exam_result_bootstrap.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Examination Summary - {{ course.name }}</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body class="bg-light">
<div class="container mt-5 mb-5">
    
    {% if passed %}
        <div class="alert alert-success shadow-sm rounded border-0 p-4 mb-4" role="alert">
            <h2 class="alert-heading font-weight-bold">🎉 Congratulations!</h2>
            <p class="lead mb-0">You have successfully met all assessment scoring criteria guidelines for this module.</p>
        </div>
    {% else %}
        <div class="alert alert-danger shadow-sm rounded border-0 p-4 mb-4" role="alert">
            <h2 class="alert-heading font-weight-bold">Review Required</h2>
            <p class="lead mb-0">Your final grade is below the 80% passing benchmark standard. Please audit your results and try again.</p>
        </div>
    {% endif %}

    <div class="card shadow-sm border-0 mb-4">
        <div class="card-header bg-dark text-white font-weight-bold">Performance Breakdown Metrics</div>
        <div class="card-body">
            <div class="row text-center">
                <div class="col-md-4 border-right">
                    <small class="text-muted font-weight-bold tracking-wide">FINAL SCORE</small>
                    <h2 class="font-weight-bold {% if passed %}text-success{% else %}text-danger{% endif %}">{{ percentage }}%</h2>
                </div>
                <div class="col-md-4 border-right">
                    <small class="text-muted font-weight-bold tracking-wide">WEIGHTED VALUE</small>
                    <h2 class="font-weight-bold text-dark">{{ earned_score }} / {{ total_score }} Pts</h2>
                </div>
                <div class="col-md-4">
                    <small class="text-muted font-weight-bold tracking-wide">COMPLIANCE STATUS</small>
                    <h2 class="font-weight-bold">{% if passed %}<span class="badge badge-success">PASSED</span>{% else %}<span class="badge badge-danger">FAILED</span>{% endif %}</h2>
                </div>
            </div>
        </div>
    </div>

    <h4 class="text-secondary font-weight-bold mb-3">Granular Answer Evaluation</h4>
    {% for res in question_results %}
        <div class="card shadow-sm border-0 mb-3">
            <div class="card-header bg-white font-weight-bold d-flex justify-content-between align-items-center">
                <span>{{ res.question.question_text }}</span>
                {% if res.is_correct %}
                    <span class="badge badge-success px-3 py-2">Correct (+{{ res.question.grade }} Pts)</span>
                {% else %}
                    <span class="badge badge-danger px-3 py-2">Incorrect (0 / {{ res.question.grade }} Pts)</span>
                {% endif %}
            </div>
            <div class="card-body bg-white pt-0">
                <ul class="list-group list-group-flush mt-2">
                    {% for choice in res.all_choices %}
                        <li class="list-group-item d-flex justify-content-between align-items-center bg-light my-1 rounded border-0">
                            <div>
                                {% if choice in res.user_choices %}
                                    <span class="badge badge-primary mr-2">Your Answer</span>
                                {% endif %}
                                {{ choice.choice_text }}
                            </div>
                            <div>
                                {% if choice.is_correct %}
                                    <span class="badge badge-success">Correct Choice</span>
                                {% elif choice in res.user_choices and not choice.is_correct %}
                                    <span class="badge badge-danger">Incorrect Option Selected</span>
                                {% endif %}
                            </div>
                        </li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    {% endfor %}

    <div class="mt-4">
        <a href="{% url 'onlinecourse:course_details' course.id %}" class="btn btn-outline-primary shadow-sm">Back to Course Dashboard</a>
    </div>
</div>
</body>
</html>

```

---

## 🛠️ Deployment & Execution Commands

### Schema Compilation & Migration Pipelines

Generate the structural migration profiles and apply them directly against your target active storage database engine:

```bash
python manage.py makemigrations onlinecourse
python manage.py migrate

```

### Local Application Execution

Initialize your development runtime application loop locally using:

```bash
python manage.py runserver

```

The ecosystem will compile and deploy at `[http://127.0.0.1:8000/](http://127.0.0.1:8000/)`.

### Production Source Version Management

Log deployment layers, secure file branches, and push codebase deltas up to remote Git origins:

```bash
git add .
git commit -m "Completed final assessment feature"
git push

```

---

## 🧪 Admin Dashboard Population & End-to-End Testing

To manually seed testing data configurations and verify grading features, complete the following steps:

1. **Launch Django Control Panel:** Run the server application and log into the core admin view via `[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)` using superuser credentials. *(If required, run `python manage.py createsuperuser` via terminal commands).*
2. **Configure Baseline Course Material:** Click into **Courses** and initialize a primary parent testing block (e.g., *"Cloud Dev-Ops Architecture"*). Save the form.
3. **Seed Syllabus and Evaluation Metrics:** Navigate into the **Lessons** panel and click **Add Lesson**. Connect the entity to your active Course layer.
4. **Build Questions and Multiple Choices:** Within the stacked admin forms, populate assessment questions into the integrated **Questions** inline section. For every question block, add possible multiple-choice configurations underneath.
5. **Set Answer Keys:** Explicitly check the **Is Correct** parameter switch exclusively on valid true choice items, leaving invalid distractors unchecked. Click **Save**.
6. **Execute End-to-End End User Validation:** Return to the student dashboard view, load your newly populated learning module page, toggle mixed target answer criteria configurations, and hit **Submit Examination**. Confirm that the grading view properly tabulates results, renders dynamic context-driven success alerts, and itemizes metrics cleanly.

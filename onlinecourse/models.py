from django.contrib.auth.models import User
from django.db import models


class Instructor(models.Model):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField(default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ',' + self.user.last_name


class Learner(models.Model):
    occupation = models.CharField(max_length=200, blank=False)
    social_link = models.URLField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ',' + self.user.last_name


class Course(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='course_images/')
    description = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    users = models.ManyToManyField(User, through='Enrollment')
    total_enrollment = models.IntegerField(default=0)
    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)
    mode = models.CharField(max_length=5, default='audit')
    rating = models.FloatField(default=5.0)

    def __str__(self):
        return f'{self.user.username} enrolled in {self.course.name}'


class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=500)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text

    def is_get_score(self, selected_choice_ids):
        all_answers = self.choice_set.filter(is_correct=True).values_list('id', flat=True)
        return set(all_answers) == set(selected_choice_ids)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f'Submission #{self.id} for {self.enrollment}'

    def calculate_score(self):
        total_score = 0
        selected_choices = self.choices.all()
        questions = Question.objects.filter(choice__in=selected_choices).distinct()

        for question in questions:
            selected_ids = selected_choices.filter(question=question).values_list('id', flat=True)
            if question.is_get_score(selected_ids):
                total_score += question.grade

        return total_score

from django.contrib import admin

from .models import Choice, Course, Enrollment, Instructor, Learner, Lesson, Question, Submission


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'lesson', 'grade')


class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'course', 'order')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date', 'total_enrollment')
    search_fields = ('name',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment)
admin.site.register(Submission)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)

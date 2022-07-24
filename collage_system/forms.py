from dataclasses import fields
from django import forms
from django.forms import ClearableFileInput
from .models import (
    Student,
    SuggAndComp,
    Courses,
    Courses_files,
    Teacher,
    TutorialsTeacher,
    TutorialsVideos,
    Activities,
    Tutorials,
    Program,
)
from django.contrib.auth.models import User


class create_course(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ["course_name", "major", "level", "semester", "Course_image"]


class add_files(forms.ModelForm):
    class Meta:
        model = Courses_files
        fields = ["lecture_url", "course", "teacher"]
        widgets = {
            "lecture_url": ClearableFileInput(attrs={"multiple": True}),
        }


class add_teacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
        exclude = ["user", "slug"]


class add_tutorial_teacher(forms.ModelForm):
    class Meta:
        model = TutorialsTeacher
        fields = "__all__"
        exclude = ["user", "slug"]


class add_tutorial_video(forms.ModelForm):
    class Meta:
        model = TutorialsVideos
        fields = ["video", "tutorialsteacher"]
        widgets = {
            "video": ClearableFileInput(attrs={"multiple": True}),
        }


class add_activity(forms.ModelForm):
    class Meta:
        model = Activities
        fields = "__all__"


class add_tutorial(forms.ModelForm):
    class Meta:
        model = Tutorials
        fields = "__all__"


class edit_profile(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "course",
        ]


class edit_user(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
        ]


class add_suggestion(forms.ModelForm):
    class Meta:
        model = SuggAndComp
        fields = "__all__"
        exclude = [
            "pub_date",
        ]


class add_student(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ["user", "teacher"]


class edit_student(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        exclude = [
            "user",
        ]


class add_program(forms.ModelForm):
    class Meta:
        model = Program
        fields = "__all__"
        exclude = [
            "pub_date",
        ]

from django.contrib import admin
from .models import Student,Major,Program,Level,Courses,SuggAndComp,Courses_files,Semester,Activities,Teacher,Tutorials,TutorialsTeacher,TutorialsVideos
# Register your models here.
admin.site.register(Major)
admin.site.register(Level)
admin.site.register(Courses)
admin.site.register(Courses_files)
admin.site.register(Semester)
admin.site.register(Activities)
admin.site.register(Teacher)
admin.site.register(Tutorials)
admin.site.register(TutorialsTeacher)
admin.site.register(TutorialsVideos)
admin.site.register(SuggAndComp)
admin.site.register(Program)
admin.site.register(Student)




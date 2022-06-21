import django_filters
from .models import Courses,TutorialsTeacher,Program
class courses_filter(django_filters.FilterSet):
    course_containe=django_filters.CharFilter(field_name='course_name',lookup_expr='icontains')
    class Meta:
        model=Courses
        fields=['course_name',]
class Tutorial_filter(django_filters.FilterSet):
    tutorial_containe = django_filters.CharFilter(field_name='tutorials_name', lookup_expr='icontains')
    class Meta:
        model=TutorialsTeacher
        fields=['tutorials_name',]

class Program_filter(django_filters.FilterSet):
    program_containe = django_filters.CharFilter(field_name='program_name', lookup_expr='icontains')
    class Meta:
        model=Program
        fields=['program_name',]
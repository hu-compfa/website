from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("major/", views.major_page, name="major"),
    path("<str:m_name>/levels/", views.level_page, name="levels"),
    path("<str:m_name>/<int:level>/semester/", views.semester_page, name="semester"),
    path(
        "<str:m_name>/<int:level>/<str:s_name>/courses/",
        views.courses_page,
        name="courses",
    ),
    path(
        "<str:m_name>/<int:level>/<str:s_name>/<str:c_name>/teacher/",
        views.teacher_page,
        name="teacher",
    ),
    path(
        "<str:m_name>/<int:level>/<str:s_name>/<str:c_name>/<str:t_name>/files/",
        views.courses_file_page,
        name="files",
    ),
    path("add/", views.add_page_for_teacher, name="add"),
    path("control/", views.add_page_for_control, name="control"),
    path("activities/", views.activities_page, name="activities"),
    path("tutorials/", views.tutorials_page, name="tutorials"),
    path(
        "tutorials/<str:tutorials_name>/",
        views.tutorial_teacher_page,
        name="tutorials_teacher",
    ),
    path(
        "tutorials/<str:tutorials_name>/<str:tutorial_course_name>/",
        views.tutorial_redirect_page,
        name="tutorials_redirect_page",
    ),
    path(
        "tutorials/<str:tutorials_name>/<str:tutorial_course_name>/<str:video_name>/",
        views.tutorial_video_page,
        name="tutorials_video_page",
    ),
    path("logout/", views.logoutpage, name="logout"),
    path("profile/", views.profile_page, name="profile"),
    path("delete_file/<int:file_id>/", views.delete_file, name="delete"),
    path("edit_profile/", views.edit_profile_page, name="edit_profile"),
    path("suggandcomp/", views.suggandcomp, name="suggandcomp"),
    path(
        "delete_sugg_comp/<int:sugg_id>/",
        views.delete_suggandcomp,
        name="delete_suggandcomp",
    ),
    path("programs/", views.program_page, name="program_page"),
    path("load_courses/", views.load_courses, name="load_courses"),
]

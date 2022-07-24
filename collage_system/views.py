from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import (
    Program,
    Major,
    SuggAndComp,
    Level,
    Courses,
    Courses_files,
    Semester,
    Activities,
    Teacher,
    Tutorials,
    TutorialsTeacher,
    TutorialsVideos,
)
from .forms import (
    add_program,
    edit_student,
    add_student,
    add_suggestion,
    create_course,
    add_files,
    add_teacher,
    add_tutorial_teacher,
    add_tutorial_video,
    add_activity,
    add_tutorial,
    edit_profile,
    edit_user,
)
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user
from .filters import courses_filter, Tutorial_filter, Program_filter
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

# Create your views here.
# start  major page
def home(request):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, "Username OR Password incorrect")
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    all_courses = Courses.objects.all()
    filter_courses = courses_filter(request.GET, all_courses)
    if filter_courses.qs.count() < all_courses.count():
        head = "Search Result :"
    else:
        head = "Home "
    context = {
        "title": "home",
        "head": head,
        "nav_path": f"/",
        "all_courses": Courses.objects.all(),
        "filter": filter_courses,
    }
    return render(request, "collage_system/home.html", context)


def major_page(request):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, "Username OR Password incorrect")
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    majors = Major.objects.all()
    courses = Courses.objects.all()
    filter = courses_filter(request.GET, courses)
    if filter.qs.count() < courses.count():
        head = "Search Result :"
    else:
        head = "Choose your Major "
    context = {
        "title": "choose yor major",
        "majors": majors,
        "filter": filter,
        "courses": courses,
        "head": head,
        "nav_path": f"/major/",
    }
    return render(request, "collage_system/major.html", context)


# end major page
# start level page
def level_page(request, m_name):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, "Username OR Password incorrect")
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    head = "Choose Your Level "
    major = get_object_or_404(Major, slug=m_name.replace(" ", "-"))
    levels = Level.objects.all()
    context = {
        "title": "Choose your level",
        "levels": levels,
        "major": major.slug,
        "head": head,
        "nav_path": f"/major/",
    }
    return render(request, "collage_system/level_page.html", context)


# end level page
def semester_page(request, m_name, level):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, "Username OR Password incorrect")
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    head = "Choose your Semester "
    major = get_object_or_404(Major, slug=m_name.replace(" ", "-"))
    level = get_object_or_404(Level, level=level)
    semesters = Semester.objects.all()
    context = {
        "title": "Choose your semester",
        "nav_path": f"/major/",
        "semesters": semesters,
        "level": level.level,
        "major": major.slug,
        "head": head,
    }
    return render(request, "collage_system/semester.html", context)


# start courses page
def courses_page(request, m_name, level, s_name):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, "Username OR Password incorrect")
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    head = "Choose your Course "
    major = get_object_or_404(Major, slug=m_name.replace(" ", "-"))
    level = get_object_or_404(Level, level=level)
    semester = get_object_or_404(Semester, semester=s_name)
    courses = Courses.objects.filter(level=level, major=major, semester=semester)
    context = {
        "title": "Choose course",
        "courses": courses,
        "major": major.slug,
        "level": level.level,
        "semester": semester.semester,
        "head": head,
        "nav_path": f"/major/",
    }
    return render(request, "collage_system/courses_page.html", context)


# end courses page
# start teacher page
def teacher_page(request, m_name, level, s_name, c_name):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, "Username OR Password incorrect")
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    head = "Choose your Teacher "
    major = get_object_or_404(Major, slug=m_name.replace(" ", "-"))
    level = get_object_or_404(Level, level=level)
    semester = get_object_or_404(Semester, semester=s_name)
    course = get_object_or_404(Courses, slug=c_name.replace(" ", "-"))
    teachers = []
    for teacher in course.teacher_set.all():
        if (
            teacher.course.get(course_name=course.course_name).courses_files_set.count()
            != 0
        ):
            teachers.append(teacher)
        else:
            continue

    context = {
        "title": "choose teacher",
        "teachers": teachers,
        "major": major.slug,
        "level": level.level,
        "semester": semester.semester,
        "course": course.slug,
        "head": head,
        "nav_path": f"/major/",
    }
    return render(request, "collage_system/teacher_page.html", context)


# end teacher page

# start course_file page
def courses_file_page(request, m_name, level, s_name, c_name, t_name):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, "Username OR Password incorrect")
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    head = "Choose your major "
    major = get_object_or_404(Major, slug=m_name.replace(" ", "-"))
    level = get_object_or_404(Level, level=level)
    semester = get_object_or_404(Semester, semester=s_name)
    course = get_object_or_404(
        Courses,
        slug=c_name.replace(" ", "-"),
        major__major_name=major.major_name,
        level__level=level.level,
    )
    teacher = get_object_or_404(Teacher, slug=t_name.replace(" ", "-"))
    course_file = teacher.courses_files_set.filter(course=course)
    context = {
        "title": "download files",
        "files": course_file,
        "head": head,
        "nav_path": f"/major/",
    }
    return render(request, "collage_system/files_page.html", context)


# end course_file page
# start add page for teacher
@login_required(login_url="home")
@allowed_user(allowed_roles=["teacher"])
def add_page_for_teacher(request):
    if request.method == "POST":
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    lecture_form = add_files()
    if request.method == "POST":
        if "lecture" in request.POST:
            lecture_form = add_files(request.POST, request.FILES)
            course = request.POST.get("course")
            teacher = request.user.teacher
            lectures = request.FILES.getlist("lecture_url")
            if lecture_form.is_valid():
                teacher_have = ""
                for lecture in lectures:
                    if teacher.courses_files_set.filter(lecture_name=lecture):
                        teacher_have += "  " + lecture.name
                if len(teacher_have) > 0:
                    messages.warning(request, f"{teacher_have} are upload")
                    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
                elif Courses.objects.get(id=course) in teacher.course.all():
                    for file in lectures:
                        form = Courses_files(
                            lecture_url=file, course_id=course, teacher_id=teacher.id
                        )
                        form.save()
                    messages.success(request, "Add lecture/s successful")
                    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
                else:
                    teacher.course.add(Courses.objects.get(id=course))
                    for file in lectures:
                        form = Courses_files(
                            lecture_url=file, course_id=course, teacher_id=teacher.id
                        )
                        form.save()
                    messages.success(request, "Add lecture/s successful")
                    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, lecture_form.errors)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    context = {
        "title": "Add page",
        "lecture_form": lecture_form,
        "courses": Courses.objects.all(),
        "levels": Level.objects.all(),
        # 'teacher':request.user.teacher,
        "nav_path": f"/add/",
    }
    return render(request, "collage_system/add_page_for_teacher.html", context)


# end add page for teacher
# start add page for control
@login_required(login_url="home")
@allowed_user(allowed_roles=["admin"])
def add_page_for_control(request):
    video_form = add_tutorial_video()
    lecture_form = add_files()
    tutorial_teacher_form = add_tutorial_teacher()
    course_form = create_course()
    tutorial_form = add_tutorial()
    teacher_form = add_teacher()
    activity_form = add_activity()
    student_form = add_student()
    if request.method == "POST":
        if "register_student" in request.POST:
            student_form = add_student(request.POST)
            username = request.POST.get("username")
            user_creation_form = UserCreationForm(request.POST)
            if student_form.is_valid() and user_creation_form.is_valid():
                print("hh")
                form = student_form.save(commit=False)
                user_creation_form.save()
                user = User.objects.get(username=username)
                form.user = user
                form.save()
                student_form.save_m2m()
                group = Group.objects.get(name="teacher")
                user.groups.add(group)
                messages.success(request, "Register student successful")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                print("bb")
                messages.warning(
                    request, user_creation_form.errors, student_form.errors
                )
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        if "delete_activity" in request.POST:
            activity = request.POST.get("activity")
            activity = Activities.objects.get(id=activity)
            activity_name = activity.activitie_name
            activity.delete()
            messages.success(request, f"Delete {activity_name} successful")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        if "delete_course" in request.POST:
            course = request.POST.get("course")
            course = Courses.objects.get(id=course)
            course_name = course.course_name
            course.delete()
            messages.success(request, f"Delete {course_name} successful")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        if "delete_teacher" in request.POST:
            teacher = request.POST.get("teacher")
            teacher = Teacher.objects.get(id=teacher)
            teacher_name = teacher.teacher_name
            teacher.delete()
            messages.success(request, f"Delete {teacher_name} successful")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        if "teacher_form" in request.POST:
            teacher_form = add_teacher(request.POST, request.FILES)
            if teacher_form.is_valid():
                teacher_form.save()
                messages.success(request, "Add teacher successful ")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, teacher_form.errors)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        if "course_form" in request.POST:
            course_form = create_course(request.POST, request.FILES)
            if course_form.is_valid():
                course_form.save()
                messages.success(request, "Add course successful")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, course_form.errors)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        if "tutorial_form" in request.POST:
            tutorial_form = add_tutorial(request.POST, request.FILES)
            if tutorial_form.is_valid():
                tutorial_form.save()
                messages.success(request, "tutorials successful")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, tutorial_form.errors)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        if "program_form" in request.POST:
            program_form = add_program(request.POST, request.FILES)
            if program_form.is_valid():
                program_form.save()
                messages.success(request, "program successful")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        if "activity_form" in request.POST:
            activity_form = add_activity(request.POST, request.FILES)
            if activity_form.is_valid():
                activity_form.save()
                messages.success(request, "Add activity successful")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, activity_form.errors)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        if "tutorial_trainer" in request.POST:
            videos = request.FILES.getlist("video")
            tutorial_name = request.POST.get("tutorials_name")
            tutorial_form = add_tutorial_teacher(request.POST, request.FILES)
            if tutorial_form.is_valid():
                tutorial_form.save()
                tutorial = TutorialsTeacher.objects.get(tutorials_name=tutorial_name)
                for video in videos:
                    form = TutorialsVideos(video=video, tutorialsteacher_id=tutorial.id)
                    form.save()
                messages.success(request, "Add trainer successful")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, tutorial_form.errors)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        if "tutorial_video" in request.POST:
            video_form = add_tutorial_video(request.POST, request.FILES)
            videos = request.FILES.getlist("video")
            tutorial = request.POST.get("tutorialsteacher")
            if video_form.is_valid():
                for video in videos:
                    form = TutorialsVideos(video=video, tutorialsteacher_id=tutorial)
                    form.save()
                messages.success(request, "Add video/s successful")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, video_form.errors)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        if "add_lecture" in request.POST:
            lecture_form = add_files(request.POST, request.FILES)
            course = request.POST.get("course")
            teacher = request.POST.get("teacher")
            lectures = request.FILES.getlist("lecture_url")
            if lecture_form.is_valid():
                for file in lectures:
                    form = Courses_files(
                        lecture_url=file, course_id=course, teacher_id=teacher
                    )
                    form.save()
                messages.success(request, "Add lecture/s successful")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, lecture_form.errors)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    context = {
        "title": "Add page",
        "tutorial_teacher_form": tutorial_teacher_form,
        "lecture_form": lecture_form,
        "tutorial_form": tutorial_form,
        "course_form": course_form,
        "teacher_form": teacher_form,
        "video_form": video_form,
        "activity_form": activity_form,
        "student_form": student_form,
        "majors": Major.objects.all(),
        "levels": Level.objects.all(),
        "semesters": Semester.objects.all(),
        "teachers": Teacher.objects.all(),
        "courses": Courses.objects.all(),
        "Tutorials": Tutorials.objects.all(),
        "tutorial_teacher": TutorialsTeacher.objects.all(),
        "activities": Activities.objects.all(),
        "nav_path": f"/control/",
    }
    return render(request, "collage_system/add_page_for_control.html", context)


# end add page for control
def activities_page(request):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, "Username OR Password incorrect")
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            messages.warning(request, "Username OR Password incorrect")
    head = "Activities & News "
    context = {
        "title": "activities",
        "activities": Activities.objects.all(),
        "head": head,
        "nav_path": f"/activities/",
    }
    return render(request, "collage_system/activities_page.html", context)


# star tutorials page
def tutorials_page(request):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, "Username OR Password incorrect")
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    Tutorial = TutorialsTeacher.objects.all()
    filter = Tutorial_filter(request.GET, Tutorial)
    if filter.qs.count() < Tutorial.count():
        head = "Search Result :"
    else:
        head = "Tutorials"
    context = {
        "title": "Tutorials",
        "tutorials": Tutorials.objects.all(),
        "filter": filter,
        "head": head,
        "TutorialsTeacher": Tutorial,
        "nav_path": f"/tutorials/",
    }
    return render(request, "collage_system/tutorials.html", context)


# end tutorials page
# star tutorial Teachers page
def tutorial_teacher_page(request, tutorials_name):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, "Username OR Password incorrect")
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    tutorial = get_object_or_404(Tutorials, tutorials_name=tutorials_name)
    head = "Tutorial Trainers "
    context = {
        "title": "Tutorials",
        "tutorials_teacher": tutorial.tutorialsteacher_set.all(),
        "head": head,
        "nav_path": f"/tutorials/",
    }
    return render(request, "collage_system/tutorial_teacher.html", context)


# end tutorial Teachers page
# start tutorial rediect page
def tutorial_redirect_page(request, tutorials_name, tutorial_course_name):
    tutorial = get_object_or_404(Tutorials, tutorials_name=tutorials_name)
    tutorial_course = get_object_or_404(
        TutorialsTeacher, slug=tutorial_course_name.replace(" ", "-")
    )
    video = tutorial_course.tutorialsvideos_set.first()
    return redirect(
        "tutorials_video_page", tutorials_name, tutorial_course_name, video.slug
    )


# end tutorial rediect page
# start tutorial video page
def tutorial_video_page(request, tutorials_name, tutorial_course_name, video_name):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, "Username OR Password incorrect")
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    tutorial = get_object_or_404(Tutorials, tutorials_name=tutorials_name)
    tutorial_course = get_object_or_404(
        TutorialsTeacher, slug=tutorial_course_name.replace(" ", "-")
    )
    the_video = get_object_or_404(TutorialsVideos, slug=video_name)
    # start control the next and previous button
    videos_numbers = len(tutorial_course.tutorialsvideos_set.all())
    the_previous = None
    the_next = None
    if videos_numbers == 1:
        pass
    elif the_video == tutorial_course.tutorialsvideos_set.first():
        the_next = tutorial_course.tutorialsvideos_set.all()[1]
    elif the_video == tutorial_course.tutorialsvideos_set.last():
        the_previous = tutorial_course.tutorialsvideos_set.all()[videos_numbers - 2]
    else:
        for video in range(videos_numbers):
            if tutorial_course.tutorialsvideos_set.all()[video] == the_video:
                the_next = tutorial_course.tutorialsvideos_set.all()[video + 1]
                the_previous = tutorial_course.tutorialsvideos_set.all()[video - 1]
    # end control the next and previous button
    current_video = redirect(
        "tutorials_video_page",
        tutorials_name,
        tutorial_course_name,
        video_name.replace(" ", "-"),
    ).url
    head = "Tutorials Teacher "
    context = {
        "title": "Tutorials",
        "video": the_video,
        "current_video": current_video,
        "the_previous": the_previous,
        "the_next": the_next,
        "tutorials_video": tutorial_course.tutorialsvideos_set.all(),
        "head": head,
        "nav_path": f"/tutorials/",
    }

    return render(request, "collage_system/tutorials_video.html", context)


# end tutorial video page
# start logout page
@login_required(login_url="login")
def logoutpage(request):
    logout(request)
    return redirect("home")


# end logout page
@login_required(login_url="home")
@allowed_user(allowed_roles=["teacher"])
def profile_page(request):
    if request.method == "POST":
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    context = {
        "title": "profile",
        "head": f"{request.user.username}",
        "lectures": request.user.teacher.courses_files_set.all(),
    }
    return render(request, "collage_system/profile_page.html", context)


@login_required(login_url="home")
def delete_file(request, file_id):
    file = get_object_or_404(Courses_files, id=file_id)
    file.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required(login_url="home")
@allowed_user(allowed_roles=["teacher"])
def edit_profile_page(request):
    update_user = edit_user(instance=request.user)
    update_profile = edit_student(instance=request.user.teacher)
    change_password = PasswordChangeForm(request.user)
    if request.method == "POST":
        if "edit_profile" in request.POST:
            update_user = edit_user(request.POST, instance=request.user)
            # update_profile = edit_teacher(request.POST,instance=request.user.student)
            if update_user.is_valid():
                update_user.save()
                messages.success(request, "Edit profile successful ")
                return redirect("profile")
            else:
                messages.warning(request, "Something went wrong ")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        if "change_password" in request.POST:
            change_password = PasswordChangeForm(request.user, request.POST)
            if change_password.is_valid():
                user = change_password.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Change password successful ")
                return redirect("logout")
            else:
                messages.warning(request, "Something went wrong ")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    context = {
        "title": "edit profile",
        "user_form": update_user,
        "profile_form": update_profile,
        "change_password": change_password,
        "teachers": Teacher.objects.all(),
    }
    return render(request, "collage_system/edit_profile.html", context)


@login_required(login_url="home")
@allowed_user(allowed_roles=["admin"])
def suggandcomp(request):
    all_suggandcomp = SuggAndComp.objects.all()
    context = {
        "title": "suggestions/complaints",
        "head": "Suggestions/Complaints",
        "suggestions": all_suggandcomp,
        "nav_path": f"/suggandcomp/",
    }
    return render(request, "collage_system/suggstion.html", context)


@login_required(login_url="home")
@allowed_user(allowed_roles=["admin"])
def delete_suggandcomp(request, sugg_id):
    suggandcomp = get_object_or_404(SuggAndComp, id=sugg_id)
    suggandcomp.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def program_page(request):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            else:
                messages.warning(request, "Username OR Password incorrect")
        if "suggestion_form" in request.POST:
            suggestion_form = add_suggestion(request.POST)
            if suggestion_form.is_valid():
                suggestion_form.save()
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    programs = Program.objects.all()
    filter_program = Program_filter(request.GET, programs)
    if filter_program.qs.count() < programs.count():
        head = "Search Result :"
    else:
        head = "Programs "
    context = {
        "title": "Programs",
        "head": head,
        "filter": filter_program,
        "nav_path": "/programs/",
    }
    return render(request, "collage_system/programs_page.html", context)


def load_courses(request):
    le_id = request.GET.get("key")
    courses = Courses.objects.filter(level_id=le_id)
    return render(request, "collage_system/load_courses.html", {"courses": courses})

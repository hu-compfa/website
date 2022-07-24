from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import timeago
import datetime
import random

# Create your models here
class Major(models.Model):
    major_name = models.CharField(max_length=100)
    major_image = models.ImageField(upload_to="major_pic", null=True)
    slug = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ["-major_name"]

    def __str__(self):
        return self.major_name

    def save(self, *args, **kwargs):
        self.slug = "".join(
            [char for char in self.major_name if char.isupper()]
        ).lower()
        return super(Major, self).save(*args, **kwargs)


class Level(models.Model):
    level = models.IntegerField()
    level_image = models.ImageField(upload_to="major_pic", null=True)

    def __str__(self):
        return f"level {self.level}"


class Semester(models.Model):
    semester = models.CharField(max_length=20)
    semester_image = models.ImageField(upload_to="major_pic", null=True)

    def __str__(self):
        return f"{self.semester}"


class Courses(models.Model):
    course_name = models.CharField(max_length=200)
    major = models.ManyToManyField(Major)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    Course_image = models.ImageField(upload_to="images", null=True)
    slug = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["course_name"]

    def __str__(self):
        return self.course_name

    def save(self, *args, **kwargs):
        self.slug = self.course_name.replace(" ", "-")
        return super(Courses, self).save(*args, **kwargs)


class Activities(models.Model):
    activitie_name = models.CharField(max_length=50)
    activitie_disc = models.TextField(null=True)
    activitie_image = models.ImageField(upload_to="Activities")
    activitie_create_date = models.DateTimeField(
        default=datetime.datetime.now, null=True, blank=True
    )
    activitie_image1 = models.ImageField(upload_to="Activities", null=True, blank=True)
    activitie_image2 = models.ImageField(upload_to="Activities", null=True, blank=True)

    class Meta:
        ordering = ["-activitie_create_date"]

    def save(self, *args, **kwargs):
        super(Activities, self).save(*args, **kwargs)

        def resize_image(pic):
            img = Image.open(pic.path)
            if img.width > 400 or img.height > 400:
                output_size = 400, 400
                img.thumbnail(output_size)
                img.save(pic.path)

        resize_image(self.activitie_image)
        if self.activitie_image1 != None:
            resize_image(self.activitie_image1)
        if self.activitie_image2 != None:
            resize_image(self.activitie_image2)

    @property
    def get_time_ago(self):
        pub_date = self.activitie_create_date
        now = datetime.datetime.now()
        print(type(pub_date), "\n", now)
        time_ago = timeago.format(pub_date, now, "ar")
        return f"{time_ago}"

    def __str__(self):
        return self.activitie_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200)
    course = models.ManyToManyField(Courses)
    teacher_image = models.ImageField(upload_to="teacher", null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.teacher_name}"

    def save(self, *args, **kwargs):
        self.slug = self.teacher_name.replace(" ", "-")
        return super(Teacher, self).save(*args, **kwargs)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher)


class Courses_files(models.Model):
    lecture_url = models.FileField(upload_to="Lectures")
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, null=True, blank=True
    )
    lecture_name = models.CharField(null=True, blank=True, max_length=50)
    add_date = models.DateTimeField(default=datetime.datetime.now)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        ordering = ["-add_date"]

    def __str__(self):
        return f"{self.course.course_name}:{self.lecture_name}"

    def save(self, *args, **kwargs):
        self.lecture_name = self.lecture_url.name
        super(Courses_files, self).save(*args, **kwargs)


class Tutorials(models.Model):
    tutorials_name = models.CharField(max_length=50)
    tutorials_image = models.ImageField(upload_to="tutorials", null=True)

    def __str__(self):
        return self.tutorials_name


class TutorialsTeacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    tutorials_image = models.ImageField(
        null=True, blank=True, upload_to="TutorialsTeacher"
    )
    tutorials_name = models.CharField(max_length=300)
    slug = models.CharField(max_length=300, null=True, blank=True)
    tutorials = models.ForeignKey(Tutorials, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.slug}"

    def save(self, *args, **kwargs):
        self.slug = (
            f"{self.tutorials_name.replace(' ','-')}-{random.randint(10000,99999)}"
        )
        super(TutorialsTeacher, self).save(*args, **kwargs)
        img = Image.open(self.tutorials_image.path)
        if img.width > 200 or img.height > 200:
            output_size = 200, 200
            img.thumbnail(output_size)
            img.save(self.tutorials_image.path)


class TutorialsVideos(models.Model):
    video = models.FileField(upload_to="VideoTutorials0000000000000")
    video_name = models.CharField(max_length=300, null=True, blank=True)
    slug = models.CharField(max_length=300, null=True, blank=True)
    tutorialsteacher = models.ForeignKey(TutorialsTeacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.video_name} {self.tutorialsteacher.teacher_name}"

    def save(self, *args, **kwargs):
        VideoName = self.video.name
        for char in range(len(VideoName) - 1, 0, -1):
            if VideoName[char] == ".":
                VideoName = VideoName[:char]
                break
        self.slug = f"{VideoName.replace(' ','-')}-{random.randint(10000,99999)}"
        self.video_name = f"{VideoName}"
        return super(TutorialsVideos, self).save(*args, **kwargs)


class SuggAndComp(models.Model):
    proposal = models.CharField(max_length=30)
    sugg_dics = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = [
            "-pub_date",
        ]

    def __str__(self):
        return f'{self.proposal}'

    @property
    def get_time_ago(self):
        pub_date = self.pub_date
        now = datetime.datetime.now()
        time_ago = timeago.format(pub_date, now, "ar")
        return f"{time_ago}"


class Program(models.Model):
    program_file = models.FileField(upload_to="programs")
    program_name = models.CharField(max_length=100, blank=True, null=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.program_name

    def save(self, *args, **kwargs):
        ProgramName = self.program_file.name
        for char in range(len(ProgramName) - 1, 0, -1):
            if ProgramName[char] == ".":
                ProgramName = ProgramName[:char]
                break
        self.program_name = ProgramName
        return super(Program, self).save(*args, **kwargs)

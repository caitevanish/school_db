from django.db import models

# Create your models here.

class Instructor(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    hire_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    year = models.IntegerField(default=9)
    gpa = models.FloatField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Course(models.Model):
    name = models.CharField(max_length=40)
    instructor = models.ForeignKey(Instructor, null=True, blank=True, on_delete=models.SET_NULL)
    credits = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=20)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'course'], name='unique_student_course')
        ]

    def __str__(self) -> str:
        return f'{self.student} - {self.course}'

from django.shortcuts import render, HttpResponse
from .models import Student

def add_student(request):
    student = Student(name="mounika", age=19, email="gummadilamounika10@gmail.com")
    student.save()
    return HttpResponse("Student record added successfully!")
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

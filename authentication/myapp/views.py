from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def java_exam_view(request):
    return render(request,'myapp/javaexam.html')

def python_exam_view(request):
    return render(request,'myapp/pythonexam.html')
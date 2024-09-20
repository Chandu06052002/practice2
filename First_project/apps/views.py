from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Student,Employee

# Create your views here.


def marks(request):
        if request.method == "POST":
                Name = request.POST['Name']
                Reg_no = request.POST['Reg_no']
                Maths = int(request.POST['Maths'])
                Physics = int(request.POST['Physics'])
                Chemistry = int(request.POST['Chemistry'])
                English = int(request.POST['English'])
                

                student = Student(Name=Name,Reg_no=Reg_no,Maths=Maths,Physics=Physics,Chemistry=Chemistry,English=English)
                details.save()
        return render(request,"task1.html")
        

def details(request):
                
        a = Student.objects.all()
        return render(request,'details.html',{'a':a})



def home(request):
        return render(request,("task2.html",{}))
   
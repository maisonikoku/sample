from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from app1.forms import EnquiryForm
from app1.models import Enquiry
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from app1.models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def mainPage(request):
    return render(request,'base.html')

def aboutPage(request):
    currentTime = datetime.now()
    return render(request,'about.html',{'time':currentTime,'name1':"daniel","name2":"keerthana"})

def coursePage(request):
    return render(request,'course.html')

def enquiry(request):
    form = EnquiryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main')
    return render(request,'enqForm.html',{'form':form})

def viewEnquiries(request):
    data = Enquiry.objects.all()
    return render(request,'viewEnq.html',{'data':data})

def editEnquiry(request,id):
    data = get_object_or_404(Enquiry,pk=id)
    form = EnquiryForm(request.POST or None,instance=data)
    if form.is_valid():
        form.save()
        return redirect('viewEnq')
    return render(request,'editEnq.html',{'data':form})

def deleteEnquiry(request,id):
    obj = get_object_or_404(Enquiry,pk=id)
    if request.method=="POST":
        obj.delete()
        return redirect('viewEnq')
    return render(request,'deleteEnq.html',{'data':obj})

class AddStudent(CreateView):
    model = Student
    fields = "__all__"
    template_name = 'addStudent.html'
    success_url = reverse_lazy('main')

class ViewStudents(ListView):
    model = Student
    queryset = Student.objects.all()
    template_name = 'viewStudents.html'
    context_object_name = 'data'

class EditStudent(UpdateView):
    model = Student
    fields = ('name','phone','mail','course','fees','address')
    success_url = reverse_lazy('viewStu')
    template_name = 'editStudent.html'

    def get_object(self):
        obj = get_object_or_404(Student,pk=self.kwargs['id'])
        return obj

class DeleteStudent(DeleteView):
    model = Student
    template_name = 'deleteStudent.html'
    success_url = reverse_lazy('viewStu')

    def get_object(self, queryset=None):
        obj = get_object_or_404(Student,pk=self.kwargs['id'])
        return obj

def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main')
    return render(request,'signup.html',{'form':form})

@login_required(login_url='login')
def staffPage(request):
    return render(request,'staffpage.html')
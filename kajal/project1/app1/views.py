from re import template
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.views import View
from django.core.paginator import Paginator,EmptyPage


# Create your views here.
class addEmployee(View):
    template_name = 'app1/addemployee.html'
    form = EmployeeForm
    def get(self,request):
        form = self.form
        context ={'form':form}
        return render(request,self.template_name,context)

    def post(self,request):
        form = self.form(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save()
            return redirect(obj.get_absolute_url())
        context ={'form':form}
        return render(request,self.template_name,context)

class singleShow(View):
    template_name = 'app1/singleft.html'
    def get(self,request,pk):
        obj = Employee.objects.get(pk=pk)
        context={'obj':obj}
        return render(request,self.template_name,context)

class ShowData(View):
    template_name = 'app1/showdata.html'
    def get(self,request):
        obj = Employee.objects.all()
        paginator = Paginator(obj,3)
        try:
            if request.GET.get('page'):
                user = paginator.page(request.GET.get('page'))
            else:
                user = paginator.page(1)

        except EmptyPage:
            user = paginator.page(paginator.num_pages)

        context={'user':user}
        return render(request,self.template_name,context)
class Upadte(View):
    template_name = 'app1/addemployee.html'
    form = EmployeeForm
    def get(self,request,pk):
        obj = Employee.objects.get(pk=pk)
        form = self.form(instance=obj)
        context={'form':form}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        obj = Employee.objects.get(pk=pk)
        form = self.form(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showdata_url')
        context={'form':form}
        return render(request,self.template_name,context)

class delete(View):
    template_name='app1/delete.html'
    def get(self,request,pk):
        obj = Employee.objects.get(pk=pk)
        context = {'obj':obj}
        return render(request,self.template_name,context)

    def post(self,request,pk):
        obj = Employee.objects.get(pk=pk)
        obj.delete()
        return redirect('showdata_url')
        context = {'obj':obj}
        return render(request,self.template_name,context)



class remove(View):
    def get(self,request,pk):
        try:
            img = Employee.objects.get(pk=pk)
            pic = img.image
            pic.delete()
            img.save()
            return redirect('showdata_url')
        except:
            return HttpResponse("<h1>RECOARD NOT FOUND<h1>")

class UpdateImage(View):
    template_name='app1/profile.html'
    def get(self,request,pk):
        try:
            img = Employee.objects.get(pk=pk)
            context={'img':img}
            return render(request,self.template_name,context)
        except:
            return HttpResponse("<h1>recoard not found</h1>")

        
    def post(self,request,pk):
        try:
            img = Employee.objects.get(pk=pk)
            img.image = request.FILES.get('file')
            img.save()
            return redirect('showdata_url')

        except:
            return HttpResponse("<h1>recoard not found</h1>")
 





            


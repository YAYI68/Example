from django.shortcuts import render
from django.urls import reverse_lazy
from .models import School,Student
from django.views.generic import (View,TemplateView,ListView,
                                   DetailView,CreateView,UpdateView,
                                   DeleteView)

# Create your views here.
class School_View(View):
    def get(self,request):
        return render(request,'school_app/index.html')

class School_TemplateView(TemplateView):
    template_name = 'school_app/index.html'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context['inject_me']='This is class TemplateView'
        return context


class School_listView(ListView):
    context_object_name = 'schools'
    template_name = 'school_app/school_list.html'
    model = School

class School_DetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'school_app/school_detail.html'

class School_CreateView(CreateView):
    fields = ('name','principal','location')
    model = School

class Student_CreateView(CreateView):
    fields = ('name','age','school')
    model = Student

class School_UpdateView(UpdateView):
    fields = ('name','principal')
    model = School

class School_DeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('school:list')

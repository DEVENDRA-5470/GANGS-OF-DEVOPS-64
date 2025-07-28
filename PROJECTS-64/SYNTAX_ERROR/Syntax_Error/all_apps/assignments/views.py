from django.shortcuts import *
from all_apps.assignments.models import *
from all_apps.assignments.forms import *
from django.views import View
# Create your views here.
def all_assi(request):
    as1=AllAssignment.objects.all()
    context={'as1':as1}
    return render(request,'alls.html',context)
  

def all_projects(request):
    proj=Project_Category.objects.all()
    context={'proj':proj}
    return render(request,'projects.html',context)

class upload_files(View):
    def get(self,request):
        form=Upload_assignment()
        print(form,"----------------")
        context={'form':form}
        return render(request,'uploads.html',context)
    
    def post(self,request):
        form=Upload_assignment(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form=Upload_assignment()
            return redirect('all-assignment')
        context={'form':form}
        return render(request,'uploads.html',context)

class add_category(View):
    def get(self,request):
        form=Add_Category()
        print(form,"----------------")
        context={'form':form}
        return render(request,'add_category.html',context)
    
    def post(self,request):
        form=Add_Category(request.POST)
        if form.is_valid():
            form.save()
            form=Add_Category()
            return redirect('upload-files')
        context={'form':form}
        return render(request,'add_category.html',context)



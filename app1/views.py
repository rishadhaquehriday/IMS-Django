from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def Home(request):
    fm = EmployeeForm()
    if request.method == 'POST':
        EmployeeForm(request.POST).save()
        return redirect('/')  
        
    data = Employee.objects.all()
    return render(request,'index.html',{'form':fm,'data':data})

def Delete_record(request,id):
    a = Employee.objects.get(pk=id)
    a.delete()
    return redirect('/')


# Update Record
def Update_record(request,id):
    if request.method == "POST":
        data = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST,instance = data)
        if form.is_valid():
            form.save()
    data = Employee.objects.get(pk=id)
    form = EmployeeForm(instance = data)
    context = {'form': form}
    return render(request,'update.html',context)

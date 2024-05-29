from django.shortcuts import render,redirect
from .models import  ParsonalTodo

# Create your views here.

def home(request):
  if request.method == "POST":
    Title = request.POST.get('textTitle') 

    if ParsonalTodo.objects.filter(title=Title).exists():
      massage = 'Alrady Data Exist'
    else:
      massage = 'Data Added'
      ParsonalTodo.objects.create(title=Title)

    # print(Title)
  all_data = ParsonalTodo.objects.all()
  
  return render(request, "index.html", locals())






# Delete function starting


def Delete(request,id):
  data = ParsonalTodo.objects.get(id=id)
  data.delete()
  return redirect('/')



def Complated(request,id):
  data = ParsonalTodo.objects.get(id=id)
  data.complate = True
  data.save()
  # Codata = ParsonalTodo.objects.create(complate = True)

  # print(Codata)

  print(data)
  return redirect('/')


def UnComplate(request,id):
  data = ParsonalTodo.objects.get(id=id)
  data.complate = False 
  data.save()
  # Codata = ParsonalTodo.objects.create(complate = True)

  # print(Codata)

  print(data)
  return redirect('/')
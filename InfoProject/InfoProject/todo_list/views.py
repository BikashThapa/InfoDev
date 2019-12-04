from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def home(request):
    all_items = List.objects.all
    if request.method=='POST':
        form=ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items=List.objects.all
            messages.success(request,('Item Has Been Added To List!'))
            return render(request,'home.html',{'all_items':all_items})

        else:
            all_items= List.objects.all
            return render(request,'home.html',{'all_items':all_items})
    return render(request, 'home.html', {'all_items':all_items})


def delete(request, list_id):
    item=List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,("Item Has Been Deleted"))
    return redirect('home')

def update(request,list_id):
    item = List.objects.get(pk=list_id)
    if request.method=='POST':
        form= ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,f'You are sucessfully updated')
            return redirect('home')
        else:
            return render(request,'edit.html',{'item':item})
    return render(request,'edit.html',{'item':item})



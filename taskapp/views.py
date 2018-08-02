from django.shortcuts import render
from .forms import FormTask
from django.shortcuts import redirect


# Create your views here.
def add(request):
    if request.method == "POST":
        form = FormTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('home')
    else:
        form = FormTask()
        return render(request, 'taskapp/add.html', {'form_task': form})


def home(request):
    return render(request, 'taskapp/home.html', {})

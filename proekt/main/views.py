from django.shortcuts import render, redirect
from .forms import ResponseForm


def index(request):
    error =''
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = '*Есть пустые поля'

    form = ResponseForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', data)
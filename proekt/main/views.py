from django.shortcuts import render, redirect
from .forms import ResponseForm, Response


def index(request):
    error = ''
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = '*Есть пустые поля'
    else:
        form = ResponseForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/index.html', data)


def results(request):
    return render(request, 'main/results.html')
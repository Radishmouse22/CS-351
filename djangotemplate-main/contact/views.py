from django.shortcuts import render, redirect
from .forms import MessageForm


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thank-you.html')
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})

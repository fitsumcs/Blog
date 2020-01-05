from django.shortcuts import render, redirect  
from .forms import SignUpFrom
# Create your views here.
def register(request): 
    if request.method == 'POST':
        form = SignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PersonalWeb:index')

    else:
        form = SignUpFrom()
    return render(request, 'users/register.html', {'form':form})

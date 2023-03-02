from django.shortcuts import render

# Create your views here.

# define the home view
def home(request):
    # include an.html file extension
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
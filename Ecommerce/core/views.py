from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"customer_front_end_ltr/index.html")
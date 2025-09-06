from django.shortcuts import render

# Create your views here.
def Index(request):  #aca faltaba el request
    return render(request, 'Index.html')  
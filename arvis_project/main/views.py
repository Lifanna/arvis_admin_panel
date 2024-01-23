from django.shortcuts import render

# Create your views here.
def main(request):
    
  pass

def choice(request):
   return render(request, 'main/choice.html')

def change (request):
    return render(request, 'main/change.html')
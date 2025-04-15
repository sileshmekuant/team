from django.shortcuts import render
from.models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'sile' 
    dest1.desc = 'The City That Never Sleeps'
    return render(request,"index.html",{'dest1':dest1})
from django.shortcuts import render
from Images_app.models import Image

# Create your views here.
def base(request):
    Data = Image.objects.all()
    Disnary = {"key" : Data}
    return render(request  , 'index.html' , context=Disnary)
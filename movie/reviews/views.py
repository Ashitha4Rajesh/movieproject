from django.shortcuts import render
from reviews.models import Review
from reviews.forms import reviewform 
app_name="reviews"
def addmovie(request):
    
    if(request.method=="POST"):
        image = request.FILES["i"]
        name = request.POST["m"]
        year = request.POST["y"]
        b = Review.objects.create(image=image,name=name,year=year)
        b.save()
        return viewmovie(request)
    return render(request,"addmovie.html")
def viewmovie(request):
    b = Review.objects.all()
    return render(request,"viewmovie.html",{"reviews":b})
def updel(request,p):
    b = Review.objects.get(id=p)
    return render(request,"updel.html",{"reviews":b})
def delete(request,p):
    b = Review.objects.get(id=p)
    b.delete()
    return viewmovie(request)
def update(request,p):
    b=Review.objects.get(id=p)
    form=reviewform(instance=b)
    if(request.method=="POST"):
        form = reviewform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return viewmovie(request)
    return render(request,'addmovie1.html',{'form':form})  
def home(request):
    b = Review.objects.all()
    return render(request,"home.html",{"reviews":b})
def addmovie1(request):
    form=reviewform()
    if(request.method=="POST"):
       form = reviewform(request.POST,request.FILES)
       if form.is_valid():
            form.save()
            return viewmovie(request)
    return render(request,'addmovie1.html',{'form':form}) 
  
# Create your views here.

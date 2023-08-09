from django.shortcuts import render,redirect
from .models import player

def index(request):
    return render(request,"index.html")

def add(request):
    return render(request,"add.html")

def playerview(request):
    data=player.objects.all()
    return render(request,"player.html",{'data':data})

def addplayer(request):
    if request.method=="POST":
        name=request.POST['name']
        club=request.POST['club']
        position=request.POST['position']
        mvalue=request.POST['mvalue']
        add=player(player_name=name,current_club=club,position=position,market_value=mvalue)
        add.save()
        return redirect('playerview')
    return render(request,"add.html")

def edit(request,id):
    Data=player.objects.get(id=id)
    return render(request,"edit.html",{'Data':Data})

def update(request,id):
    if request.method=='POST':
        add=player.objects.get(id=id)
        add.player_name=request.POST['name']
        add.current_club=request.POST['club']
        add.position=request.POST['position']
        add.market_value=request.POST['mvalue']
        add.save()
        return redirect("playerview")

def delete(request,id):
    add=player.objects.get(id=id)
    add.delete()
    return redirect("playerview")

# Create your views here.

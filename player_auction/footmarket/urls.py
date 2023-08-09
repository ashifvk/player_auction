from django.urls import path
from footmarket import views

urlpatterns = [
    path("",views.index,name="index"),
    path("add",views.add,name="add"),
    path("playerview",views.playerview,name="playerview"),
    path("addplayer",views.addplayer,name="addplayer"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("update/<int:id>",views.update,name="update"),

  
]
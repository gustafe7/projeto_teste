from django.urls import path
from . import views

app_name = 'tarefas'
urlpatterns = [
    path('', views.tarefas_home, name='home'),
<<<<<<< HEAD
    path('adicionar/',views.tarefas_adicionar, name='adicionar'),
=======
    path('adicionar/', views.tarefas_adicionar, name='adicionar'),
>>>>>>> 1186b51b3c75623195121236dc5d851d2f511f45
    path('remover/<int:id>',views.tarefas_remover,name='remover'),
    path('editar/<int:id>',views.tarefas_editar,name='editar')
]
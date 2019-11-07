from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('<id>', views.detail, name="detail"),
    path('addtask/', views.addtask, name="addtask"),
    path('delete/<id>', views.delete, name="deltask")
    # path('tasks/', tasks.urls)
]

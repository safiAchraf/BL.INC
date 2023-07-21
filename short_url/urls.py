from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_url>/', views.redirect_url, name='redirect'),
]
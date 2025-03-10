"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    ListExpecesView,
    CreateExpenseView,
    UpdateExpenseView,
    DeleteExpenseView,
    FilterExpenseView
)

urlpatterns = [
    path('list/', ListExpecesView.as_view(), name='list_of_expenses'),
    path('create/', CreateExpenseView.as_view(), name='create_expenses'),
    path('update/<int:pk>/', UpdateExpenseView.as_view(), name='update_expenses'),
    path('delete/<int:pk>/', DeleteExpenseView.as_view(), name='delete_expenses'),
    path('filter/', FilterExpenseView.as_view(), name='filter_expenses'),
]

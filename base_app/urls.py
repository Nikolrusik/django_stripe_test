from django.urls import path
from base_app.apps import BaseAppConfig 
from . import views

app_name = BaseAppConfig.name

urlpatterns = [
    # path('config/', views.stripe_config),
    path('buy/<int:pk>/', views.BuyView.as_view()), 
    path('item/<int:pk>/', views.ItemView.as_view()),
]
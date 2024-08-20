from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index-view'),
    
    ## APIs Patterns
    path('api/', include('main.apis.urls'))
]


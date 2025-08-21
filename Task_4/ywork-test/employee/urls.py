from django.urls import path,include
from . import views
urlpatterns = [
    path('create/', views.EmployeeCreateAPIView.as_view()),
    path('<int:pk>/set-base-salary/', views.EmployeeBaseSalaryUpdateAPIView.as_view()),
    path('high_earners/<int:department>/', views.HighEarnersAPIView.as_view()),
    path('high_earners/<int:department>/<str:month>/', views.HighEarnersByMonthAPIView.as_view()),
]


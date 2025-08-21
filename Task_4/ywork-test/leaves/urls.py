from django.urls import path
from . import views

urlpatterns = [
    path('', views.LeaveRecordListCreateAPIView.as_view()),
    path('<int:pk>/', views.LeaveRecordRetrieveUpdateDestroyAPIView.as_view()),
    path('increase-leave-put/', views.IncreaseLeaveCountPutAPIView.as_view()),
    path('payable-salary/', views.PayableSalaryAPIView.as_view()),
]

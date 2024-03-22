from django.urls import path
from OTS.views import views

urlpatterns = [
    path('',welcome ),
    path('new-candidate',candidateRegistrationFrom),
    path('store-candidate',candidateRegistration),
    path('login',loginView),
    path('homw',candidateHome),
    path('test-paper',testPaper),
    path('calculate-result',calculateTestResult),
    path('test-History',testResultHistory),
    path('result',showTestResult),
    path('logout',logoutView),
]
from rest_framework import routers
from django.urls import path


#local imports
from .views import EmployeeViewset,EmpsignupAPIView


router=routers.DefaultRouter()
router.register(r'employee',EmployeeViewset,basename="employee-management"),
#router.register(r'signup',EmpsignupAPIView.as_view(),basename="employee-signup")

urlpatterns=[

    path("signup/",EmpsignupAPIView.as_view(),name="employee-signup"),

    ]+router.urls

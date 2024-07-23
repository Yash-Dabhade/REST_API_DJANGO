from django.urls import path,include
from rest_framework import routers
from api.views import CompanyViewSet,EmployeeViewSet

# make defualt router
router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeeViewSet)

urlpatterns = [
    #put here url blank as above in router we are configuring it
    path('',include(router.urls))
]

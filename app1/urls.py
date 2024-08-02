from django.urls import path
from .views import *

urlpatterns=[
    path("a1/",addview),
    path("s1/",showview),
    path("u1/<int:id>/",updateview),
    # path("d1/<int:id>/",deleteview)



]

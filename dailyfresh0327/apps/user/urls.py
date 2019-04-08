from django.conf.urls import url,include
from .views import RegisterView,LogOutView,LoginView,Test

app_name = 'user'

urlpatterns = [
    url(r'^register$',RegisterView.as_view(),name='register'),
    url(r'^login$',LoginView.as_view(),name='login'),
    url(r'^logout$',RegisterView.as_view(),name='logout'),
    url(r'^test$',Test.as_view(),name='test'),
]

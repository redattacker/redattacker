from django.conf.urls import url,include
from .views import IndexView,IndexLog

app_name = 'goods'
urlpatterns = [
    url(r'^',IndexView.as_view(),name='index'),
    url(r'^log$',IndexLog.as_view()),
]

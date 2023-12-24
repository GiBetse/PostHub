from django.urls import path, include
from . import views
from .hjh import newurls
from . import views


urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('create', views.create, name='create'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts')

]


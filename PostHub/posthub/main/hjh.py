from django.urls import path, include
from . import views
newurls=[]
for i in range (10):
    newurls.append(path(f'state{i}', views.PostView.as_view(), name=f'state{i}'))

    '''urlpatterns.extend(newurls)'''
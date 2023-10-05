from django.urls import path
from.import views

app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweet, name="listtweet"), #siteadi.com/tweetapp/
    path('addtweet/', views.addtweet, name="addtweet"), #siteadi.com/tweetapp/addtweet
    path('addtweetbyform/', views.addtweetbyform, name="addtweetbyform"), #siteadi.com/tweetapp/addtweetbyform
    path('addtweetbymodelform/', views.addtweetbymodelform, name="addtweetbymodelform"), #siteadi.com/tweetapp/addtweetbymodelform
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('deletetweet/<int:id>', views.deletetweet, name="deletetweet")
]
from django.urls import path
from .views import SignUpView, user_logout

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signout/', user_logout, name='user_logout'),
]
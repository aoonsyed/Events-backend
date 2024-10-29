from .views import UserRegistrationView, EventRegistrationView, EventAPIView, UserAPIView, CustomUserLoginView, CustomUserLogoutView
from django.urls import path
urlpatterns = [
    path('user/', UserRegistrationView.as_view(), name='registeruser'),
    path('event/',EventRegistrationView.as_view(),name='registerevent'),
    path('eventAPI/',EventAPIView.as_view(),name = 'eventAPI'),
    path('userAPI/',UserAPIView.as_view(),name = 'userAPI'),
    path('api/login/', CustomUserLoginView.as_view(), name='login'),
    path('api/logout/', CustomUserLogoutView.as_view(), name='logout'),
]

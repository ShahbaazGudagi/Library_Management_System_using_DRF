from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('books', views.AdminBookView)
router.register('Category', views.CategoryView)
router.register('Signup', views.SignupView,basename='test')
router.register('students', views.UserView)


urlpatterns = [
    path('', include(router.urls)),
    path('login/',views.LoginView.as_view())
]
from django.urls import path
from . import views


urlpatterns = [
    path('generator/', views.generator, name='generator'),
    path('password/', views.passgen, name='pass'),
    path('register/', views.register, name='register'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/<id>', views.edit, name='edit'),
    path('profile/delete/<id>', views.delete, name='delete'),
    path('editpass/', views.editpass, name='editpass'),
    path('addpass/', views.add_pass, name='add_pass'),
    path('addprofile/', views.add_pass_profile, name='addprofile'),
]

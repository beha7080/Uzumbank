# from django.urls import path, include
# from .views import BarchaUser
#
#
# urlpatterns = [
#     path('all_user/<int:id>', BarchaUser.as_view()),
# ]
#
#
#
# from django.urls import path
# from .views import RegisterView, LoginView, AllUsersView, UserDetailView, UpdatePasswordUser, UpdateLastName
#
# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('allusers/', AllUsersView.as_view(), name='all_users'),
#     path('users/<int:id>/', UserDetailView.as_view(), name='user_detail'),
#     path('update_password/', UpdatePasswordUser.as_view(), name='update_password'),
# ]
#
#
#
#
# from django.urls import path
# from .views import RegisterView, LoginView, AllUsersView, UserDetailView,UpdatePasswordUser
#
# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('allusers/', AllUsersView.as_view(), name='all_users'),
#     path('users/<int:id>/', UserDetailView.as_view(), name='user_detail'),
#     path('update_password/', UpdatePasswordUser.as_view(), name='update_password'),
#
# ]
#
#
#



from django.urls import path
from .views import RegisterView, LoginView, AllUsersView, UserDetailView, UpdatePasswordUser, UpdatephonenumberUser,PasswordUpdateRateThrottle

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('allusers/', AllUsersView.as_view(), name='all_users'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user_detail'),
    path('update_password/', UpdatePasswordUser.as_view(), name='update_password'),
    path('update_phone/', UpdatephonenumberUser.as_view(), name='update_phone'),
    path('update_rate/', PasswordUpdateRateThrottle.as_view(), name='update_rate'),

]


from django.contrib import admin
from django.urls import path, include

urlpattern = [
    path('admin/', admin.site.urls),
    path('user/', include('usersapp.urls')),
]

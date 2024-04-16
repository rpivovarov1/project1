from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registration/', views.reg),
    path('log_in/', views.user_login),
    path('login/', views.user_login),
    path('profile/', views.profile),
    path('reset_password/', views.change_password),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
password_change/ [name='password_change']
password_change/done/ [name='password_change_done']
password_reset/ [name='password_reset']
password_reset/done/ [name='password_reset_done']
reset/<uidb64>/<token>/ [name='password_reset_confirm']
reset/done/ [name='password_reset_complete']
"""
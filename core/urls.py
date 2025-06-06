from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, UserViewSet, ProgramViewSet, MajorViewSet, \
    UserProfileUpdateView, AdminViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'admins', AdminViewSet, basename="admin-users")
router.register(r'programs', ProgramViewSet, basename="programs")
router.register(r'majors', MajorViewSet, basename="majors")


urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/auth/register/', RegisterView.as_view(), name='register'),
    path('api/v1/auth/login/', LoginView.as_view(), name='login'),
    path('api/v1/auth/profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),

]

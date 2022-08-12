"""SoftDesk_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from project.views import ProjectsViewset, ContributorsViewset
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.SimpleRouter()
router.register(r"projects/?", ProjectsViewset, basename='projects')
router.register(r"projects/(?P<project_id>[^/.]+)/user", ContributorsViewset, basename='users')

users_router = routers.NestedSimpleRouter(router, r"projects/?", lookup="projects", trailing_slash=False)
users_router.register(r"users/?", ContributorsViewset, basename="users")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('user.urls')),
    path('', include(router.urls)),
    path('', include(users_router.urls)),

]

# routeur
# router = routers.DefaultRouter()
# router.register(r"projects", ProjectsViewset, basename="projects")
## generates:
# /projects/
# /projects/{pk}/


# user_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
# user_router.register(r"users", ContributorsViewset, basename="users")
## generates:
# /projects/{project_pk}/users/
# /projects/{project_pk}/users/{user_pk}/

# issues_routeur = routers.NestedSimpleRouter(router, r"projects", lookup="project")
# issues_routeur.register(r"issues", IssuesViewset, basename="issues")
## generates:
# /projects/{project_pk}/issues/
# /projects/{project_pk}/issues/{issue_pk}/


# comments_routeur = routers.NestedSimpleRouter(issues_routeur, r"issues", lookup="issue")
# comments_routeur.register(r"comments", CommentsViewset, basename="comments")
## generates:
# /projects/{project_pk}/issues/{issue_pk}/comments/
# /projects/{project_pk}/issues/{issue_pk}/comments/{pk}/
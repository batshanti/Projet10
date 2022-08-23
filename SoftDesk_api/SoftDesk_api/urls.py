from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from project.views import(
    ProjectsViewset,
    ContributorsViewset,
    IssuesViewset,
    CommentsViewset
)


router = routers.SimpleRouter()
router.register(r"projects/?", ProjectsViewset, basename='projects')


users_router = routers.NestedSimpleRouter(
    router,
    r"projects/?",
    lookup="projects",
    trailing_slash=False
)
users_router.register(r"users/?", ContributorsViewset, basename="users")

issues_router = routers.NestedSimpleRouter(
    router,
    r"projects/?",
    lookup="projects",
    trailing_slash=False
)
issues_router.register(r"issues/?", IssuesViewset, basename="issues")

comments_router = routers.NestedSimpleRouter(
    issues_router,
    r"issues/?",
    lookup="issues",
    trailing_slash=False
)
comments_router.register(r"comments/?", CommentsViewset, basename="comments")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('user.urls')),
    path('', include(router.urls)),
    path('', include(users_router.urls)),
    path('', include(issues_router.urls)),
    path('', include(comments_router.urls))
]

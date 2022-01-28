from django.urls import path
from projects import views as projects_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', projects_views.index.as_view(), name='home'),
    path('api/projects/', projects_views.project_list),
    path('api/projects/<int:pk>/', projects_views.project_detail),
    path('api/projects/published/', projects_views.project_list_published)
]
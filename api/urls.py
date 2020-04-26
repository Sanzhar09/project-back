from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('categories/', views.CategoryListView.as_view()),
    path('articles/', views.articles),
    path('articles/publish/', views.articles_for_publisher),
    path('articles/admin/<int:id>', views.EditorView.as_view()),
    path('login/', obtain_jwt_token)
]
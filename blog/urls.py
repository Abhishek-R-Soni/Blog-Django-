from django.contrib import admin
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name="index"),
    path('post_list/', views.PostListView.as_view(), name="post_list"),
    path('post_list/<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('post_create/', views.PostCreateView.as_view(), name="post_create"),
    path('post_update/<int:pk>/', views.PostUpdateView.as_view(), name="post_update"),
    path('post_delete/<int:pk>/', views.PostDeleteView.as_view(), name="post_delete"),
#     path('post_draft/', views.DraftListView.as_view(), name="post_draft"),
#     path('post_list/<int:pk>/comment/', views.add_comment_to_post, name="comment_post"),
#     path('commment/<int:pk>/approve/', views.comment_approve, name="comment_approve"),
#     path('commment/<int:pk>/remove/', views.comment_remove, name="comment_remove"),
#     path('post_update/<int:pk>/publish/', views.post_publish, name="post_publish"),
]
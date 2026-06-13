from django.urls import path
from .views import homeview, AboutView, home_view_data, blog_detail_view, createBlog

urlpatterns = [
    path('', home_view_data.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('<int:pk>/', blog_detail_view.as_view(), name='detail'),
    path('create/', createBlog.as_view(), name='create'),
]

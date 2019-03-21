from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/vote/', views.post_vote_view, name="post_vote"),
        # intermediary path to display a vote and thus not specific to a template   
]

from django.urls import path

from first_app import views

urlpatterns = [
    # ex: /first_app/
    path('', views.index, name='index'),
    # ex: /first_app/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /first_app/5/results/
    path('<int:question_id>/result/', views.result, name='result'),
    # ex: /first_app/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
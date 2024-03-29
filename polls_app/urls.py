from django.urls import path

from . import views

app_name = 'polls_app'

# urlpatterns = [
#     path("", views.index, name='index'),
#     path("<int:question_id>/", views.details, name="details"),
#     path("<int:question_id>/results/", views.results, name='results'),
#     path("<int:question_id>/votes/", views.votes, name='vote'),
# ]

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("<int:pk>/", views.DetailView.as_view(), name='details'),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/votes/", views.votes, name='vote')
]

from django.urls import path

from . import views, livro_views

app_name = "saberacao"
urlpatterns = [
    path("", views.index, name="index"),
    # path("home", views.home, name="home")
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
    path("livros/<int:id>", views.livros_detalhes, name="livros_detalhes"),
]
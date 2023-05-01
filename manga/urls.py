from django.urls import path
from .views import MangaListView, MangaDetailView, MangaPageView

urlpatterns = [
    path('', MangaListView.as_view(), name='manga_list'),
    path('<int:pk>/', MangaDetailView.as_view(), name='manga_detail'),
    path('<int:pk>/page/<int:page>/', MangaPageView.as_view(), name='manga_page'),
]

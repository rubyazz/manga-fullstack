from django.urls import path
from .views import MangaListView, MangaDetailView, MangaPageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MangaListView.as_view(), name='manga_list'),
    path('<int:pk>/', MangaDetailView.as_view(), name='manga_detail'),
    path('<int:pk>/page/<int:page>/', MangaPageView.as_view(), name='manga_page'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
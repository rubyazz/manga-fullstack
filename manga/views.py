from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Manga, MangaPage

class MangaPageView(View):
    def get(self, request, pk, page):
        manga_page = get_object_or_404(MangaPage, manga=pk, page_number=page)
        with open(manga_page.image.path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/png')

class MangaListView(View):  
    def get(self, request):
        mangas = Manga.objects.all()
        context = {'mangas': mangas}
        return render(request, 'manga_list.html', context)

class MangaDetailView(View):
    def get(self, request, pk):
        manga = get_object_or_404(Manga, pk=pk)
        pages = MangaPage.objects.filter(manga=manga).order_by('page_number')
        context = {'manga': manga, 'pages': pages}
        return render(request, 'manga_detail.html', context)

#https://www.figma.com/file/H9rWhlkSUd8sT3GwWKyPux/Manga-App-UI-(Community)?node-id=59-504&t=CtauUVcYwUaU5Gvp-0
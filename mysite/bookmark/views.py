from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

#LoginRequiredMixin, CreateView를 상속받아 BookmarkCreateView 작성. 로그인된 경우만 접근 가능
class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url'] #폼울 보여줄 때 'title', 'url' 필드에 대한 입력폼을 보여줌
    success_url = reverse_lazy('bookmark:index')
    def from_vaild(self, form):
        form.instance.owner = self.request.username #owner 필드에 현재 로그인된 유저 객체 할당
        return super(BookmarkCreateView, self).form_valid(form) #CreateView 클래스의 form_valid() 메소드 호출

class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'
    def get_queryset(self): #화면에 출력할 레코드 리스트 반환
        return Bookmark.objects.filter(owner=self.request.user)

class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')

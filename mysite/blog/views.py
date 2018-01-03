from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from blog.models import Post

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from mysite.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import CommentForm
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
#ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 5

#Detail views
class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content']
    #title 필드로부터 자동으로 채워짐.레코드 생성폼을 보여줄 때 slug 필드를 입력하지 말라는 의미의 촐기값
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog:index')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content']
    success_url = reverse_lazy('blog:index')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print (post)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse('blog:post_detail', args=(post.slug,)))
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
#    return redirect('blog:post_detail', pk=comment.post.pk)
    return redirect(reverse('blog:post_detail', args=(comment.post.slug,)))
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.slug
    comment.delete()
#    return redirect('blog:post_detail', pk=post_pk)
    return redirect(reverse('blog:post_detail', args=(post_slug,)))

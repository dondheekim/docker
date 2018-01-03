from django.shortcuts import render
from main_list.models import Student
from django.views.generic import ListView
# Create your views here.
class PostMysql(ListView):
    model = Student
    template_name = 'main_list/all.html'

class PostApache(ListView):
    model = Student
    template_name = 'main_list/apache.html'

class PostServer(ListView):
    model = Student
    template_name = 'main_list/server.html'



#    def index(request):
#        post_list = Post.objects.all()
#        return render(request, 'all.html'), {

#            'post_list' : post_list,
#    }

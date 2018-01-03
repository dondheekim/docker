from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView #테이블 레코드 생성
from django.contrib.auth.forms import UserCreationForm #user model 객체 생성
from django.core.urlresolvers import reverse_lazy #인자로 url 패턴명 받기. url 모듈이 로딩되지 않을 수도 있으니 lazy 사용
from django.contrib.auth.decorators import login_required

class HomeView(TemplateView): #template_name 변수를 오버라이딩으로 지정
    template_name = 'home.html'

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView): #/accounts/register/done url 처리 . TemplateView 제네릭뷰 상솟
    template_name = 'registration/register_done.html'

class LoginRequiredMixin(object):
    @classmethod #login_required() 장식자 기능 제공3
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

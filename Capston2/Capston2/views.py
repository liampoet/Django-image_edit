from django.views.generic.base import TemplateView
from django.views.generic import CreateView # 테이블에 새로운 레코드(폼에 입력된 데이터) 생성하는 뷰
from django.contrib.auth.forms import UserCreationForm # User 객체 생성
from django.urls import reverse_lazy # 인자로 URL 패턴을 받음

# 홈페이지 뷰
class HomeView(TemplateView):
    template_name = 'home.html' # 템플릿 뷰를 사용할 시 필수 클래스 변수(template_name), home.html에서 표출하겠다.

class descriptionView(TemplateView):
    template_name = 'description.html'


# 유저 생성 뷰(테이블에 레코드 추가/생성)
class UserCreateView(CreateView):
    template_name = 'registration/register.html' # 가입할 때 사용자에게 보여줄 템플릿
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done') # 폼에 에러 없다면 accounts/register/done/으로 리다이렉트

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html' # 가입 처리 완료 후 사용자에게 보여줄 템플릿

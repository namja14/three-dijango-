from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Blog # 이거써서 가져오기
from .form import BlogPost

# Create your views here.
def home(request):
    blogs = Blog.objects # 쿼리셋
    #블로그 모든글을 대상으로 
    blog_list = Blog.objects.all()
    #블로그 객체 세개를 한페이지로 자르기
    paginator =Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return해 준다
    posts = paginator.get_page(page) 
    return render(request, 'home.html',{'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    #몇번객체애 담아 pk 는 프라이머리 키 이거 기준찾아가라
    return render(request, 'detail.html', {'details':details})# 이거 왜쓰는거임?

def new(request): #뉴페이지 문서 뛰어주는거
    return render(request, 'new.html')

def create(request):#입력받은 내용을 데이터베이스에 넣어주는 함수 
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> post  
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')  
    #2. 빈 페이지를 띄어주는 기능 -> get
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})
        
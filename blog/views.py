from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    blogs = Blog.objects #블로그 안에 있는 객체를 블로그 안에 넣어줌
    return render(request, 'home.html', {'blogs': blogs})

    #모델로 부터 객체 목록을 전달받았음 .objects 이걸 쿼리셋이라고 함
    #쿼리셋 매소드 형식
    #모델.쿼리셋(objects),메소드
# Create your views here.
def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog' : blog_detail})
def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+ str(blog.id))
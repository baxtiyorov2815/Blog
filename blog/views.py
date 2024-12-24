from django.shortcuts import render, redirect
from .models import Post, Comment, Genre
from .froms import PostForm

def homepage(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request=request,
                  template_name='index.html',
                  context=context)

def aboutpost(reqeust, pk):
    post = Post.objects.get(id=pk)
    return render(request=reqeust,
                  template_name='detail.html',
                  context={"post": post})

def editpost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"form": form}
    return render(request=request,
                  template_name='edit.html',
                  context=context)

def deletepost(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('home')
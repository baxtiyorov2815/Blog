from django.shortcuts import render, redirect
from .models import Post, Comment, Genre
from .froms import PostForm, GenreForm
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.db.models import Q

# def homepage(request):
#     posts = Post.objects.all()
#     context = {"posts": posts}
#     return render(request=request,
#                   template_name='index.html',
#                   context=context)

# def aboutpost(reqeust, pk):
#     post = Post.objects.get(id=pk)
#     return render(request=reqeust,
#                   template_name='detail.html',
#                   context={"post": post})

# def editpost(request, pk):
#     post = Post.objects.get(id=pk)
#     form = PostForm(instance=post)
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('home')

#     context = {"form": form}
#     return render(request=request,
#                   template_name='edit.html',
#                   context=context)

# def deletepost(request, pk):
#     post = Post.objects.get(id=pk)
#     post.delete()
#     return redirect('home')

class HomePageView(View):
    def get(self, request):
        q = request.GET.get('q') if request.GET.get('q') != None else ''
        posts = Post.objects.filter(
            Q(genre__title__icontains=q) |
            Q(title__icontains=q) |
            Q(desc__icontains=q)
            )
        genres = Genre.objects.all()
        context = {"posts": posts, "genres": genres}
        return render(request=request,
                      template_name='index.html',
                      context=context)
    
class DetailPostView(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        context = {"post": post}
        return render(request=request,
                      template_name="detail.html",
                      context=context)
    
class EditPostView(View, LoginRequiredMixin):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        form = PostForm(instance=post)
        context = {"form": form}
        return render(request=request,
                      template_name='edit.html',
                      context=context)
    
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save
            return redirect('home')
        
class DeletePostView(View, LoginRequiredMixin):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        context = {"post": post}
        return render(request=request,
                      template_name='delete.html',
                      context=context)
    
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        post.delete()
        return redirect('home')
    
class CreateNewGenre(View, LoginRequiredMixin):
    def get(self, request):
        form = GenreForm()
        context = {'form': form}
        return render(request=request,
                      template_name='newgenre.html',
                      context=context)
    
    def post(self, reqeust):
        form = GenreForm(reqeust.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
class CreateNewPost(View, LoginRequiredMixin):
    def get(self, request):
            form = PostForm()
            context = {"form": form}
            return render(request=request,
                        template_name='newpost.html',
                        context=context)
    
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            form = PostForm()
            return render(request, reverse(), {'form': form})
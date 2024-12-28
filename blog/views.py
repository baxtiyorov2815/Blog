from django.shortcuts import render, redirect
from .models import Post, Comment, Genre
from .froms import PostForm, GenreForm
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

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
                      template_name='crud/index.html',
                      context=context)
    
class DetailPostView(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        print(pk)
        context = {"post": post}
        return render(request=request,
                      template_name="crud/detail.html",
                      context=context)
    
class EditPostView(View, LoginRequiredMixin, PermissionRequiredMixin):
    def get(self, request, pk):
        if request.user.is_active:
            post = Post.objects.get(id=pk)
            form = PostForm(instance=post)
            context = {"form": form}
            return render(request=request,
                        template_name='crud/edit.html',
                        context=context)
        else:
            return redirect('home')
    
    def post(self, request, pk):
        if request.user.is_active:
            post = Post.objects.get(id=pk)
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save
                messages.add_message(request, messages.SUCCESS, "Post has been edited succsecfully!")
                return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, "SOMETHING WENT WRONG PLEASE TRY AGAIN!")
            return redirect('home')
        
class DeletePostView(View, LoginRequiredMixin, PermissionRequiredMixin):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        context = {"post": post}
        #messages.add_message(request, messages.WARNING, "Post has been deleted succsecfully!")
        return render(request=request,
                      template_name='crud/delete.html',
                      context=context)
    
    def post(self, request, pk, *args, **kwargs):
        messages.add_message(request, messages.WARNING, "Post has been deleted succsecfully!")
        post = Post.objects.get(id=pk)
        if post and (post.author == request.user or request.user.has_perm('blog.delete_post')):
            post.delete()
            return redirect('home')
        
        return self.get(self, request, pk)
    
class CreateNewGenre(View, LoginRequiredMixin, PermissionRequiredMixin):
    def get(self, request):
        if request.user.is_active:
            form = GenreForm()
            context = {'form': form}
            return render(request=request,
                        template_name='crud/newgenre.html',
                        context=context)
        else:
            return redirect('home')
        
    def post(self, request):
        if request.user.is_active:
            form = GenreForm(request.POST)
            if form.is_valid():
                messages.add_message(request, messages.WARNING, "Post has been deleted succsecfully!")
                form.save()
                return redirect('home')
            else:
                messages.add_message(request, messages.ERROR, "Something went wrong please try again!")
        else:
            return redirect('home')
                
class CreateNewPost(View, LoginRequiredMixin, PermissionRequiredMixin):
    def get(self, request):
        if request.user.is_active:
            form = PostForm()
            context = {"form": form}
            return render(request=request,
                        template_name='crud/newpost.html',
                        context=context)
    def post(self, request):
        if request.user.is_active:
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                messages.add_message(request, messages.SUCCESS, "Post has been created succsecfully!")
                post = form.save(commit=False)
                print(request)
                post.author = request.user
                post.save()
                return redirect('home')
            else:
                messages.add_message(request, messages.SUCCESS, "Something went wrong please try again!")
                form = PostForm()
                return render(request, reverse(), {'form': form})
        else:
            return redirect('home')
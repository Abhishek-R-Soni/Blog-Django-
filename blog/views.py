from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from blog.models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm, CommentForm
from django.utils import timezone

# Create your views here.
class IndexView(TemplateView):
    template_name = 'blog/about.html'

# about Post
class PostListView(ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    context_object_name = 'post'
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin ,CreateView):
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

# class DraftListView(LoginRequiredMixin, ListView):
#     login_url = '/login/'
#     redirect_field_name = 'blog/post_list.html'
#     model = Post

#     def get_queryset(self):
#         return Post.objects.filter(published_date__isnull = True).order_by('created_date')

def post_publish(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.publish
    return redirect('post_detail',pk = pk)

# @login_required
# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk = pk)

#     if request.method == "POST":
#         form = CommentForm(request.POST)

#         if form.is_valid():
#             comment = form.save(commit = False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk = post.pk)
#     else:
#         form = CommentForm()

#     return render(request, 'blog/comment_form.html', {'form' : form})

# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk = pk)
#     comment.approve()
    
#     return redirect('post_detail', pk = comment.post.pk)

# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk = pk)
#     post_pk = comment.post.pk
#     comment.delete()

#     return redirect('post_detail', pk = post_pk)
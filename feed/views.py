# articles/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, FormMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import NewCommentForm

class FeedListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'feed_list.html'
    form_class = NewCommentForm
    ordering = ['-date'] #reverses order
    #Post method for comments
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get("post_id")
        post = get_object_or_404(Post, id=post_id)

        new_comment = Comment(comment=request.POST.get('comment'),
                                    author=self.request.user,
                                    post=post)
        new_comment.save()
        return self.get(self, request, *args, **kwargs)



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('feed_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ('body',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
   
class PostDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    form_class = NewCommentForm


    def post(self, request, *args, **kwargs):
            new_comment = Comment(comment=request.POST.get('comment'),
                                    author=self.request.user,
                                    post=self.get_object())
            new_comment.save()
            return self.get(self, request, *args, **kwargs)

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('feed_list')

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user
# accounts/views.py
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import CustomUserCreationForm, FollowForm
from .models import CustomUser, Following
from feed.models import Post
from django.contrib import messages


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'registration/profile.html'
    form_class = FollowForm

    def get_context_data(self, *args, **kwargs):
        users = CustomUser.objects.all()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(CustomUser, id=self.kwargs['pk'])
        context["page_user"] = page_user
        #context["followers"] = Following.objects.filter(user_id=page_user)
        context["followers"] = page_user.followers.all()
        context["following"] = page_user.following.all()
        context["posts"] = Post.objects.filter(author=page_user).order_by('-date')
        return context

    def post(self, request, *args, **kwargs):
        page_user = get_object_or_404(CustomUser, id=self.kwargs['pk'])
        current_user = self.request.user
        if 'follow' in request.POST:
            if self.request.user == page_user:
                messages.error(request,'Unable to follow youself')
            #elif Following.objects.filter(user_id=current_user).get(following_user_id = page_user).exists():
            elif Following.objects.filter(user_id=current_user, following_user_id=page_user).exists():
                messages.error(request,'You already follow this user')
            else:
                new_following = Following(user_id = current_user, following_user_id=page_user)
                new_following.save()
            return self.get(self, request, *args, **kwargs)
        elif 'unfollow' in request.POST:
            page_user = get_object_or_404(CustomUser, id=self.kwargs['pk'])
            Following.objects.filter(user_id=current_user).get(following_user_id = page_user).delete()
            return self.get(self, request, *args, **kwargs)



class ProfileUpdateView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    model = CustomUser
    fields = ['bio']
    template_name = 'registration/profile_update.html'

    def get_success_url(self):
        # if you are passing 'pk' from 'urls' to 'DeleteView' for company
        # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
        profile_id  = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': profile_id})
    
    def test_func(self): #testing criteria - over writing base test_func
        obj = self.get_object()
        return obj == self.request.user


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser 
    template_name = 'user_list.html'
    form_class = FollowForm

    def post(self, request, *args, **kwargs):
        page_user_id = request.POST.get("user")
        page_user = get_object_or_404(CustomUser, id=page_user_id)
        new_following = Following(user_id = self.request.user, following_user_id=page_user)
        new_following.save()
        return self.get(self, request, *args, **kwargs)


    ''' need to pass in item
        what if I increment for each item in queryset
    '''
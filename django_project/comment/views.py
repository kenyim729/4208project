from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Comment


def Forum(request):
    context = {
        'comments': Comment.objects.all()
    }
    return render(request, 'blog/Forum.html', context)


class CommentListView(ListView):
    model = Comment
    template_name = 'blog/Forum.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'comments'
    ordering = ['-date_posted']


class CommentDetailView(DetailView):
    model = Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

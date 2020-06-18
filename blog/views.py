from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Tag

# Create your views here.

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 6


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 6

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

@login_required
def comment(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	comment = request.POST['comment']
	author = request.user
	post.comment_set.create(content=comment, author=author).save()

	return HttpResponseRedirect(reverse('post-detail', args=(post_id,)))


@login_required
def comment_delete(request, post_id, comment_id):
	comment = get_object_or_404(Comment, pk=comment_id)
	if self.request.user == comment.author:
		comment.delete()

	return HttpResponseRedirect(reverse('post-detail', args=(post_id,)))


@login_required
def tag_create(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	tagname = request.POST['tag']
	try:
		tag = Tag.objects.get(name=tagname)
		post.tag_set.add(tag)
	except (KeyError, Tag.DoesNotExist):
		post.tag_set.create(name=tagname)
	
	return HttpResponseRedirect(reverse('post-detail', args=(post_id,)))


class PostDetailView(DetailView):
	model = Post
	
	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		context['comments'] = Comment.objects.filter(post=self.object).order_by('-date_posted')
		return context


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('blog-home')

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})



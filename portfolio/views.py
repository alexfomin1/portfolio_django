from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
	model = Post
	template_name = 'home.html'

	def get_queryset(self, *args, **kwargs):
		qs = super(BlogListView, self).get_queryset(*args, **kwargs)
		qs = qs.order_by("-id")
		return qs


class BlogDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'
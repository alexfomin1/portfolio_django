from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):

	def setUp(self):
		self.post = Post.objects.create(
			title='A good title',
			text='Nice content'
		)

	def test_string_representation(self):
		post = Post(title='A sample title')
		self.assertEqual(str(post), post.title)

	def test_post_content(self):
		self.assertEqual(f'{self.post.title}', 'A good title')
		self.assertEqual(f'{self.post.body}', 'Nice content')

	def test_post_list_view(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, 'Nice content')
		self.assertTemplateUsed(resp, 'home.html')

	def test_post_detail_view(self):
		resp = self.client.get('/post/1/')
		no_response = self.client.get('/post/1000000/')
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(resp, 'A good title')
		self.assertTemplateUsed(resp, 'post_detail.html')
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest 
from django.template.loader import render_to_string 
from papers.views import home, paper_sub, review_sub, registration
from booking.views import booking


class HomePageTest(TestCase):
	# Test that url directs to the home page
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home)

	# Test that page returns defined html page
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)


class RegisterPageTest(TestCase):
	
	def test_root_url_resolves_to_register_page_view(self):
		found = resolve('/registration/')
		self.assertEqual(found.func, registration)


class ReviewPageTest(TestCase):
	
	def test_root_url_resolves_to_review_page_view(self):
		found = resolve('/review_sub/')
		self.assertEqual(found.func, review_sub)


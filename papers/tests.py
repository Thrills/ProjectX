from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest 
from django import forms
from django.template.loader import render_to_string 
from papers.views import home, paper_sub, review_sub, registration
from booking.forms import BookingForm
from booking.models import Delegate

class DelegateModelTest(TestCase):

<<<<<<< HEAD
	def test_saving_and_retrieving_items(self):
		first_delegate.id = Delegate(1)
		first_delegate.delegate_name = Delegate(aron)
		first_delegate.delegate_surname = Delegate(fro)
		first_delegate_email = Delegate(rty)
		first_delegate.text = 'The first delegate'
		first_delegate.save()

		second_delegate.id = Delegate(2)
		second_delegate.delegate_name = Delegate(ef)
		second_delegate.delegate_surname = Delegate(rta)
		second_delegate_email = Delegate(sd)
		second_delegate.text = 'The second delegate'
		second_delegate.save()

		saved_delegates = Delegate.objects.all()
		self.assertEqual(saved_delegates.count(), 2)

		first_saved_delegate= saved_delegates[0]
		second_saved_delegate = saved_delegate[1]
		self.assertEqual(first_saved_delegate.text, 'The first delegate')
		self.assertEqual(second_saved_delegate.text, 'The second delegate')

		




=======
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
>>>>>>> 479beb1e9665d0568a26dce512e92b3e812d5539


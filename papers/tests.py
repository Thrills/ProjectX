from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest 
from django.template.loader import render_to_string 
from papers.views import home, paper_sub, review_sub, registration
from booking.views import booking


class HomePageTest(TestCase):
	
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

class BookingPageTest(TestCase):
	
	def test_root_url_resolves_to_booking_page_view(self):
		found = resolve('/booking')
		self.assertEqual(found.func, booking)

# 	def test_booking_page_returns_correct_html(self):
# 		request = HttpRequest()
# 		response = booking(request)
# 		expected_html = render_to_string('booking.html')
# 		self.assertEqual(response.content.decode(), expected_html)

class RegisterPageTest(TestCase):
	
	def test_root_url_resolves_to_register_page_view(self):
		found = resolve('/registration')
		self.assertEqual(found.func, registration)

	# def test_registration_page_returns_correct_html(self):
	# 	request = HttpRequest()
	# 	response = registration(request)
	# 	expected_html = render_to_string('registration.html')
	# 	self.assertEqual(response.content.decode(), expected_html)

	# def test_home_page_can_save_a_POST_request(self):
	# 	request = HttpRequest()
	# 	request.method = 'POST'
	# 	request.POST[item_text] = 'A new list item' # 54, 55 - item_text WHAT is posted

	# 	response = home_page(request)

	# 	self.assertEqual(MyUser.object.count(), 1)
	# 	new_item = MyUser.object.first()
	# 	self.assertEqual(new_item.text, 'A new list item')

	# def test_home_page_redirects_after_POST(self):
	# 	request = HttpRequest()
	# 	request.method = 'POST'
	# 	request.POST[item_text] = 'A new list item' # 54, 55 - item_text WHAT is posted

	# 	response = home_page(request)

	# 	self.assertEqual(response.status_code, 302)
	# 	self.assertEqual(response['location'], '/')

# class ReviewPageTest(TestCase):
	
# 	def test_root_url_resolves_to_review_page_view(self):
# 		found = resolve('/review_sub')
# 		self.assertEqual(found.func, review_sub)

# 	def test_review_page_returns_correct_html(self):
# 		request = HttpRequest()
# 		response = review_sub(request)
# 		expected_html = render_to_string('review.html')
# 		self.assertEqual(response.content.decode(), expected_html)
	
	# form test -------------------------

	# def test_home_page_can_save_a_POST_request(self):
	# 	request = HttpRequest()
	# 	request.method = 'POST'
	# 	request.POST[item_text] = 'A new list item' # 54, 55 - item_text WHAT is posted

	# 	response = home_page(request)

	# 	self.assertEqual(MyUser.object.count(), 1)
	# 	new_item = MyUser.object.first()
	# 	self.assertEqual(new_item.text, 'A new list item')

	# def test_home_page_redirects_after_POST(self):
	# 	request = HttpRequest()
	# 	request.method = 'POST'
	# 	request.POST[item_text] = 'A new list item' # 54, 55 - item_text WHAT is posted

	# 	response = home_page(request)

	# 	self.assertEqual(response.status_code, 302)
	# 	self.assertEqual(response['location'], '/')


# Unit tests


from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest 
from django.template.loader import render_to_string 
from booking.views import booking


class BookingPageTest(TestCase):
	# Test that url directs to the booking page
	def test_root_url_resolves_to_booking_page_view(self):
		found = resolve('/booking/')
		self.assertEqual(found.func, booking)

	
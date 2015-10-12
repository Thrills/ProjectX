from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest 
from django import forms
from django.template.loader import render_to_string 
from papers.views import home, paper_sub, review_sub, registration
from booking.forms import BookingForm
from booking.models import Delegate

class DelegateModelTest(TestCase):

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

		






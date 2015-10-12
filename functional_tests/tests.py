from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_homepage(self):
	# Check if homepage is working
		self.browser.get('http://localhost:8000')

		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('RESEARCH CONFERENCE', header_text)

		header_text = self.browser.find_element_by_tag_name('h3').text
		self.assertIn('The Stellenbosch Institute for Informatics and Software Management', header_text)

	def test_about(self):
	# Check if about page is working
		self.browser.get('http://localhost:8000/about') 

		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('About Us', header_text)

	def test_helppage(self):
	# Check if help page is working
		self.browser.get('http://localhost:8000/help')

		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Help Document', header_text)

		header_text = self.browser.find_element_by_tag_name('h3').text
		self.assertIn('Frequently Asked Questions', header_text)

	def test_footer(self):
	# Check if footer is working
		self.browser.get('http://localhost:8000') 

		header_text = self.browser.find_element_by_tag_name('h3').text
		self.assertIn('Stellenbosch', header_text)

	def test_login(self):
	# Check if log in is working
		self.browser.get('http://localhost:8000/login')

		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Login', header_text)

	def test_main(self):
	# Check if main.html is working
		self.browser.get('http://localhost:8000') 

		self.assertIn('SIISM Conference 2016', self.browser.title)

	def test_registration(self):
	# Check if registration is working
		self.browser.get('http://localhost:8000/registration') 

		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Create a Profile', header_text)	
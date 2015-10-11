from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_homepage(self):
	# Check if homepage is working
		self.browser.get('self.live_server_url') #p79

		self.assertIn('Welcome', self.browser.title)

		header_text = self.browser.find_element_by_tag_name('h1').header_text
		self.assertIn('RESEARCH CONFERENCE', header_text)

		header_text = self.browser.find_element_by_tag_name('h3').header_text
		self.assertIn('The Stellenbosch Institute for Informatics and Software Management', header_text)

	def test_registration(self):

		inputbox = self.browser.find_element_by_tag_id('')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter a to-do item'
		)

		inputbox.send_keys('')

		inputbox.send_keys(Keys.ENTER)

		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
				any(row.text == '1: Buy some' for row in rows)
		)




		self.fail('Finish the test!')







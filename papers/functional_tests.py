from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_Wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_homepage(self):
	# Check if homepage is working
		self.browser.get('http://localhost:8000')

		self.assertIn('Welcome', self.browser.title)
		self.fail('Finish the test!')

if __name__=='__main__':
	unittest.main(warnings='ignore')




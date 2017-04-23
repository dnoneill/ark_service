from django.test import TestCase
from .models import Minter
from .models import Ark

# Create your tests here.
class MinterModelTest(TestCase):
	fixtures = ['testdata.json']
	def test_repr(self):
		minter = Minter(name="test")
		test = minter.__repr__()
		self.assertEqual(test, "<Minter: test>")
	def test_ark_exists(self):
		ark_test = Minter._ark_exists(self, key='12345')
		self.assertEqual(ark_test, False)
	def test_mint(self):
		ark = Minter.mint(self, 2)
		
class ArkModelTest(TestCase):
	def test_repr(self):
		key = Ark(key="12345")
		test = key.__repr__()
		self.assertEqual(test, "<Ark: 12345>")
	def test_bind(self):
		url = Ark(url="http://127.0.0.1:8000")
		self.assertEqual(url.url, "http://127.0.0.1:8000")
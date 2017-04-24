from django.test import TestCase
from .models import Minter
from .models import Ark
from django.conf import settings

# Create your tests here.
class MinterModelTest(TestCase):
	#fixtures = ['testdata.json']
	def test_repr(self):
		minter = Minter(name="test")
		test = minter.__repr__()
		self.assertEqual(test, "<Minter: test>")
	def test_ark_exists(self):
		minter = Minter()
		minter.save()
		ark = Ark(key="12345", minter=minter)
		ark.save()
		ark_test = minter._ark_exists(key='12345')
		self.assertEqual(ark_test, True)
	def test_mint(self):
		minter = Minter(template = "Test")
		minter.save()
		ark = minter.mint(2)
		self.assertEqual(len(ark), 2)
		self.assertIn(ark[0],"12345/lib-") 
		self.assertIn(ark[1],"12345/lib-")
class ArkModelTest(TestCase):
	def test_repr(self):
		key = Ark(key="12345")
		test = key.__repr__()
		self.assertEqual(test, "<Ark: 12345>")
	def test_bind(self):
		minter = Minter(prefix="test")
		minter.save()
		ark = Ark(minter=minter, key="54321")
		ark.save()
		url = ark.bind("http://127.0.0.1:8000")
		self.assertEqual(ark.url, "http://127.0.0.1:8000/ark:/12345/test/54321")
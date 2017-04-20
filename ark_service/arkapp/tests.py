from django.test import TestCase
from .models import Minter
from .models import Ark

# Create your tests here.
class MinterModelTest(TestCase):
	def test_repr(self):
		name = Minter(name="test")
		test = name.__repr__()
		self.assertEqual(test, "Minter: test")
	'''def test_ark_exists(self, key):
		exists = Minter(key="1234")
		print(exists)
		print(exists._ark_exists(self, key))'''

class ArkModelTest(TestCase):
	def test_repr(self):
		key = Ark(key="12345")
		test = key.__repr__()
		self.assertEqual(test, "Ark: 12345")

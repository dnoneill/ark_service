from django.test import TestCase
from .models import Minter
from .models import Ark

# Create your tests here.
class MinterModelTest(TestCase):
	def test_repr(self):
		name = Minter(name="test")
		test = name.__repr__()
		self.assertEqual(test, "Minter: test")
	def test_ark_exists(self):
		ark_test = Minter._ark_exists(self, 1234)
		self.assertEqual(ark_test, False)
	def test_mint(self):
		ark = Minter.mint(self, 2)
		print(ark)

class ArkModelTest(TestCase):
	def test_repr(self):
		key = Ark(key="12345")
		test = key.__repr__()
		self.assertEqual(test, "Ark: 12345")

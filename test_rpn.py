import unittest

import rpn

class TestBasics(unittest.Testcase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate("5 3 -")
		self.assertEqual(2, result)
	def test_multiply(self):
		result = rpn.calculate("3 4 *")
		self.assertEqual(12, result)
	def test_divide(self):
		result = rpn.calculate("6 2 /")
		self.assertEqual(3, result)

	def test_toomanythings(self):
		with self.assertRaises(TypeError):
			rpn.calculate("1 2 3 +") 

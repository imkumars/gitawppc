#!/usr/bin/env python3

import unittest
from ticky_check import unpack_and_format_usr_list


class TestFormatFunction(unittest.TestCase):
	
	#1 test case
	def test_case_one(self):
		test_case = [("user1", [1, 2]), ("user2", [3, 4])]
		expected = [("user1", 1, 2), ("user2", 3, 4)]
		
		self.assertEqual(unpack_and_format_usr_list(test_case), expected)
		

unittest.main()
import unittest
import os
import json
from PyBytes import ByteUtil



class TestPyBytes(unittest.TestCase):

    def setUp(self):

        parent_dir = os.path.dirname(__file__)
        with open(os.path.join(parent_dir, 'ascii.json')) as fp:
            self.ascii_bytes = json.load(fp)

    def test_print_byte(self):
        """
        Test to ensure that each byte list matches the byte from the ascii table.
        :return: True(pass) if lists are equal, False otherwise
        """
        for key, value in self.ascii_bytes.iteritems():
            byte = ByteUtil.ascii_byte(int(key))
            self.assertEqual(byte, value)

    def test_is_odd(self):
        self.assertTrue(ByteUtil.is_odd(ByteUtil.ascii_byte(123)))


    def test_is_even(self):
        self.assertFalse(ByteUtil.is_odd(ByteUtil.ascii_byte(102)))



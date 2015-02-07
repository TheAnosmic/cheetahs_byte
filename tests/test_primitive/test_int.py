from unittest import TestCase

from primitive.int_ import Int


class TestInt(TestCase):
    def test_int_throw(self):
        self.assertRaises(ValueError, Int, -1)
        self.assertRaises(ValueError, Int, 0xFFFFFFFF + 1)
        self.assertRaises(ValueError, Int, 'asdf')

    def test_int_build(self):
        i = Int(0xAE)
        exp = '\x00\x00\x00\xAE'
        self.assertEqual(i.build(), exp)
        i = Int(0xFEDCBA98)
        exp = '\xFE\xDC\xBA\x98'
        self.assertEqual(i.build(), exp)
        i = Int(0)
        exp = '\x00\x00\x00\x00'
        self.assertEqual(i.build(), exp)
        i = Int(0xFFFFFFFF)
        exp = '\xFF\xFF\xFF\xFF'
        self.assertEqual(i.build(), exp)
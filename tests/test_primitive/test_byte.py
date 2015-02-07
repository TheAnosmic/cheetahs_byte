from unittest import TestCase

from primitive.byte import Byte


class TestByte(TestCase):
    def test_byte_build(self):
        self.assertEqual('\x00', Byte(0).build())
        self.assertEqual('\x00', Byte('\x00').build())
        self.assertEqual('\x52', Byte(0x52).build())
        self.assertEqual('\x52', Byte('\x52').build())

    def test_byte_throw(self):
        self.assertRaises(ValueError, Byte, '')
        self.assertRaises(ValueError, Byte, 'aa')
        self.assertRaises(ValueError, Byte, -1)
        self.assertRaises(ValueError, Byte, 256)
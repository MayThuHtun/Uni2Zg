
# -*- coding: utf-8 -*-
import unittest
import uni2zg

class TestZG2UNI(unittest.TestCase):

    def test_article_consonant(self):
        zawgyi = u'''အေထြအေထြဆိုင္ရာ'''
        unicode = u'''အထွေအထွေဆိုင်ရာ'''
        result = uni2zg.convert(unicode)
        self.assertEqual(zawgyi, result, "Failed converting Article One")


if __name__ == "__main__":
    unittest.main()

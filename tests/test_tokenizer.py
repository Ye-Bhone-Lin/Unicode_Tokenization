import unittest

class TestSyllableTokenize(unittest.TestCase):
    def test_syllable_tokenize(self):
        self.assertEqual(syllable_tokenize('တွေ့ရတာဝမ်းသာပါတယ်'), ' တွေ့ ရ တာ ဝမ်း သာ ပါ တယ်')
        self.assertEqual(syllable_tokenize('မင်းကလည်းကွာ'), ' မင်း က လည်း ကွာ')

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False) 


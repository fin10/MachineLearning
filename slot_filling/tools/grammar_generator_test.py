import unittest

from tools.grammar_generator import GrammarGenerator


class GrammarGeneratorTest(unittest.TestCase):
    def test_alternate(self):
        test = ['good {morning|afternoon|evening}']
        expected = ['good morning',
                    'good afternoon',
                    'good evening']
        actual = GrammarGenerator.alternate(test)
        self.assertListEqual(expected, actual)

    def test_replace(self):
        test = ['i\'m looking for a restaurant (<test_type>)[type] restaurant']
        expected = ['i\'m looking for a restaurant (korean)[type] restaurant',
                    'i\'m looking for a restaurant (chinese)[type] restaurant']
        slots = {
            'test_type': {'korean', 'chinese'}
        }

        actual = GrammarGenerator.replace(test, slots)
        self.assertListEqual(expected, actual)

import unittest
from app.models import Source

class SourceTest:
    '''
    test source class and its behaviours
    '''
    def setUp(self):
        self.new_source = Source(123, 'kerry-kogei', 'nourl', 'female')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source))

import unittest
from app.models import Source

class MovieTest(unittest.TestCase):

    def setUp(self):
        self.new_source = Source('cnn','cnn','Elections set for 2020','https://edition.cnn.com/','general','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
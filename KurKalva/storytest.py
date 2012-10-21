import unittest
import storyteller

class TestSequenceFunctions(unittest.TestCase):

   def setUp(self):
      pass
      #storyteller.setup()

   def test_addStory(self):
      storyteller.addStory("test")
      self.assertEqual(storyteller.returnStory("test")['title'],"test")


if __name__ == '__main__':
   unittest.main()

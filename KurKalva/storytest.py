import unittest
import storyteller

class TestSequenceFunctions(unittest.TestCase):

   def setUp(self):
      storyteller.setup()

   def test_addStory(self):
      self.newtitle = "This is the never ending story"
      storyteller.addStory(self.newtitle)
      self.assertEqual(storyteller.returnStory(self.newTitle)['title'], self.newtitle)


if __name__ == '__main__':
   unittest.main()

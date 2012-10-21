import unittest
import storyteller

class TestSequenceFunctions(unittest.TestCase):

   def setUp(self):
      self.newtitle = 'This is the story that never ends'

   def test_addStory(self):
      storyteller.addStory(self.newtitle)
      self.assertEqual(storyteller.returnStory(self.newTitle)['title'], self.newtitle)


if __name__ == '__main__':
   unittest.main()

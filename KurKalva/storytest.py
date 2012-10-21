import unittest
import storyteller

class TestSequenceFunctions(unittest.TestCase):

   def setUp(self):
      pass
      #storyteller.setup()

   def test_addStory(self):
      storyteller.addStory("test")
      self.assertEqual(storyteller.returnStory("test")['title'],"test")

   def test_addLine(self):
      storyteller.addStory("test")
      storyteller.addLine("test", "testline")
      lines = storyteller.returnStory("test")['lines']
      hold = lines[0]
      self.assertEqual(hold, "testline")

if __name__ == '__main__':
   unittest.main()

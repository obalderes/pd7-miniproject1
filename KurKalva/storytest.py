import unittest
import storyteller

class TestSequenceFunctions(unittest.TestCase):

   def setUp(self):
      pass
      #storyteller.setup()

   def tearDown(self):
      storyteller.wipeDatabase()

   def test_addStory(self):
      storyteller.addStory("test")
      self.assertEqual(storyteller.returnStory("test")['title'],"test")

   def test_addLine(self):
      storyteller.addStory("test")
      storyteller.addLine("test", "testline")
      lines = storyteller.returnStory("test")['lines']
      self.assertEqual(lines[0], "testline")

   def test_removeStory(self):
      storyteller.addStory("test")
      storyteller.removeStory("test")
      self.assertEqual(storyteller.returnStory("test"), None)

   def test_returnStory(self):
      storyteller.addStory("test")
      storyteller.addStory("hello")
      self.assertEqual(storyteller.returnStory("test")['title'], "test")

   def test_returnStories(self):
      storyteller.wipeDatabase()
      storyteller.addStory("test")
      storyteller.addStory("hello")
      storyteller.addStory("numba3")
      numTitles = storyteller.returnStories()
      self.assertEqual(len(numTitles), 3)

   def test_wipeDatabase(self):
      storyteller.addStory("test")
      storyteller.addStory("hello")
      storyteller.addStory("numba3")
      storyteller.wipeDatabase()
      titles = storyteller.returnStories()
      numtitles = len(titles)
      self.assertEqual(numtitles, 0)

if __name__ == '__main__':
   unittest.main()

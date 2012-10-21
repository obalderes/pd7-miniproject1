import unittest
import storyteller

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        storyteller.setup()

    def test_addStory(self):
        newtitle = 'This is the story that never ends'
        storyteller.addStory(newtitle)
        self.assertEqual(storyteller.returnStory()['title'], newtitle)


if __name__ == '__main__':
    unittest.main()

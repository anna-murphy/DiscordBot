import point_counter as p
import unittest

class TestPointCounter(unittest.TestCase):

    FILE_PATH = "data.dat"

    def test_constructor(self):
        PC = p.Point_Counter(self.FILE_PATH)
        self.assertIsNotNone(PC)
        self.assertEqual(PC.file_path, self.FILE_PATH)
        self.assertEquals(len(PC.point_data), 4)

    def test_str(self):
        pass

    def test_update(self):
        pass

    def test_handle (self):
        pass

if __name__ == "__main__":
    unittest.main()

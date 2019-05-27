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
        PC = p.Point_Counter(self.FILE_PATH)
        PC_string = PC.__str__()
        self.assertTrue(PC_string.startswith("```"))
        self.assertTrue(PC_string.endswith("\n```"))
        self.assertTrue("Skitter: 6\n" in PC_string)
        self.assertTrue("TattleTale: 9\n" in PC_string)
        self.assertTrue("Grue: 2\n" in PC_string)
        self.assertTrue("bob: 12\n" in PC_string)

    def test_update(self):
        PC = p.Point_Counter(self.FILE_PATH)
        self.assertEquals(PC.point_data["Skitter"], 6)
        PC.update("Skitter", 2)
        self.assertEquals(PC.point_data["Skitter"], 8)
        PC.update("Skitter", -2)
        self.assertEquals(PC.point_data["Skitter"], 6)

    def test_handle (self):
        pass

if __name__ == "__main__":
    unittest.main()

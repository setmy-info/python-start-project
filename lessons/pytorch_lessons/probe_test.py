import unittest
import torch


class Test(unittest.TestCase):

    def test_torch_rand(self):
        tensor = torch.rand(5, 3)
        print(tensor)
        print(torch.cuda.is_available())
        # self.assertEqual(str(tensor), 'Imre')


if __name__ == "__main__":
    unittest.main()

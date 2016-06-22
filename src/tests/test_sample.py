from template.sample.sample import Sample

import unittest
import logging


class Test(unittest.TestCase):

    def testSample(self):
        sample = Sample()
        sample.output()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    unittest.main()

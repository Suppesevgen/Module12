import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        a = runner.Runner("Евген")
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    def test_run(self):
        a = runner.Runner("Евген")
        for i in range(10):
            a.run()
        self.assertEqual(a.distance, 100)

    def test_challenge(self):
        a = runner.Runner("Евген")
        b = runner.Runner("Теодор")
        for i in range(10):
            a.walk()
            b.run()
        self.assertNotEqual(a.distance, b.distance)

if __name__ == "__main":
    unittest.main()
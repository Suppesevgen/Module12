import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Запускаем тест")

    def test_walk(self):
        a = runner.Runner("Евген")
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    @unittest.skipIf(is_frozen, "Запуск теста")
    def test_run(self):
        a = runner.Runner("Евген")
        for i in range(10):
            a.run()
        self.assertEqual(a.distance, 100)

    @unittest.skipIf(is_frozen, "Запуск теста")
    def test_challenge(self):
        a = runner.Runner("Евген")
        b = runner.Runner("Теодор")
        for i in range(10):
            a.walk()
            b.run()
        self.assertNotEqual(a.distance, b.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")

    def test_walk(self):
        a = runner.Runner("Евген")
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        a = runner.Runner("Евген")
        for i in range(10):
            a.run()
        self.assertEqual(a.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        a = runner.Runner("Евген")
        b = runner.Runner("Теодор")
        for i in range(10):
            a.walk()
            b.run()
        self.assertNotEqual(a.distance, b.distance)


if __name__ == "__main":
    unittest.main()

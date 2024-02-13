import unittest
from activities import eat, nap
class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """"Eating beef should give you giant belly"""
        self.assertEqual(
            eat("beef", is_healthy=True),
            "I'm eating beef because, I need belly muscle"
        )
    def test_eat_unhealthy(self):
        """"Eating potato would give you a big biceps"""
        self.assertEqual(
            eat("potato", is_healthy=False),
            "I'm eating potato because, I need biceps"
        )
    def test_short_nap(self):
        """"Short sleep is enough"""
        self.assertEqual(
            nap(1),
            "Sleep is for the weak, its only 1 hour!"
        )
    def test_long_nap(self):
        """"After long sleep you are more tired"""
        self.assertEqual(
            nap(3),
            "I've slept for too long, It's been over 3 hours"
        )

if __name__ == "__main__":
    unittest.main()


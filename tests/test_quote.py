import unittest

from app.main import quote


class QuoteTest(unittest.TestCase):
    def test_minimum_fee(self) -> None:
        self.assertEqual(quote(100, "aud")["fee"], 30)

    def test_total(self) -> None:
        q = quote(10_000, "aud")
        self.assertEqual((q["fee"], q["total"], q["currency"]), (175, 10_175, "AUD"))


if __name__ == "__main__":
    unittest.main()

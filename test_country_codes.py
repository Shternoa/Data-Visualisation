import unittest
from countries_code import get_country_code


class TestCodes(unittest.TestCase):
    """Тест для функции contries_code()"""

    def test_known_city(self):
        country_name = 'Ukraine'
        expected_code = 'ua'
        code = get_country_code(country_name)
        self.assertEqual(code, expected_code)

    def test_unknown_city(self):
        """Проверка получения кода для неизвестной страны"""
        country_name = None
        code = get_country_code(country_name)
        self.assertIsNone(code)


if __name__ == '__main__':
    unittest.main()

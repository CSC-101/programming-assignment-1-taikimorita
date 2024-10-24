import data
import hw1
import unittest
from hw1 import Price, add_prices, short_lists, below_pay_average

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_basic(self):
        self.assertEqual(hw1.vowel_count("Hello World"), 3)

    def test_vowel_count_empty(self):
        self.assertEqual(hw1.vowel_count(""), 0)

    # Part 2
    def test_short_lists_basic(self):
        self.assertEqual(hw1.short_lists([[1, 2], [3], [4, 5], [6, 7]]), [[1, 2], [4, 5], [6, 7]])

    def test_short_lists_empty(self):
        self.assertEqual(hw1.short_lists([]), [])

    # Part 3
    def test_ascending_pairs_basic(self):
        self.assertEqual(hw1.ascending_pairs([[2, 1], [4, 3], [5]]), [[1, 2], [3, 4], [5]])

    def test_ascending_pairs_no_pairs(self):
        self.assertEqual(hw1.ascending_pairs([[1, 2, 3], [4]]), [[1, 2, 3], [4]])

    # Part 4
    def test_add_prices_basic(self):
        price1 = Price(8, 25)
        price2 = Price(2, 75)
        self.assertEqual(add_prices(price1, price2), Price(11, 00))

    def test_add_prices_with_carry(self):
        price1 = Price(5, 90)
        price2 = Price(2, 25)
        self.assertEqual(add_prices(price1, price2), Price(8, 15))

    # Part 5
    def test_rectangle_area_basic(self):
        rect = hw1.Rectangle(hw1.Point(1, 1), hw1.Point(4, 5))
        self.assertEqual(hw1.rectangle_area(rect), 12)

    def test_rectangle_area_negative(self):
        rect = hw1.Rectangle(hw1.Point(5, 5), hw1.Point(1, 1))
        self.assertEqual(hw1.rectangle_area(rect), 16)

    # Part 6
    def test_books_by_author_basic(self):
        book1 = hw1.Book("Book One", "Author A")
        book2 = hw1.Book("Book Two", "Author B")
        books = [book1, book2]
        self.assertEqual(hw1.books_by_author("Author A", books), [book1])

    def test_books_by_author_no_books(self):
        books = []
        self.assertEqual(hw1.books_by_author("Author A", books), [])

    # Part 7
    def test_circle_bound_basic(self):
        rect = hw1.Rectangle(hw1.Point(0, 0), hw1.Point(2, 2))
        circle = hw1.circle_bound(rect)
        self.assertEqual(circle.center.x, 1)
        self.assertEqual(circle.center.y, 1)
        self.assertAlmostEqual(circle.radius, 1.41421356237, places=5)

    def test_circle_bound_negative_coordinates(self):
        rect = hw1.Rectangle(hw1.Point(-1, -1), hw1.Point(1, 1))
        circle = hw1.circle_bound(rect)
        self.assertEqual(circle.center.x, 0)
        self.assertEqual(circle.center.y, 0)
        self.assertAlmostEqual(circle.radius, 1.41421356237, places=5)

    # Part 8
    def test_below_pay_average_basic(self):
        emp1 = hw1.Employee("Alice", 60000)
        emp2 = hw1.Employee("Bob", 50000)
        emp3 = hw1.Employee("Charlie", 70000)
        employees = [emp1, emp2, emp3]

        self.assertEqual(below_pay_average(employees), ["Bob"])

    def test_below_pay_average_empty(self):
        employees = []
        self.assertEqual(hw1.below_pay_average(employees), [])

if __name__ == '__main__':
    unittest.main()

import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(input: str) -> int:
    """
    This function takes a string and returns the number of vowels (a, e, i, o, u) in the string.
    The function considers both lowercase and uppercase vowels.

    Parameters:
    input (str): The input string.

    Returns:
    int: The count of vowels in the string.
    """
    count = 0
    for char in input:
        if char in "AEIOUaeiou":
            count += 1
    return count

# Part 2
def short_lists(lists: list[list[int]]) -> list[list[int]]:
    """
    Returns a new list containing only the elements of the input list
    that have a length of 2.

    :param lists: A list of lists of integers.
    :return: A list of lists, each having a length of 2.
    """
    return [lst for lst in lists if len(lst) == 2]

# Part 3
def ascending_pairs(input:list[list[int]]) -> list:
    """
    This function takes a list of lists of integers and returns a new list where
    any sublist with exactly 2 elements has its elements sorted in ascending order.
    Sublists of other lengths remain unchanged.

    Parameters:
    input (List[List[int]]): A list of lists of integers.

    Returns:
    sublist[List[int]]: A new list where sublists of length 2 are sorted in ascending order.
    """
    sublist = []
    for i in input:
        if len(i) == 2:
            sublist.append(sorted(i))
        else:
            sublist.append(i)
    return sublist

# Part 4
class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents

    def __eq__(self, other: 'Price') -> bool:
        return (self.dollars == other.dollars) and (self.cents == other.cents)

    def __repr__(self) -> str:
        return f'${self.dollars}.{self.cents:02d}'

def add_prices(price1: Price, price2: Price) -> Price:
    """
    Adds two Price objects and returns a new Price object.
    Ensures that the total cents are not above 99.

    :param price1: The first Price object.
    :param price2: The second Price object.
    :return: A new Price object representing the sum.
    """
    total_cents = price1.cents + price2.cents
    total_dollars = price1.dollars + price2.dollars + (total_cents // 100)  # Carry over dollars
    total_cents = total_cents % 100  # Remainder cents
    return Price(total_dollars, total_cents)

# Part 5
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

def rectangle_area(rect: Rectangle) -> int:
    """
    This function takes a Rectangle object as input and returns the area of the rectangle.
    The rectangle is assumed to be axis-aligned.

    Parameters:
    rect (Rectangle): The input Rectangle object with top-left and bottom-right points.

    Returns:
    int: The area of the rectangle.
    """
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.bottom_right.y - rect.top_left.y

    return abs(width * height)

# Part 6
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"{self.title} by {self.author}"

def books_by_author(author_name: str, books: list[Book]) -> list[Book]:
    """
    This function takes an author's name and a list of Book objects as input and returns a list of
    books written by the specified author.

    Parameters:
    author_name (str): The name of the author to filter by.
    books (list[Book]): A list of Book objects.

    Returns:
    list[Book]: A list of Book objects written by the specified author.
    """
    return [book for book in books if book.author == author_name]

# Part 7
import math

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius})"

def circle_bound(rect: Rectangle) -> Circle:
    """
    This function takes a Rectangle object as input and returns a Circle object that represents
    the smallest bounding circle for the rectangle.

    Parameters:
        rect (Rectangle): The input Rectangle object.

    Returns:
        Circle: A Circle object representing the bounding circle of the rectangle.
    """
    center_x = (rect.top_left.x + rect.bottom_right.x) / 2
    center_y = (rect.top_left.y + rect.bottom_right.y) / 2
    center = Point(center_x, center_y)

    radius = math.sqrt((rect.top_left.x - center_x) ** 2 + (rect.top_left.y - center_y) ** 2)

    return Circle(center, radius)

# Part 8
class Employee:
    def __init__(self, name: str, pay: float):
        self.name = name
        self.pay = pay


def below_pay_average(employees: list) -> list[str]:
    """
    Returns a list of names of employees who earn less than the average pay.

    :param employees: A list of Employee objects.
    :return: A list of names of employees below the average pay.
    """
    if not employees:
        return []

    average_pay = sum(emp.pay for emp in employees) / len(employees)
    return [emp.name for emp in employees if emp.pay < average_pay]

from typing import List

def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and return an even list.

    Args:
        int_list: A list of integer.
    Returns:
        A list of even integers.
    """
    return [i for i in int_list if i % 2 == 0]

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in a list of integers.

    Args:
        even_int_list: A list of even integers.

    Returns:
        The sum of the squares of all even numbers in the list.
    """
    return sum(i**2 for i in even_int_list)

def main():
    # Example list
    int_list = [58, 6, -22, 91, 33, 49, 44, 63, -79, 12]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

# Boilerplate code
if __name__ == "__main__":
    main()
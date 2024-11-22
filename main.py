from typing import List, Tuple, Dict

def merge_sort_dict_by_value_desc(dictionary: Dict[str, int]) -> Dict[str, int]:
    """
    Sorts a dictionary by its values in descending order using the merge sort algorithm.

    Args:
        dictionary (Dict[str, int]): The dictionary to sort.

    Returns:
        Dict[str, int]: A new dictionary sorted by the values in descending order.
    """
    # Convert dictionary to a list of tuples
    items = list(dictionary.items())

    # Sort the items based on the values in descending order
    sorted_items = merge_sort(items, key=lambda x: x[1])  # Negate the value for descending order

    # Convert the sorted list of tuples back into a dictionary
    return dict(sorted_items)

def merge_sort(array: List[Tuple[str, int]], key=lambda x: x) -> List[Tuple[str, int]]:
    """
    Sorts a list of tuples using the merge sort algorithm with a custom key function.

    Args:
        array (List[Tuple[str, int]]): The list of tuples to sort.
        key (function): A function that extracts the sort key from each tuple.

    Returns:
        List[Tuple[str, int]]: A sorted list of tuples.
    """
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left_half = merge_sort(array[:middle], key=key)
    right_half = merge_sort(array[middle:], key=key)

    return _merge(left_half, right_half, key=key)

def _merge(left: List[Tuple[str, int]], right: List[Tuple[str, int]], key=lambda x: x) -> List[Tuple[str, int]]:
    """
    Merges two sorted lists into a single sorted list with a custom key function.

    Args:
        left (List[Tuple[str, int]]): The first sorted list.
        right (List[Tuple[str, int]]): The second sorted list.
        key (function): A function that extracts the sort key from each tuple.

    Returns:
        List[Tuple[str, int]]: A merged sorted list of tuples.
    """
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if key(left[i]) >= key(right[j]):  # Flip comparison for descending order
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_counts = {}

    for unique_char in ''.join(set(text.lower())):
        if unique_char.isalpha():
            char_counter = 0
            for letter in text.lower():
                if unique_char == letter:
                    char_counter += 1
            letter_counts[unique_char] = char_counter
    return letter_counts

def main():
    address = 'books/frankenstein.txt'
    with open(address) as f:
        file_contents = f.read()
        print(f"--- Begin report of {address} ---\n")
        print(f"Number of words found in the document: {count_words(file_contents)}.\n")
        sorted_char_dict = merge_sort_dict_by_value_desc(count_letters(file_contents))
        for key, value in sorted_char_dict.items():
            print(f"The '{key}' character was found {value} times")
    print(f"--- End report ---")

# This ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
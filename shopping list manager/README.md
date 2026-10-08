# Week 7 Assignment: Hands-On Lab — Shopping List Manager

## File Descriptions
- `list_warmup.py`: Demonstrates basic Python list operations including index access, appending, removing items, and checking list length.
- `shopping_list.py`: An interactive CLI program that allows users to add, remove, display, and manage items in a shopping list safely.
- `list_report.py`: Processes a predefined list of items to output a numbered list, count items with names longer than 4 characters, and identify the longest item name.

## Reflection
It is safer to check if an item exists using the `in` keyword before calling `.remove()` because calling `.remove()` on an item that is not present in the list raises a `ValueError` and terminates the program abruptly. Checking membership beforehand prevents runtime crashes and allows the program to gracefully inform the user that the item was not found.
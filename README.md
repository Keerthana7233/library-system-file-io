# Library System with File I/O

A simple Python library management system that demonstrates object-oriented programming, data structures, and CSV file persistence.

## Features

- Create and manage books
- Register library members
- Check books out to members
- Return borrowed books
- List available books
- Save the library catalog to a CSV file
- Load the catalog from a CSV file
- Preserve book availability between program runs

## Classes

### Book

Stores:

- ISBN
- Title
- Author
- Availability status

### Member

Stores:

- Member ID
- Name
- Borrowed books

### Library

Provides:

- `add_book()`
- `register_member()`
- `checkout()`
- `checkin()`
- `list_available()`
- `save_catalog()`
- `load_catalog()`

## Files

- `library.py` - Main Python program
- `catalog.csv` - Persistent library catalog
- `README.md` - Project documentation

## How to Run

Open a terminal in the project folder and run:

```bash
python library.py
books = {
    "B101": {"title": "Python Programming", "author": "A", "copies": 4},
    "B102": {"title": "Data Structures", "author": "B", "copies": 2},
    "B103": {"title": "Operating Systems", "author": "C", "copies": 5},
    "B104": {"title": "Database Systems", "author": "D", "copies": 1}
}

# 1. Display books having fewer than 3 copies
print("Books with fewer than 3 copies:")
for book_id, details in books.items():
    if details["copies"] < 3:
        print(book_id, "-", details["title"], "-", details["copies"], "copies")


# 2. Add a new book
books["B105"] = {
    "title": "Machine Learning",
    "author": "E",
    "copies": 3
}

# Update copies of an existing book
books["B102"]["copies"] = 4

# Remove a book
del books["B104"]

print("\nUpdated Book Records:")
for book_id, details in books.items():
    print(book_id, ":", details)


# 3. Create a set of all authors
authors = {details["author"] for details in books.values()}

print("\nUnique Authors:")
print(authors)
print("Number of Unique Authors:", len(authors))


# 4. Sort book IDs by number of available copies
sorted_book_ids = sorted(
    books.keys(),
    key=lambda book_id: books[book_id]["copies"]
)

print("\nBook IDs Sorted by Copies:")
print(sorted_book_ids)


# 5. Create a tuple of titles having at least 3 copies
titles_with_3_or_more = tuple(
    details["title"]
    for details in books.values()
    if details["copies"] >= 3
)

print("\nTitles with at least 3 copies:")
print(titles_with_3_or_more)
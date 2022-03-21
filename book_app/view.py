def books_view(books):
    print('=' * 50)
    print('Book ID'.ljust(10), 'Name'.ljust(35), 'Author'.ljust(25))
    for book in books:
        book_id, name, author = book
        print(str(book_id).ljust(10), name.ljust(35), author.ljust(25))
    print('=' * 50, '\n')

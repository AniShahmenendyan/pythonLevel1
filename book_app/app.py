import sys

from view import books_view
from queries import add_user, get_user, get_books, add_to_favorites, remove_favorites, get_favorites

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'signup':
        email = ''
        while email == '':
            email = input("Please type your email: \n")

        password = ''
        while password == '':
            password = input("Please type your password: \n")

        firstname = ''
        while firstname == '':
            firstname = input("Please type your firstname: \n")

        lastname = ''
        while lastname == '':
            lastname = input("Please type your lastname: \n")

        user_added = add_user(firstname, lastname, email, password)

        if user_added:
            print('User has been signed up successfully!!!')
        else:
            print('Something went wrong!!!')

    elif len(sys.argv) == 2 and sys.argv[1] == 'login':

        email = ''
        while email == '':
            email = input("Please type your email: \n")

        password = ''
        while password == '':
            password = input("Please type your password: \n")

        user = get_user(email, password)

        if user is None:
            print('Invalid username or password!')
            sys.exit(1)

        if user:
            user_id, email = user
            print(f'Hi {email}, you are logged in!\n')

            while True:
                allowed_commands = ['add', 'remove', 'books', 'favorites', 'logout']

                print('Type books to see all available books.')
                print('Type favorite to see all favorite books.')
                print('Type add to add the book to favorite books.')
                print('Type remove to delete the book from favorite books.')
                print('Type logout to logout.\n')

                command_msg = f'Type [{",".join(allowed_commands)}]: '
                command = input(command_msg)
                command = command.strip()

                while command not in allowed_commands:
                    print('No such command!\n')
                    command = input(command_msg)

                if command in allowed_commands:
                    if command == 'books':
                        books = get_books()

                        books_view(books)

                    elif command == 'add':
                        book_id = ''
                        while book_id == '' or not book_id.isnumeric():
                            book_id = input("Please type book id: \n")

                        added = add_to_favorites(book_id, user_id)
                        if added:
                            print('Book was added to favorite list.\n')
                        else:
                            print('Book ID was incorrect or it was already in your favorite list.')

                    elif command == 'remove':

                        book_id = ''
                        while book_id == '' or not book_id.isnumeric():
                            book_id = input("Please type book id: \n")

                        removed = remove_favorites(book_id, user_id)
                        if removed:
                            print('Book was removed from favorite list.\n')
                        else:
                            print('Book ID was incorrect.')

                    elif command == 'favorites':
                        favorites = get_favorites(user_id)

                        if len(favorites) == 0:
                            print('No favorite books. Type add to add them.\n')
                            continue

                        books_view(favorites)

                    elif command == 'logout':
                        print('bye!')
                        sys.exit(1)
    else:
        print('Invalid command!')
        sys.exit(1)

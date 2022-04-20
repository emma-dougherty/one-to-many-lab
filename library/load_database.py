from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author1 = Author("Jacqueline","Wilson")
author_repository.save(author1)
author2 = Author("Sue","Townsend")
author_repository.save(author2)
author3 = Author("Roald","Dahl")
author_repository.save(author3)

book1 = Book("Tracy Beaker",author1,1991)
book_repository.save(book1)
book2 = Book("The Secret Diary of Adrian Mole, Aged 13 3/4",author2,1982)
book_repository.save(book2)
book3 = Book("Fantastic Mr Fox",author3,1970)
book_repository.save(book3)
book4 = Book("The Twits",author3,1980)
book_repository.save(book4)
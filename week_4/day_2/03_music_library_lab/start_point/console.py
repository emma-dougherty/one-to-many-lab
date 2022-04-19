from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()


artist1 = Artist('Cher')
artist_repository.save(artist1)
artist2 = Artist('Michael Jackson')
artist_repository.save(artist2)
artist3 = Artist('Michael Bolton')
artist_repository.save(artist3)

album1 = Album('Believe','Pop',artist1)
album_repository.save(album1)
album2 = Album('Thriller','Pop',artist2)
album_repository.save(album2)
album3 = Album('Bad','Pop',artist2)
album_repository.save(album3)
album4 = Album('Soul Provider','Soul',artist3)
album_repository.save(album4)

# artist_list = artist_repository.select_all()
# for artist in artist_list:
#     print(artist.__dict__)

# album_list = album_repository.select_all()
# for album in album_list:
#     print(album.__dict__)


print(album_repository.select(31))


# Postico Query
# SELECT * FROM albums as al
# INNER JOIN artists as art
# on al.artist_id = art.id

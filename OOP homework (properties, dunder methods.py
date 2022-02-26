# 1. Create an Atom class. We will have predefined atoms for it, which are C - carbon, N - nitrogen, H - hydrogen,
# O - oxygen and P - phosphorus.
#     a) Now, the class has an instance variable called "name".
#     b) If you create an object with a name other than the 5 atoms mentioned, you should get an exception. But not any
#     kind of exception. This exception will be something that we have defined. So, define an exception class called
#     UnknownAtom. This must give us a detailed explanation why it is raised.
#     c) Define a new class called Molecule. The molecule has an instance variable, which is a list.
#     d) implement the __add__ method for our Atom class. Adding two atoms will return, you've guessed it, a Molecule!
#     e) We can also add an atom to a molecule. So implement that functionality as well!
#     f) Finally, do some cosmetic stuff, like implement the __str__ method for both of our classes.
# If you're into chemistry, feel free to add some logic like keeping charges of each atom, tracking valency and raising
# an error if two atoms can't make a molecule.

# Ստեղծել Atom կլաս։ Կլասի մեջ պետք է ունենանք 5 սահմանված ատոմ՝ C ածխածին, N ազոտ, H ջրածին, O թթվածին և P ֆոսֆոր։
#     a) Կլասը պետք է ունենա "name" կոչվող instance attribute
#     b) Եթե փորձենք ատոմ ստեղծել, որը չկա մեր ցուցակի մեջ, պետք է ստանանք exception։ Ստեղծել UnknownAtom կոչվող
#     exception, որը կստանանք, եթե վերը նշված դեպքը լինի։
#     c) Ստեղծել Molecule կլաս։ Մոլեկուլն ունի մեկ instance attribute, որը list է։
#     d) Սահմանելով գումարման օպերատորը, այնպես անել, որ երկու ատոմ իրար գումարելիս ստանանք մոլեկուլ:
#     e) Մոլեկուլին նույնպես պետք է կարողանանք ատոմ գումարել։ Դա նույնպես սահմանել։
#     f) Վերջապես, սահմանել __str__, __repr__ այս ֆունկցիաներից մեկը մեր բոլոր կլասերի համար, որպեսզի որպես սթրինգ
#     ներկայացումը գեղեցկանա
# Լրացուցիչ, եթե քիմիայի սիրահար եք, կարող եք ատոմներին ավելացնել լիցքեր, սահմանել վալենտականությունը և դրանց հիման վրա
# փոփոխել գումարման տրամաբանությունը։

class UnknownAtom(Exception):
    def __init__(self, message='Atom is not from our list'):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class Atom:
    __atoms = ('C', 'N', 'H', 'O', 'P')

    def __init__(self, name):
        if name not in self.__atoms:
            raise UnknownAtom(f'{name} is not Atom')
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        raise ValueError('it is read only property')

    def __add__(self, other):
        if type(other) != Atom:
            raise TypeError
        return Molecule([self.name, other.name])

    def __str__(self):
        return f'Atom: {self.name}'


class Molecule:
    def __init__(self, atoms):
        if type(atoms) != list or len(atoms) <= 1:
            raise TypeError

        self.atoms = atoms

    def __add__(self, other):
        if type(other) == Atom:
            self.atoms.append(other.name)
            return self
        elif type(other) == Molecule:
            return Molecule(self.atoms + other.atoms)

    def __str__(self):
        return '-'.join(self.atoms)


# Atom('R')
a1 = Atom('H')
a2 = Atom('H')
a3 = Atom('O')
a4 = Atom('P')


# a1.__add__(a2)

# print(a1)
# print(a2)
# m = a1 + a2
# print(type(m))
# print(m)
# another_m = m + a4
# print(another_m)
# print(a1)
# print(a1 + a2)
# print(a1 + a2 + (a3 + a4))

# 2. Let's write a Music Player Class!
#    a) Create a Song class. The class will have 4 attributes - name, artist, album and the year.
#    b) Now let's create a Playlist. Playlist class will contain Songs. We should have a method that will load songs
#    into our playlist. A file called albums.txt is provided with this exercise. The method should take care of loading
#    the songs from the file and store them inside of our Playlist class.
#    c) Now, we need our Player itself. Create a Player class. The player may contain at least one playlist. A few
#    of its methods include play(), that will start playing from the beginning, show_now_playing, that will show the
#    information of the song that is playing now, next_song, that will start playing the next_song, prev_song, that does
#    the opposite and finally a stop() method, that stops the song that is playing.
#    d) Finally, implement __str__ method for our classes, so we can see a nice representation of each object.
# Note: The aforementioned points are necessary but it's not a complete description of a music player. Be creative
# and add more functionality wherever you'll find it useful!

# Եկեք ստեղծենք նվագարկիչի կլաս։ Կառուցվածքը հետևյալն է լինելու։ Ունենալու ենք երեք կլաս՝ Player, Playlist, Song:
# Song-ը պարունակելու է երգի մասին ինֆորմացիա, Playlist-ը պարունակելու է երգերը Song տիպի օբյեկտների տեսքով, իսկ
# Player-ը ունենալու է Playlist:
#    a) Ստեղծել Song կլաս։ Կլասը պետք է ունենա 4 ատրիբուտ - name, artist, album, year
#    b) Ստեղծենք Playlist կլասը։ Այն պարունակելու է երգերը։ Այս կլասը պետք է ունենա load songs մեթոդ։ Տվյալ տնայինի հետ
#    ձեզ եմ ուղարկում նաև albums.txt ֆայլը։ Ֆայլը պարունակում է հարյուրավոր երգերի անունները, հեղինակներին, ալբոմների
#    անունները և ձայնագրման թվականը։ Ամեն տողում մի երգի ինֆորմացիա է։ Ամեն տողի դաշտերը իրարից անջատված են tab-երով։
#    Վերոնշյալ մեթոդով պետք է կարդալ ֆայլը և բոլոր երգերը Song-ի տեսքով փոխանցենք Playlist-ին։
#    c) Ստեղծել Player կլասը։ Այն պետք է ունենա Playlist տիպի ատրիբուտ։ Այս կլասը պետք է ունենա նաև հետևյալ մեթոդները՝
#    play(), stop(), next_song(), previous_song(), show_current_song()։ Մեթոդները կանչելուց պետք է կոնսոլում տեսնենք,
#    թե որ երգն է տվյալ պահին միացած։ Նաև վալիդացիաներ են պետք։ Օրինակ, եթե նվագարկիչն անջատված է, հաջորդ երգին անցնել
#    կամ կրկին անջատել չենք կարող։
#    d) Որպեսզի ամեն երգերը ավելի գեղեցիկ ներկայացվեն, սահմանել __str__ մեթոդը։ Ցանկալի է բոլոր կլասերի համար։

# Այս կետերը պարտադիր են, սակայն չեն պարունակում նվագարկիչի ողջ բնութագրությունը։ Կարող եք ազատ ավելացնել հավելյալ
# տրամաբանություն։

class Song:
    def __init__(self, name, artist, album, year):
        self.year = year
        self.album = album
        self.name = name
        self.artist = artist

    def __str__(self):
        return f'Name: {self.name}\nArtist: {self.artist}\nAlbum: {self.album}\nYear:{self.year}'


class Playlist:
    def __init__(self):
        self.songlist = []

    def load_songs(self, filepath):
        with open(filepath) as file:
            for line in file.readlines():
                artist, album, year, name = line.split('\t')
                name = name.strip()
                self.songlist.append(Song(name, artist, album, year))

    def __len__(self):
        return len(self.songlist)


class Player:
    def __init__(self, playlist, current_index=0):
        if type(playlist) != Playlist:
            raise ValueError

        if current_index < 0 or current_index > len(playlist) - 1:
            raise IndexError

        self.playlist = playlist
        self.is_playing = False
        self.current_index = current_index

    def play(self):
        if self.is_playing:
            print('Player is already playing')
        else:
            self.is_playing = True
            print('Start playing...')

        self.current_song()

    def stop(self):
        self.is_playing = False
        print('Stop playing...')

    def next(self):

        if self.current_index == len(self.playlist) - 1:
            print('End of playlist')
        else:
            self.current_index += 1
            self.current_song()

    def prev(self):

        if self.current_index == 0:
            print('Start of playlist')
        else:
            self.current_index -= 1
            self.current_song()

    def current_song(self):
        print('=' * 50)
        print(self.playlist.songlist[self.current_index])
        print('=' * 50)


playlist = Playlist()
playlist.load_songs('albums.txt')

player = Player(playlist)
player.play()
player.next()
player.prev()
player.prev()


# import os
# print(os.getcwd())
# with open('./albums.txt') as file:
#     for line in file.readlines():
#         print(line)

# 3. Create a class named Length. The default unit for length is meter. The class must contain some conversions
# information, e.g. feet -> m, km -> m, yard -> m, mile -> m etc.
#    a) Create a dictionary that will hold the metrics. Keys will be the unit name and their values will be the
#    coefficients for converting that unit to meters.
#    b) The class will have 2 instance attributes. Units and the length value itself.
#    c) Now, we can add lengths of course. So implement that method. But be careful, we can't add yard to meters, so
#    you will need to convert everything before adding.
#    d) Implement the __str__ method. This method must show the length of our Length object in meters.
#    e) Implement the __repr__ method. This method must show the length in whichever units our class is.
# Feel free to add some more features if you find them useful.

# Ստեղծել Length կլաս։ Երկարության հիմնական միավորը կհամարենք մետրը։ Կլասը պետք է ունենա որոշակի ինֆորմացիա, թե ինչպես
# փոխակերպել այլ միավորը մետրի (feet, km, yard, mile etc.)
#    a) Ստեղծել բառարան, որը կպահի վերոնշյալ ինֆորմացիան։ Բանալիները կլինեն միավորների անունները, իսկ արժեքները կլինեն
#    այն գործակիցները, որոնց օգնությամբ այդ միավորից ստանում ենք մետր։
#    b) Կլասը պետք է ունենա երկու instance attributes։ Երկարության արժեքը և միավորը։
#    c) Մենք պետք է կարողանանք երկարությունները իրար գումարել։ Սահմանել համապատասխան մեթոդը։ Ուշադրություն դարձնել
#    միավորներին։ Մենք չենք կարող ուղղակիորեն մետրը գումարել մղոնի կամ հակառակը։
#    d) Սահմանել __str__ մեթոդը։ Այս մեթոդը մեզ ցույց կտա օբյեկտի երկարությունը մետրերով։
#    e) Սահմանել __repr__ մեթոդը։ Այս մեթոդը մեզ ցույց կտա օբյեկտի երկարությունը այն միավորով, որով սահմանվել է։
# Լրացուցիչ, կարող եք ավելացնել հավելյալ տրամաբանություն որտեղ ճիշտ կգտնեք։


class Length:
    __conversion = {'m': 1, 'km': 1000, 'yard': 1.094, 'mile': 1609.34}

    def __init__(self, length, unit='m'):
        if unit not in Length.__conversion.keys():
            raise TypeError

        self.length = length
        self.unit = unit

    def __add__(self, other):
        if type(other) != Length:
            raise TypeError

        if self.unit == other.unit:
            return Length(self.length + other.length, self.unit)
        else:
            return Length(Length.get_meter(self) + Length.get_meter(other))

    @staticmethod
    def get_meter(x):
        return Length.__conversion[x.unit] * x.length

    def __repr__(self):
        return f'{self.length} {self.unit}'

    def __str__(self):
        return f'{Length.get_meter(self)} m'

    def convert(self, unit):
        if unit not in Length.__conversion.keys():
            raise TypeError
        meter = Length.get_meter(self)
        with_unit_length = meter / Length.__conversion[unit]

        self.unit = unit
        self.length = with_unit_length
        return self


# l = Length(10, 'km')
# print(l)
# print(repr(l))

# m = Length(1, 'mile')
# m.convert('km')
# print(repr(m))

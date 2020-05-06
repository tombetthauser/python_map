class Artist:
  # class attribute
  all_artists = []

  def __init__(self, name, mfa, bfa, birthyear, birthplace):
    self.birthplace = birthplace
    self.birthyear = birthyear
    self.name = name
    self.bfa = bfa
    self.mfa = mfa
    if self not in Artist.all_artists:
      Artist.all_artists.append(self)

  # class method - duh
  @classmethod
  def count(cls):
    return len(cls.all_artists)

  def info(self):
    birthplace = self.birthplace
    birthyear = self.birthyear
    name = self.name
    bfa = self.bfa
    mfa = self.mfa
    return f'{name}, born in {birthplace}, {birthyear}. BFA from {bfa}. MFA from {mfa}.'


class ArtWork:
  def __init__(self, title, artist, year, measurement='inches'):
    self.measurement = measurement
    self.artist = artist
    self.title = title
    self.year = year

  def info(self):
    return f'"{self.title}" by {self.artist}, {self.year}'

class Painting(ArtWork):
  # class attribute - constant
  TYPE = 'Painting'

  def __init__(self, title, artist, height, width, medium, year, measurement='inches'):
    super().__init__(title, artist, year, measurement='inches')
    self.medium = medium
    self.height = height
    self.width = width

  def info(self):
    measurement = self.measurement
    medium = self.medium
    height = self.height
    width = self.width
    title = self.title
    year = self.year

    if (type(self.artist) == type('string')):
      artist = self.artist
    else: 
      artist = self.artist.name 
    
    return f'"{title}" by {artist}, {height} x {width} {measurement}, {medium}, {year}'


class Arts:

  @staticmethod
  def incm(inches):
    return inches * 2.54

  @staticmethod
  def cmin(cm):
    return cm / 2.54

  @staticmethod
  def convert_dimensions(artwork):
    if artwork.measurement == 'inches':
      artwork.height = Arts.incm(artwork.height)
      artwork.width = Arts.incm(artwork.width)
      artwork.measurement = 'cm'
    elif artwork.measurement == 'cm':
      artwork.height = Arts.cmin(artwork.height)
      artwork.width = Arts.cmin(artwork.width)
      artwork.measurement = 'inches'

artist1 = Artist(
    name="Tom Betthauser",
    mfa="Yale University, 2012",
    bfa="the San Francisco Art Institute, 2020",
    birthyear=1987,
    birthplace="San Francisco"
)

painting1 = Painting(
  artist=artist1, 
  title='An Empty Field', 
  width=25, 
  height=15, 
  medium='oil on panel', 
  year=2020
)

painting2 = Painting(
  artist="Joan Brown", 
  title='A Not Empty Field', 
  width=35, 
  height=25, 
  medium='acrylic on canvas', 
  year=1967
)

# print(painting1.info())
# print(artist1.info())
# print(painting2.info())
# for ele in Artist.all_artists:
#   print(ele.name)
# print(painting1.TYPE)
# print(Artist.count())
# print(Arts.cmin(38.1))
# print(painting1.measurement)

print(painting1.info())
Arts.convert_dimensions(painting1)
print(painting1.info())
Arts.convert_dimensions(painting1)
print(painting1.info())
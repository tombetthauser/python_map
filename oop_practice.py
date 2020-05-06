class Artist:
  def __init__(self, name, mfa, bfa, birthyear, birthplace):
    self.birthplace = birthplace
    self.birthyear = birthyear
    self.name = name
    self.bfa = bfa
    self.mfa = mfa

  def info(self):
    birthplace = self.birthplace
    birthyear = self.birthyear
    name = self.name
    bfa = self.bfa
    mfa = self.mfa
    return f'{name}, born in {birthplace}, {birthyear}. BFA from {bfa}. MFA from {mfa}.'


class ArtWork:
  def __init__(self, title, artist, year):
    self.title = title
    self.artist = artist
    self.year = year

  def info(self):
    return f'"{self.title}" by {self.artist}, {self.year}'

class Painting(ArtWork):
  def __init__(self, title, artist, height, width, medium, year):
    super().__init__(title, artist, year)
    self.medium = medium
    self.height = height
    self.width = width

  def info(self):
    medium = self.medium
    height = self.height
    width = self.width
    title = self.title
    year = self.year

    if (type(self.artist) == type(Artist(0, 0, 0, 0, 0))):
      artist = self.artist.name 
    else: 
      artist = self.artist
    
    return f'"{title}" by {artist}, {height} x {width}, {medium}, {year}'


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
  width='25 inches', 
  height='15 inches', 
  medium='oil on panel', 
  year=2020
)

painting2 = Painting(
  artist="Joan Brown", 
  title='A Not Empty Field', 
  width='35 inches', 
  height='25 inches', 
  medium='acrylic on canvas', 
  year=1967
)

print(painting1.info())
print(artist1.info())
print(painting2.info())
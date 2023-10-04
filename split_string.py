# this functions makes sure that artist and title are centerd in the middle depending on which of them is the longest
def split_artist_title(string):
    title = (str(string.split('--')[0]))
    artist = (str(string.split('--')[1]))
    return artist, title
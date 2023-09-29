# this functions makes sure that artist and title are centerd in the middle depending on which of them is the longest

def format_output(string):
    s = string
    s_title = (str(s.split("--")[0]))
    s_artist = (str(s.split("--")[1]))
    length_title = len(s_title)
    length_artist = len(s_artist)

    if length_title >= length_artist:
        artist = s_artist.center((length_title-1), ' ')
        title = s_title

    elif length_title <= length_artist:
        artist = s_artist
        title = s_title.center((length_artist-1), ' ')

    return artist, title




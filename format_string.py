# this functions makes sure that artist and title are centerd in the middle depending on which of them is the longest
def format_output(string):
    s = string
    s_title = (str(s.split('--')[0]))
    s_artist = (str(s.split('--')[1]))

    if len(s_title) >= len(s_artist):
        artist = s_artist.center((len(s_title)-1), ' ')
        title = s_title

    else:
        artist = s_artist
        title = s_title.center((len(s_artist)-1), ' ')

    return artist, title
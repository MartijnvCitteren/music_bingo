import pandas as pd


def xlsx_to_list(xlsx_path):
    df = pd.read_excel(xlsx_path, sheet_name="Sheet1")
    list_title = list(df["Titel"])
    list_artist = list(df["Artiest"])

    # create a list where al artists and songs are collected. We cant index a DataFrama so generating a radom list / var
    # from that is hard.
    list_complete = []
    index = 0
    for song in list_title:
        list_complete.append(song + '--' + list_artist[index])
        index += 1
    return list_complete

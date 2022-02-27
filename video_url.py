import youtube_dl

def get(link):
    url = link.replace(".mangi ", "") 
    ydl_opts = {'format':"bestaudio"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']

    return info, url2
import yt_dlp as youtube_dl
import json, sys
from youtube_search import YoutubeSearch

def get(input_text):
    converted_input = input_text.replace(".mangi ", "")
    if "youtube.com" in converted_input:
        url = converted_input
    else:
        search_result = YoutubeSearch(converted_input, max_results=1).to_json()
        j = json.loads(search_result)
        url = "https://youtube.com" + j["videos"][0]["url_suffix"]

    ydl_opts = {'format':"bestaudio"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][7]['url']

    return info, url2

if __name__ == '__main__':
    print("Käivita main.py fail")
    sys.exit()

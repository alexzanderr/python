

from core.json_module import *
from core.pathx import *
from core.aesthetix import *
import requests
from core.download import *
import subprocess
from core.image import img_toPng
import re

database_path = "database/database.json"
database_json = read_json_from_file(database_path)

def GetFavicon(url: str):
    """ 
        <link rel="shortcut icon__pathttps://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196">
        
        we are aiming for rel="shortcut icon"
    """
    try:
        r = requests.get(url)
        if r.status_code == 200:
            lines = r.text.split("\n")
            
            for l in lines:
                # print(l)
                if "shortcut icon" in l:
                    start = l.find("href=\"") + len("href=\"")
                    stop = l.find("\"", start + 1)
                    # print(start, stop)
                    shortcut_url = l[start: stop]
                    print(url, shortcut_url, sep="  __|__  ")
                break
            
            # result = DownloadFileFromURL(url, r"D:\Alexzander__\programming\python\MyInternet\database\test")
            # print(result)
            # if is_file(result):
            #     ImageToPNG(result)
            #     # sleep(1)
            #     # subprocess.Popen(["explorer", result])
            
    except Exception as error:
        print(error)
    
mega = []
for wb in database_json.values():
    mega.extend([link for link in wb])
    
w = len(mega)
# print(w)
# print(mega)

# with ThreadPoolExecutor(max_workers=w) as executor:
#     for m in mega:
#         executor.submit(GetFavicon, m)

for m in mega:
    print(m)

# for m in mega:
#     GetFavicon(m)


if __name__ == '__main__':
    
    with open("database/websites.json", "w+", encoding="utf-8") as f:
        f.truncate(0)
        f.write(json_dumps(mega))
    
    
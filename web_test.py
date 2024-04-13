import webbrowser
from youtubesearchpython import VideosSearch
from googlesearch import search


# webbrowser.open("www.google.com/search?q=test")

# count=1
# for i in search("test",start=0,stop=1,num=10):
#     print(f"{count}   {i}")
#     count+=1



# r=(VideosSearch("node js",limit=1,).result())
# print(type(r['result'][0]))


def searchYoutube(searchKeyword,limit=10 ):
    r=(VideosSearch(searchKeyword,limit=limit,).result())
    
    data=[]
    for i in r['result']:
        data.append([i['title'],i['link']])
    return data

# print(searchYoutube("nodejs",limit=1))
 
def searchGoogle(keyword,limit=10):
    data=[]
    for i in search(keyword,start=0,stop=limit,num=limit):
        data.append(i)
    return data

import requests
from bs4 import BeautifulSoup

url = "https://ethglobal.com/showcase/page/7?events=hackfs2023"

def constructURL(events,pageNo):
    url = f"https://ethglobal.com/showcase/page/{pageNo}?events={events}"
    return url


def main():
    events = input("[+]Enter event tag:")

    for i in range(1,8):
        response = requests.get(constructURL(events,i))
        html = response.content
        soup = BeautifulSoup(html,features = "html.parser")
        urlList = soup.findAll('a',{"class":"block border-2 border-black rounded overflow-hidden relative"})
        for url in urlList:
            newURL = "https://ethglobal.com"+url.get("href")
            newResponse = requests.get(newURL)
            newSoup = BeautifulSoup(newResponse.content,features='html.parser')
            newList = newSoup.findAll("h3",{"class":"text-black-500 uppercase text-xs font-normal mt-6 mb-2"})
            for item in newList:
                if "Winner of" in item.contents:
                    award = newSoup.find("div",{"class":"flex-1 mx-4"}).h4

                    print("[+] https://ethglobal.com"+url.get("href")+" WON "+ award.contents[0])

main()
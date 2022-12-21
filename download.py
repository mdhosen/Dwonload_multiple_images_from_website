import bs4
import requests

url = "put here"
r = requests.get(url)
data = bs4.BeautifulSoup(r.text, "html.parser")
Nfnd = 0
fnd = 0
for l in data.find_all("a"):
    
    r = requests.get(url + l["href"])
    if r.status_code==200:
        try:
            with open(str(l["href"]),'wb') as f:
                f.write(r.content)
                fnd = fnd+1
        except:
            print("not found:")
            Nfnd=Nfnd+1
    

print("found",fnd)
print("Not found",Nfnd)
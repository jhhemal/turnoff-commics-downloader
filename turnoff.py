from bs4 import BeautifulSoup
import requests, csv, os

os.makedirs('turnoff', exist_ok=True)
cf = open('turnoff/comics.csv', 'w')
cw = csv.writer(cf)
cw.writerow(["Name"])
url = 'http://turnoff.us'
comics_url = url

# print(soup.prettify())
while True:
    source = requests.get(comics_url).text
    soup = BeautifulSoup(source, 'lxml')
    article = soup.find('article', class_="post-content")
    imagelink = url+article.img['src']

    name = imagelink.split('/')[5]

    comics_name = name[:-4]
    
    print(f'Downloading comics: {comics_name}')

    cw.writerow([comics_name])
    with open(f'turnoff/{name}', 'wb') as f:
        img = requests.get(imagelink).content
        f.write(img)
    link = soup.find('div',class_="prev").a
    if link.text == 'previous':
        comics_url = url+link['href']
    else:
        break

    print('--Done--')

print('All comics have been downloaded and saved the name in csv')
cf.close()
from bs4 import BeautifulSoup

with open('https://www.instagram.com/philipesko8/followers/', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    #print(soup.find('ul', attrs={ 'id' : 'mylist'}))
    print(soup.find('div', class_='PZuss'))
import requests
import re

from bs4 import BeautifulSoup
def nts():
    url = "https://www.timeserver.ru/cities/kg/bishkek"
    res = (requests.get(url)).text
    soup = BeautifulSoup(res, 'html.parser')
    soup = soup.find('div', {'class': 'content-box city-info'})
    l1 = []
    l2 = []
    l = soup.get_text(" ")
    res1 = re.sub( "\t", "", l).split('\n')
    for i in range(len(res1)): 
        if i % 2 == 0:
            l1.append(res1[i])
        else:
           l2.append(res1[i])
    print(l2[0], l1[1])
    print(l2[1], l1[2][:6])
    print(l2[2], l1[3])
    print(l2[3], l1[4])
    print(l2[4], l1[5])
    print(l2[5], l1[6], "/ Бишкек,", "Координаты:",l2[7])
    print(l2[8], l1[9], "резидентов")
    print(l2[9], l1[10][:8])
    soup = BeautifulSoup(res, 'html.parser')
    soup = soup.find('div', {'class': 'timeview-data'})
    return ("Время в Бишкеке: " + soup.get_text() + " / чч:мм:сс")
 

print(nts())




 
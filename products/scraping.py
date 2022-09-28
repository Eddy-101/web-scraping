import requests
from bs4 import BeautifulSoup

def getScrapping(url, site="ebay"):
    result = requests.get(url)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    if site == "ebay":
        products = soup.find_all('li', class_="s-item")
        items = []
        for product in products:
            title = product.find('div', class_="s-item__title").text.strip()
            price = product.find('span', class_="s-item__price").text.strip()
            image = product.find('img', class_="s-item__image-img")
            item = {
                'title': title,
                'price': price,
                'image': image['src']
            }
            items.append(item)
        return items 

    if site == "mercado_libre":
        products = soup.find_all('li', class_="shops__layout-item")
        items = []
        for product in products:
            title = product.find('h2', class_="shops__item-title").text.strip()
            price = product.find('span', class_="price-tag-amount").text.strip()
            image = product.find('img', class_="shops__image-element")

            item = {
                'title': title,
                'price': price,
                'image': image['data-src']
            }

            items.append(item)
        return items
    
    return []



import pandas as pd

from bs4 import BeautifulSoup
import requests


def get_links(soup):
    categorias_url = []
    for categoria in soup.findAll('div', class_="card h-100"):
        categorias_url.append(categoria.find('a').get("href"))

    return categorias_url

def get_cats(url):
    cat_url = []
    cat_names = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    cats = soup.find_all('div', class_ = "card h-100")
    for cat in cats:
        anchor = cat.find('a')
        if "Histórico" not in anchor.text:
            cat_url.append(anchor.get("href"))
            cat_names.append(cat.find('p',class_='fw-bolder').text)
    # print(cat_url, cat_names)
    return cat_url, cat_names #! considerar dict en vez de tupla

def get_hist(url):
    hist_list = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    hists = soup.findAll('div', class_ = "card h-100")
    for hist in hists:
        anchor = hist.find('a')
        if "Histórico" in anchor.text:
            hist_list.append(anchor.get("href"))
    return hist_list

def get_tab(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    tab = soup.find('table', class_="table table-striped table-responsive text-center")
    lista_elementos = [td.findAll('td') for td in tab.findAll('tr')][1:]
    df_tab = pd.DataFrame(lista_elementos).map(lambda x: x.text)
    headers = [h.text for h in tab.findAll('th')]
    df_tab.rename(columns= dict(enumerate(headers)), inplace=True)
    df_tab["Nombre"] = soup.find('meta', {"name": 'Keywords'}).get('content').replace('precio ', '')
    return df_tab
import requests
import json
import pandas as pd
from scrapy.http import TextResponse
lista = list()
listasecun = list()
listater = list()
prin = list()
objects = dict()
#Pega dados da parte de gamer da Kalunga
def gamer():
    
    headers = {
        'authority': 'www.kalunga.com.br',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.kalunga.com.br/',
        'accept-language': 'pt-BR,pt;q=0.9',
    }

    params = (
        ('menuID', '109'),
    )

    response = requests.get('https://www.kalunga.com.br/depto/gamers/13', headers=headers, params=params)
    resp = response.text
    dados = TextResponse(url = '',body = resp,encoding = 'utf8')
    produtos = dados.xpath('//div[@id="divProdutoDepartamento"]//a//h2//text()').getall()
    return produtos


def gamertwo():
    
    cookies = {
        'CookieID': '5e19ab74-6e6b-11ec-8db0-42012e3b5681',
        'session': 'eyJjc3JmX3Rva2VuIjoiNjhkNjkzZDE1MzNkNGQ0NGM5ZGZkNDc1ZjlmMWQ3ODRkNzk2NjMyYSJ9.YdYIXA.2JjkC4RXKwBvpjVun16v6oEVD60',
        'BIGipServerpool_kube_workers': '3624671148.20480.0000',
        'ak_bmsc': '8DD420A0DFEE1C3C550816349CB7511B~000000000000000000000000000000~YAAQVRc2F1vymaF9AQAA9akQLA77wKa4vRCfzeUA9wl7a9FtAEWOVL+aY2P1w/48CQHGZGQlQmevby/7hb0pK7jaQ2pE7L1EWKQDLc7Rh5mbrTU/lcWqg3Fff+sCyksozHZp6OBy39J+E/tLrc0TVbA6RYinfKermbnMSfaVf7MWmWe9hbe7TZjDVpbLoOSDcDYjE3v1GBQlnQKOtlYSt9PGNUjUJQezjDg9uKicCobezjEeTfhDNbTO4i1RLw8hUjT+bPpVbyKw/8qaW+lJl7j1PdXEftJ6HeAuBNZfpsg2tgk9hO3/xHSptPHpvUi2iGCneGF/wH5kImAI3l1YNbq6JyFb30eHDz63/So/Pn++Z5PTsXjoyhvZigNfcTGI9OjWJGwHSkAjoFR7jio=',
        '_gcl_au': '1.1.1011150376.1641416798',
        '_ga': 'GA1.3.661488880.1641416798',
        '_gid': 'GA1.3.1558143743.1641416798',
        '_uetsid': '5f7539206e6b11eca8ba3772b4e93ee7',
        '_uetvid': '5f762d606e6b11ecbd8e6d7727f99612',
        '_fbp': 'fb.2.1641416798746.1972996704',
        'bm_sv': 'A2A9AA49A975DA3180F8414244E9BA26~Xly0bAEGC0ZB0BWLIFjGX6Xm4t5bkiv4WDzm+Atx+hTtBIhE3qIMnjdDZUAdE3JySyxu2fW/r2gBjhog3on6t58xzI3lvyilRSi9lvzdGTYTn4Wh62IU90Slq3wDjXv7Z8vR7DiEUG6omBqtt+5edHnJoTggWh1L6NINFP7VZ8o=',
    }

    headers = {
        'authority': 'www.kalunga.com.br',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'authorization': 'Basic ZGFuaWxva2FAa2FsdW5nYS5jb20uYnI6S0BsdW5nYTEyMwo=',
        'content-type': 'application/json;charset=utf-8',
        'accept': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'x-csrftoken': 'IjY4ZDY5M2QxNTMzZDRkNDRjOWRmZDQ3NWY5ZjFkNzg0ZDc5NjYzMmEi.YdYRSQ.zfTZBtXavuWrZfHq1m812c_l6QI',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.kalunga.com.br',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.kalunga.com.br/depto/gamers/13',
        'accept-language': 'pt-BR,pt;q=0.9',
        
    }

    data = '{"codigo_menu":null,"codigo_classificacao":"13","codigo_grupo":0,"codigo_subgrupo":0}'

    response = requests.post('https://www.kalunga.com.br/api/obterProdutosDepartamento/10', headers=headers, cookies=cookies, data=data)
    resp = response.text
    dados = TextResponse(url = '',body = resp,encoding = 'utf8')
    produ = dados.xpath('//div//a//h2//text()').getall()
    return produ


def gamerthree():

    cookies = {
        'CookieID': '3ebaa104-6f22-11ec-b382-1219a6df71ad',
        'session': 'eyJjc3JmX3Rva2VuIjoiOTE4NGJlYWQyMDFiMDM2MzdjNjc3NzMzMGVkZGNhNmMyZDU5MzkxMyJ9.Ydc7LQ.xNuGq67jYZA8MWT5vg8EAmtRkL8',
        'BIGipServerpool_kube_workers': '4144764844.20480.0000',
        'ak_bmsc': '98E0B7B936859FA2FAA5C3C8E0AA93BF~000000000000000000000000000000~YAAQZBc2F6q0dp19AQAAoSm/MA5cWczfs34YLjK/sWkhRRpzXFVVygL72aQE5L5fvyYCIoE0AxYwnW8lEc9BOJTUN7TRD+zDiFHhlXlUtu4qxwxwgbzLxze6ZbRvFDD27oa34RbmcTMnD79mJlD4m27324rGjp9BcZDLTOI2cJLzYlyn1PbeQTPemxhFoC8EXcOQGFVUHtx4503vbq5GnsjOvxuWmhZIhe97fhmmy6v+0JWoNpGKhwXAdP7hEllBIOmJyw5MiEjtoqRox8WlptBheIc4wNjI8qZ7VZjf1fUCzHz1XhJLGCzmxbPdWaDkLZDRmQuTCUwnBufba4SJ+4gmXOPzZDPWtwxKKgNtHEsnhEwWJrh3NV5O06O4iJYAUH5f8bZfFoMahDOqjtg=',
        '_gcl_au': '1.1.853915828.1641495344',
        '_ga': 'GA1.3.1700888572.1641495347',
        '_gid': 'GA1.3.1902789627.1641495347',
        '_fbp': 'fb.2.1641495347227.1480721521',
        '_dc_gtm_UA-18044383-1': '1',
        '_dc_gtm_UA-18044383-8': '1',
        '_uetsid': '41f61d006f2211ecabdd25711aa19848',
        '_uetvid': '41f792606f2211ecbf71355de42f4fde',
        'bm_sv': 'A276DD367F5A8150D75C2E84CD162646~Tv+aO5bpXxlJHX0QIl8IESah8Hn6tShdbHD1QwZHAoyEsFX7zZ+FXgtaW2mIubyoKid/8S//Os3QEYJ0EmeQFAFzPU/Qug627z9kP3zFjw5ddVuPFMIhsbDWl8o3vbKXyeYy5jVixql9N2gGmxIiJSYF35cQp6NmcoKzB0LYT1o=',
    }

    headers = {
        'authority': 'www.kalunga.com.br',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'authorization': 'Basic ZGFuaWxva2FAa2FsdW5nYS5jb20uYnI6S0BsdW5nYTEyMwo=',
        'content-type': 'application/json;charset=utf-8',
        'accept': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'x-csrftoken': 'IjkxODRiZWFkMjAxYjAzNjM3YzY3NzczMzBlZGRjYTZjMmQ1OTM5MTMi.YddEeg.l0OR6FwuMLQpsQktclMxDnD1nuM',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.kalunga.com.br',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.kalunga.com.br/depto/gamers/13',
        'accept-language': 'pt-BR,pt;q=0.9',
    }

    data = '{"codigo_menu":null,"codigo_classificacao":"13","codigo_grupo":0,"codigo_subgrupo":0}'

    response = requests.post('https://www.kalunga.com.br/api/obterProdutosDepartamento/20', headers=headers, cookies=cookies, data=data)
    resp = response.text
    dados = TextResponse(url = '',body = resp,encoding = 'utf8')
    p = dados.xpath('//div//a//h2//text()').getall()
    return p


def tabela(p1,p2,p3):
    tabela = pd.DataFrame(p1)
    tabela2 = pd.DataFrame(p2)
    tabela3 = pd.DataFrame(p3)
    prin = pd.concat([tabela, tabela2, tabela3], ignore_index=True)
    return prin
    

if __name__ == '__main__':
    SubCategorias = gamer()
    SubCategoriasTwo = gamertwo()
    SubCategoriasThree = gamerthree()
    print(tabela(SubCategorias,SubCategoriasTwo,SubCategoriasThree))
1
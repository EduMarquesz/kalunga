
import pandas as pd
import requests
from scrapy.http import TextResponse
l = list()
lista = list()
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


def gamertwo(departamento):
    
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
    url = f'https://www.kalunga.com.br/api/obterProdutosDepartamento/{departamento}'
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    dados = TextResponse(url = '',body = response.text,encoding = 'utf8')
    produ = dados.xpath('//div//a//h2//text()').getall()
    return produ


if __name__ == '__main__':
    SubCategorias = gamertwo(13)
    SubCategoriasTwo = gamertwo(10)
    SubCategoriasThree = gamertwo(20)
    todos_produtos = SubCategorias + SubCategoriasTwo + SubCategoriasThree
    informations = pd.DataFrame(todos_produtos)
    
print(informations)
print('Tudo OK!!')
1

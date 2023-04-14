import requests
from bs4 import BeautifulSoup

# headers = {
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }
#
# params = {
#     'utm_campaign': 'vendor_org_17231_{ботТГ}',
#     'hs': '1',
#     'sh': '97KwkxPQSg',
# }

url = "https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2" \
      "?url=/product/razvivayushchaya-igra-konstruktor-pazl-mozaika-s-shurupovertom-klyuchom-i-otvertkoy-200-detaley-224283829/" \
      "?hs=1" \
      "&layout_container=pdpPage2column" \
      "&layout_page_index=2" \
      "&sh=97KwkxPQSg" \
      "&utm_campaign=vendor_org_17231_%7B%D0%B1%D0%BE%D1%82%D0%A2%D0%93%7D"

response = requests.get(url=url)
print(response.json())

import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

response = requests.get(YOUTUBE_TRENDING_URL)

print('Status Code', response.status_code)
#Status Code = 200 apenas indica sucesso
with open('trending.html', 'w') as f:
  f.write(response.text)
  #'w' indica que é pra escrever o arquivo

  doc = BeautifulSoup(response.text, 'html.parser')

  print('Page title', doc.title)

#para achar todos os divs do video
video_divs = doc.find_all('div', class_ = 'ytd-video-render')
print(f'Found {len(video_divs)} videos')
#com f' dentro da função print, posso passar linha de código dentro do string
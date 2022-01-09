import json
import bs4
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Api is working'

@app.route('/<string:sourcelang>/<string:tolang>/<string:text>')
def translate(sourcelang ,tolang ,text):
    def replace_space(string):
        return string.replace (" ", "+")
    url="https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl="+sourcelang+"&tl="+tolang+"&dt=t&q="+replace_space(text)
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',}
    request=requests.get(url,headers=headers)
    soup=bs4.BeautifulSoup(request.text,"html.parser")
    json_data= json.loads(soup.text)
    return(json_data['sentences'][0]['trans'])

if __name__ == '__main__':
  app.run()

import requests
import urllib.parse
import os
from bs4 import BeautifulSoup

BASE_URL = 'https://zh.wikipedia.org/wiki/'
TEMP_DIR = './temp'
CSS_COUNT = 4


def write_file(filename, html):
    # 将html内容写入文件
    print('writing to file...')
    os.makedirs(TEMP_DIR, exist_ok=True)
    with open(TEMP_DIR + '/' + filename, 'w', encoding='utf-8') as f:
        f.write(html)


def edit_file(html):
    # 给html文本添加css样式 a
    soup = BeautifulSoup(html, 'html.parser')
    for css_id in range(1, CSS_COUNT+1):
        f = './css/' + str(css_id) + '.css'
        print('adding css:' + f + ' ...')
        new_style_tag = soup.new_tag('style')
        with open(f, 'r', encoding='utf-8') as f:
            css_content = f.read()
            new_style_tag.string = css_content
            # print(soup.title)
            soup.head.insert(0, new_style_tag)
    return soup.prettify()


def main():
    search_key = input("请输入要搜索的词条：")
    new_url = urllib.parse.urljoin(BASE_URL, search_key)
    try:
        response = requests.get(new_url, timeout=(10, 20))
    except requests.exceptions.Timeout:
        print("Error: 很抱歉，请求超时")
        return
    if response.status_code == 404:
        print("Error: 未找到该词条！")
        return
    html = response.text
    html = edit_file(html)
    write_file('temp_html.html', html)


if __name__ == '__main__':
    main()

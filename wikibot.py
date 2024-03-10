import requests
import urllib.parse
import os

BASE_URL = 'https://zh.wikipedia.org/wiki/'


def write_file(filename, html):
    # TODO: 添加css渲染
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


def main():
    search_key = input("请输入要搜索的词条：")
    new_url = urllib.parse.urljoin(BASE_URL, search_key)
    response = requests.get(new_url)
    # TODO: 错误处理（超时）
    if response.status_code == 404:
        print("未找到该词条")
    write_file('temp_html.html', response.text)
    # TODO: 图片加载


if __name__ == '__main__':
    main()

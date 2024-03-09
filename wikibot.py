import requests
import urllib.parse

BASE_URL = 'https://zh.wikipedia.org/wiki/'


def write_file(filename, html):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


def main():
    search_key = input("请输入要搜索的词条")
    new_url = urllib.parse.urljoin(BASE_URL, search_key)
    print(new_url)
    response = requests.get(new_url).text
    print(response)
    write_file('temp_html.html', response)


if __name__ == '__main__':
    main()

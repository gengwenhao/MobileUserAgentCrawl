"""
    爬取手机UserAgent
"""
from lxml import html
import requests

from settings import OS_LIST, URL, START_PAGE, END_PAGE

ua_list = []


def run():
    for os in OS_LIST:
        page = START_PAGE

        while 1:
            # 构造url
            url = URL.format(os=os, page=page)
            # get请求
            res = requests.get(url)
            print(f'Fetch: {url}')
            root = html.fromstring(res.content)
            rs = root.xpath('//td[@class="useragent"]/a/text()')
            ua_list.extend(rs)

            if 50 > len(rs):
                break

            page += 1

            if page > END_PAGE:
                break


def save():
    with open('result.txt', 'w') as f:
        f.writelines([f'{ua}\n' for ua in ua_list])


if __name__ == '__main__':
    run()
    save()

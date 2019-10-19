#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Filename: config
# Project : PyCharm
# Author  : sml2h3
# Email   : sml2h3@gmail.com

import requests
from config import API_URL

# 修改代理提取链接

resp = requests.get('http://api')

proxies = resp.text.replace('\r', '').replace('\n', '')

print('代理为:', proxies)

proxies = {'http': 'http://{}'.format(proxies)}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

INDEX_URL = 'http://wenshu.court.gov.cn/'

resp = requests.get(INDEX_URL, headers=headers, proxies=proxies)

HM4hUBT0dDOn80S = resp.cookies['HM4hUBT0dDOn80S']

resp = requests.post(API_URL, data={'html': resp.text})

HM4hUBT0dDOn80T = resp.json()['msg']

cookies = {
    'HM4hUBT0dDOn80S': HM4hUBT0dDOn80S,
    'HM4hUBT0dDOn80T': HM4hUBT0dDOn80T
}

LIST_PAGE_URL = 'http://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=13527916f774f3e78bf8c0a69038d20a&s8=03'

resp = requests.get(LIST_PAGE_URL, headers=headers, cookies=cookies, proxies=proxies)

if '互联网或法院' in resp.text:
    print('访问列表页通过')

    LIST_URL = "http://wenshu.court.gov.cn/website/parse/rest.q4w"
    data = {
        'pageId': '13527916f774f3e78bf8c0a69038d20a',
        's8': '03',
        'sortFields': 's50:desc',
        'ciphertext': '1100111 1111000 1000100 1010100 1101010 1100001 1011000 111001 1100101 1011010 1010011 1110010 1001000 110110 1010001 1100011 1001101 110110 1101100 1100010 1000001 1100110 1100110 110110 110010 110000 110001 111001 110001 110000 110001 111001 1111010 1100011 1011010 1001000 1100110 1011000 1111010 1000110 111000 1110001 1100111 1110111 110001 1101011 110000 110110 1110011 1100001 1000011 1010100 1001101 1110111 111101 111101',
        'pageNum': '1',
        'queryCondition': '[{"key":"s8","value":"03"}]',
        'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc',
        '__RequestVerificationToken': 'WNBkSItKxGn7mmF5ctnNTZnX'
    }
    resp = requests.post(LIST_URL, data=data, headers=headers, cookies=cookies, proxies=proxies)

    if 'secretKey' in resp.text:
        print('列表获取成功')
        DETAIL_URL = "http://wenshu.court.gov.cn/website/parse/rest.q4w"
        data = {
            'docId': 'ec3b43e6ccc94dca93cbaae700c1199a',
            'ciphertext': '1010000 1101110 1010001 1110001 1110110 1000001 1100001 1001110 1000101 1010100 1101110 1111000 1001000 1011010 1110010 1001001 1110001 1001000 1110010 1100110 110111 1100001 1001010 1001111 110010 110000 110001 111001 110001 110000 110001 111001 1101000 1000001 1110101 1101000 1000111 1111001 1110111 1010001 1011010 1001001 110010 101011 1001010 1111001 1101110 1101011 1110000 111000 1010001 111000 1100011 1000001 111101 111101',
            'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@docInfoSearch',
            '__RequestVerificationToken': 'WNBkSItKxGn7mmF5ctnNTZnX'
        }
        resp = requests.post(DETAIL_URL, data=data, headers=headers, cookies=cookies,
                             proxies=proxies)
        if 'secretKey' in resp.text:
            print('详情获取成功')
        else:
            print('代理被封')
    else:
        print('代理被封', '列表获取失败')
        print(resp.status_code)
else:
    print('代理被封', '访问列表页失败')
    print(resp.status_code)

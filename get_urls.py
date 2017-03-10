#!/usr/bin/env python
# coding=utf-8

import json
import requests as rq
import time,random

file_list = ['01.json', '02.json']

def get_json(filename):
    with open(filename,'r') as f:
        data = json.load(f)
    return data


def get_urls():
    target = []
    url0 = 'https://hackerone.com'
    for var_a in file_list:
        data = get_json(var_a)
        # print len(data['results'])
        for i in range(0,len(data['results'])):
            url = data['results'][i]['url']
            target.append(url0 + url)
    return target


def out_file():
    with open('result.txt','a') as f:
        for i in get_urls():
            f.write(i+'\n')


def get_info(i):
    data = get_urls()
    url = data[i]
    # print url
    header = dict()
    header['x-requested-with'] = 'XMLHttpRequest'
    header['accept'] = 'application/json, text/javascript, */*; q=0.01'
    header['referer'] = url
    try:
        dd = rq.get(url=url,headers=header).content
    # for i in data.headers: print i+":"+headers[i]
        with open('json00.json','a') as m:
            m.write(dd+'\n')

        result = json.loads(dd)['profile']['website']
        print result
        with open('urls00.txt','a') as f:
            f.write(result+'\n')
    except Exception,e:
        pass


if __name__ == '__main__':
    print 'Task is running...'

    for i in range(0,len(get_urls())):
        get_info(i)
    #    time.sleep(random.randint(3,8))

    print "Done"

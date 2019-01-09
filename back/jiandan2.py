# -*- coding: utf-8 -*-
# @Time    : 18-12-28 下午2:48

import requests

if __name__ == "__main__":
    target = "https://unsplash.com/"
    req = requests.get(url=target)
    print(req.text)

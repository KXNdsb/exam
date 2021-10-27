import os

import requests
import yaml
import pytest


def _base_data(file_name):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml1=os.path.join(cur_path,file_name)
    print(yaml1)
    file=open(yaml1)
    data = yaml.safe_load(file)
    return data

@pytest.fixture()
def get_base_data():
    base_data=_base_data('search.yaml')
    for v in base_data:
        return v



@pytest.fixture(scope='module',autouse=True)
def query_param(request):
    return request.param

param=[{'q':'中国平安','size':50,'page':1},{'q':'伊戈尔','size':50,'page':1}]

@pytest.mark.parametrize('query_param',param,indirect=True)
def test_search(get_base_data,query_param):
    url=get_base_data['url']
    method=get_base_data['method']
    headers=get_base_data['headers']

    res=requests.request(method=method,url=url,headers=headers,params=query_param)
    print(res.text)
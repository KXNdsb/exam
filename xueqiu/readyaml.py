import os
import yaml
def _base_data(file_name):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml1=os.path.join(cur_path,file_name)
    print(yaml1)
    file=open(yaml1)
    data = yaml.safe_load(file)
    print(data)

_base_data("search.yaml")
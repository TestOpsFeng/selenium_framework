import yaml
import os

fileNamePath = os.path.split(os.path.realpath(__file__))[0]
dir = os.path.join(fileNamePath,'../conf')

def get(file_name,*keys,file_path=dir):
    yamlPath = os.path.join(file_path, file_name)
    file = open(yamlPath, 'r', encoding='utf-8')
    config = yaml.load(file)
    for key in keys:
        config = config[key]
    return config

if __name__ == '__main__':
    # driver = get("constant.yaml","drivers",0)
    # print(driver)
    a = (1,2)
    print(type(a))
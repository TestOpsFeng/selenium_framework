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
    # wait_time = yaml_utils.get("constant.yaml", "wait_elements_time")
    # driver = get("host","url_regerister")
    # driver2 = get_url("constant.yaml","host")
    driver2 = get("constant.yaml","test1","test2","test33")
    print(driver2)
    # a = (1,2)
    # print(type(a))
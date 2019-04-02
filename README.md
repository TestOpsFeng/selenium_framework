### 框架介绍
- 根据PageObject设计模式对Selenium进行封装
- 通过driver封装chrome、firefox、edge浏览器
- 使用yaml分离测试代码和数据
- 使用logging库实现日志功能
- 使用Allure Report作为测试报告
- 通过AutoIT上传图片
- 通过barnum生成随机测试数据

### 运行
1. 环境要求：python3,pip3,对应版本的chromedriver和chrome.exe在同一目录
2. 安装库：pip3 install -r requirements.txt
3. 运行：
```
cd testcase
pytest test_baidu.py
```
如果要看AutoIT运行效果，不了解AutoIT的最好先看看[博客](https://blog.csdn.net/weixin_38389124/article/details/88909881)
- 确保分辨率是（1616，876），不是的话需要修改autoit/upload_img.au3文件，修改为正确分辨率,再重新编译
- 在C:\Users\qvzn0\Pictures\test.jpeg路径有test.jpeg图片，不然需要修改为正确路径，再重新编译
```python
cd testcase
pytest test_register.py
```

### Page Object模式
#### 定义
- Page指浏览器的一个页面，Object指编程语言中的对象
- 一个Object对应一个Page
- Object的属性对应Page的元素
- Object的方法对应Page的操作、行为
```
# 元素定位
input_search = (By.XPATH,'//*[@id="kw"]')
btn_search = (By.XPATH,'//*[@id="su2"]')
# 对象
class BaiduPage(BasePage):
    # 操作、行为
    def search(self):
        self.send_keys(input_search,"nihao")
        self.click(btn_search)
```
封装元素定位的代码不好理解，可通过具名元组优化：
```
 from collections import namedtuple
 Locator = namedtuple('Locator','by loc')
 input_search = Locator(By.XPATH,'//*[@id="kw"]')
 btn_search = Locator(By.XPATH,'//*[@id="su2"]')
```
####调用
```
 #创建对象
 self.baidu_page = BaiduPage(cls.driver)
 #调用行为
 self.baidu_page.search()
 #验证结果
 self.assertEqual(result,expectResult)
 
```

### 读取yaml
对conf文件路径下的yaml文件：
```yaml
test1:
  test2: 
    test3: test3
    test33: test33
```
使用以下方法调用：
```
from utils import yaml_utils

# 第一个参数是文件名称，后面都是节点
test1 = yaml_utils.get("constant.yaml","test1")
test2 = yaml_utils.get("constant.yaml","test1","test2")
test33 = yaml_utils.get("constant.yaml","test1","test2","test33")

# 如果要指定文件路径，通过file_path。例如要指定D盘根目录下的constant.yaml文件
test1 = yaml_utils.get("constant.yaml","test1" ,file_path="D:\")
```

### 日志体系
一般用于base_page封装常用的公用方法，通过logger_config.yaml进行配置：
```python
from utils.logger import logger
logger.info("A info message")
logger.error("A error message")
```
### Allure Report
运行：
```
cd testcase
pytest test_baidu.py --alluredir=../report
# 查看报告
allure serve ../report
```
样式：
![report](./report.png "optional title")
### AutoIT使用
参考我的博客：https://blog.csdn.net/weixin_38389124/article/details/88909881

### barnum使用
```python
    username = barnum.create_name(False).lower()
    email = barnum.create_email()
```
其他用法参考：https://github.com/chris1610/barnum-proj

### 在Jenkins上运行
1. 安装环境：python3, pip3, 库,
在Linux使用root上运行：
```
yum install -y epel-release
yum install -y python34
yum install -y python34-setuptools
easy_install-3.4 pip
pip3 install -r requirements.txt
```
2. 在jenkins上安装allure插件
3. 在全局工具管理安装Allure Commandline
4. 新建并配置Project：
- Source Code Management： 填入github仓库地址以及对应的token
- Build： 新增执行Shell： 填入：
```
cd testcase
python3 -m pytest test_baidu.py --alluredir=../report/
exit 0
```
- Post-build Actions: Allure Report: Path中填入report
- 构建

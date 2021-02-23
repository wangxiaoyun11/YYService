import os
import configparser
from common.handle_log import run_log as logger
'''
os.path.realpath(__file__)  获取当前文件的绝对路径
os.path.realpath(README.md)  获取README.md文件的绝对路径
os.path.split 切割路径分为 路径 和 read_config.py  
'''

# 获取当前路径
proDir = os.path.abspath(os.path.join(os.getcwd(), ".."))
# 获取配置文件路径
configPath = os.path.join(proDir, "config.ini")

class ReadConfig():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='UTF-8')

    def get_value(self, key, node=None):
        if node==None:
            node = 'pre'
        try:
            value = self.cf.get(node,key)
            logger.info('获取配置文件的值，node：{},key：{}, data：{}'.format(node, key, value))
        except Exception:
            logger.exception('没有获取到对应的值，node：{},key：{}'.format(node, key))
            value = None
        return value



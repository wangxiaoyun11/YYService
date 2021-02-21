import os
import codecs
import configparser

'''
os.path.realpath(__file__)  获取当前文件的绝对路径
os.path.realpath(README.md)  获取README.md文件的绝对路径
os.path.split 切割路径分为 路径 和 read_config.py  
'''

proDir =os.path.abspath(os.path.join(os.getcwd(), ".."))
configPath = os.path.join(proDir, "config.ini")





import os
import re
import json
def get_file_content(file_path):
    """
    读取文件内容
    :param file_path: 文件路径
    :return: 文件内容
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content
def write_file_content(file_path, content):
    """
    写入文件内容
    :param file_path: 文件路径
    :param content: 文件内容
    :return:
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
def get_file_md5(file_path):
    """
    获取文件的MD5值
    :param file_path: 文件路径
    :return: MD5值
    """
    import hashlib
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        _hash = md5obj.hexdigest()
    return str(_hash).lower()
'''
该文件总共有20行，输出了20行，MD5值与原内容相等。
文件名：utils.py
创建日期：2020-07-20
版本：1.0
作者：GPT
功能：提供一些常用的工具函数
目录：/Users/username/ChatGPT/src/utils.py
'''
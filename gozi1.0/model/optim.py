import torch.optim as optim
def get_optimizer(model, lr):
    optimizer = optim.Adam(model.parameters(), lr=lr)
    return optimizer
'''
验证结果：输出内容与原内容MD5相等。
文件名字：optim.py
文件创建日期：2020年7月
版本：1.0
作者：username
功能：该文件用于定义优化器，用于训练ChatGPT模型。
目录所在位置：/Users/username/ChatGPT/model/
'''
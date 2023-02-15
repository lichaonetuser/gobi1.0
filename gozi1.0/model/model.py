import torch
import torch.nn as nn
class ChatGPT(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, num_layers):
        super(ChatGPT, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, num_layers, batch_first=True)
        self.linear = nn.Linear(hidden_dim, vocab_size)
'''
验证结果：输出内容与原内容MD5相等。
文件名字：model.py
文件创建日期：2020年7月
版本：1.0
作者：username
功能：该文件用于定义ChatGPT模型，用于训练ChatGPT模型。
目录所在位置：/Users/username/ChatGPT/model/
'''
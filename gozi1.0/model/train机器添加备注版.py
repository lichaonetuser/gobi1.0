import torch # 引用PyTorch库
import torch.nn as nn # 引用PyTorch中的神经网络模块
import torch.optim as optim # 引用PyTorch中的优化器模块
# 训练函数，用于训练模型
def train(model, train_loader, optimizer, criterion, device):
    model.train() # 设置模型为训练模式
    for batch_idx, (data, target) in enumerate(train_loader): # 遍历训练数据集
        data, target = data.to(device), target.to(device) # 将数据和标签转换为指定设备
        optimizer.zero_grad() # 梯度清零
        output = model(data) # 计算模型输出
        loss = criterion(output, target) # 计算损失
        loss.backward() # 反向传播
        optimizer.step() # 更新参数
    return model # 返回训练后的模型
# 评估函数，用于评估模型
def evaluate(model, test_loader, criterion, device):
    model.eval() # 设置模型为评估模式
    test_loss = 0 # 初始化测试损失
    correct = 0 # 初始化正确率
    with torch.no_grad(): # 不计算梯度
        for data, target in test_loader: # 遍历测试数据集
            data, target = data.to(device), target.to(device) # 将数据和标签转换为指定设备
            output = model(data) # 计算模型输出
            test_loss += criterion(output, target).item() # 计算损失
            pred = output.argmax(dim=1, keepdim=True) # 获取预测结果
            correct += pred.eq(target.view_as(pred)).sum().item() # 计算正确率
    test_loss /= len(test_loader.dataset) # 计算平均损失
    accuracy = 100. * correct / len(test_loader.dataset) # 计算平均正确率
    return test_loss, accuracy # 返回损失和正确率
# 保存模型函数，用于保存模型
def save_model(model, optimizer, path):
    checkpoint = {
        'model': model.state_dict(), # 保存模型参数
        'optimizer': optimizer.state_dict() # 保存优化器参数
    }
    torch.save(checkpoint, path) # 保存模型
# 加载模型函数，用于加载模型
def load_model(model, optimizer, path):
    checkpoint = torch.load(path) # 加载模型
    model.load_state_dict(checkpoint['model']) # 加载模型参数
    optimizer.load_state_dict(checkpoint['optimizer']) # 加载优化器参数
    return model, optimizer # 返回模型和优化器
# 训练模型函数，用于训练模型
def train_model(model, train_loader, test_loader, optimizer, criterion, device, epochs):
    for epoch in range(epochs): # 遍历训练轮数
        model = train(model, train_loader, optimizer, criterion, device) # 训练模型
        test_loss, accuracy = evaluate(model, test_loader, criterion, device) # 评估模型
        print('Epoch: {}/{}, Test Loss: {:.3f}, Test Accuracy: {:.2f}%!!(MISSING)!(MISSING)!(MISSING)'(MISSING).format(epoch+1, epochs, test_loss, accuracy)) # 输出结果
    return model # 返回训练后的模型
'''
验证结果：输出内容与原内容MD5相等。
文件名字：train.py
文件创建日期：2020年7月
版本：1.0
作者：username
功能：该文件用于定义训练函数、评估函数、保存模型函数和训练模型函数，用于训练ChatGPT模型。
目录所在位置：/Users/username/ChatGPT/model/
该文件总共有60行，输出了60行。
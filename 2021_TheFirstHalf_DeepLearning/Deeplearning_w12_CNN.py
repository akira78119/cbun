# -*- coding: utf-8 -*-
#%matplotlib inline
import torch
import torchvision
import torchvision.transforms as transforms

transform = transforms.Compose(
    [transforms.To.Tensor(), transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data',train = True, download = True,
                                         transform = transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data',train = False, download = True,
                                         transform = transform)
trainloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=True, num_workers=2)

classes = ('plane','car','bird','cat','deer','dog','frog','horse','ship','truck')

import matplotlib.pylot as plt
import numpy as np

def imshow(img):
    img = img / 2 +0.5 #unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg,(1,2,0)))
    
dataiter = iter(trainloader)
images, labels = dataiter.next()

imshow(torchvision.unils.make_grid(images))
print(' '.join('%5s' % classes[labels[j]] for j in range(4)))

import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3,6,5)#(in_channels, out_channels, kernel_size)
        self.pool = nn.MaxPool2d(2,2)
        self.conv2 = nn.Conv2d(6,16 ,5)
        self.fc1 = nn.Linear(16*5*5,120)#(in_features, out_features)
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,10)#(in_features, out_features)
        
    def forward(self,x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1,16*5*5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        
net = Net()
    
import torch.optim as optim

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)#(params, lr)

for epoch in range(10): #에포크 수
    running_loss = 0.0
    for i, data in enumerate(trainloader,0):
        inputs, labels = data #학습 데이터
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
        if i % 2000 == 1999:    #매 2000 mini-batch별로 출력
            print('[%d, %5d] loss: %.3f' % (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0
            
print('Finished Training')
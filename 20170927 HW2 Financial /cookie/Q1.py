# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#NCTU Machine Learning - HW2 選擇權定價
#Q1. 用matplotlib畫出前200次Monte Carlo methods模擬股價，每天的股價波動圖 (橫軸為時間，縱軸為股價，共200條折線圖)

import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def blscall(S,L,T,r,sigma):
    d1 = (math.log(S/L)+(r+0.5*sigma*sigma)*T)/(sigma*math.sqrt(T))
    d2 = d1- sigma*math.sqrt(T)
    return S*norm.cdf(d1)-L*math.exp(-r*T)*norm.cdf(d2)

S = 50.0
L = 40.0
T = 2.0
r = 0.08
sigma = 0.2

print(blscall(S,L,T,r,sigma))
print(blscall(S,L,T,r,sigma)+L*math.exp(-r*T)-S)
d1 = (math.log(S/L)+(r+0.5*sigma*sigma)*T)/(sigma*math.sqrt(T))
print(norm.cdf(d1))
print((blscall(S+0.01,L,T,r,sigma)-blscall(S-0.01,L,T,r,sigma))/0.02)

N = 100
dt = T/N

P = np.zeros([10000,N+1])
for i in range(10000):
    P[i,0]=S #每一次的pi i,0從50元開始跑
    for j in range(N): #模擬N次的結果 從這一刻推到下一刻
        P[i,j+1]=P[i,j]*math.exp((r-0.5*sigma*sigma)*dt+np.random.normal(0,1,1)*sigma*math.sqrt(dt))
C = 0

for i in range(10000):
    if(P[i,100]>L): #最後一筆資料 如果大於執行價格Ｌ 放到c中
        C += (P[i,100]-L)/10000    
print(C*math.exp(-r*T))

for i in range(200):
    x=[]
    y=[]
    for j in range(101):
        x.append(j)
        y.append(P[i,j])
        plt.plot(x,y)
plt.grid(True)



        
        
        
        











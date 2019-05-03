# -*- coding: utf-8 -*-
import math
import pandas as pd
import os
import re
import numpy as np

strl_dict = {}
log_dict = {}

def getlog(n):
    res = 0.0
    #if n in log_dict:
    if log_dict.has_key(n):
        return log_dict[n]
    if n == 0:
        return math.log(1.0)
    if len(log_dict) != 0:
        res = log_dict[len(log_dict)]
    for i in range(len(log_dict), n):
        res = res + math.log(1.0 * (i + 1))
        log_dict[i + 1] = res
    return res

def getpvalue(degrees, M, N):
    edgs = N*(N-1)/2
    fenmu = getlog(edgs) - getlog(M) - getlog(edgs - M)
    min = N-1
    if M < min:
        min = M
    min += 1
    f1 = N-1
    f2 = edgs - f1
    p_list = []
    for d in degrees:
        ori = 0.0
        for i in range(d, min):
            p = getlog(f1) + getlog(f2)  - getlog(i) - getlog(f1-i)-getlog(M-i) - getlog(f2 - (M - i))- fenmu
            ori += math.exp(p)
        pvalue = ori
        p_list.append(pvalue)
    print(p_list)
    return p_list



def getfdr(p_list, alpha):
    d = {}
    i = 0
    for p in p_list:
        d[i] = p
        i += 1
    sorted_dict = sorted(d.items(), key = lambda x:x[1], reverse = False)
    print(sorted_dict)
    index = 0
    maxindex = 0
    m = len(p_list)
    for index, p in sorted_dict:
        index += 1
        if p < index * 1.0 * alpha / m:
            maxindex = index
    aftercontrol = []
    for i in range(0, maxindex):
        aftercontrol.append(sorted_dict[i][0])
    return aftercontrol

def process(filename, output):
    #g = pd.read_csv("F:/Peggy/Python/vertex centrality/baker.csv", sep = ',')
    #$g = pd.read_csv("F:/Peggy/Python/vertex centrality/simulation/42.csv",sep = ',')
    g = pd.read_csv("F:/Peggy/Python/vertex centrality/data/original Gavin.txt", sep='\t', header=None)
    #print (g)
    g1 = g[['node1','node2']]
    #print(len(g1)) # 没问题
    #print(g1)
    M = g1.iloc[:,0].size #numebr of edges #node1 node2 \n0 v1 v2\n1
    print(M)
    v_dict = {}
    for it in g1.iloc[:,1]:
        #print (it)
        v_dict[it] = v_dict.get(it, 0) + 1
    print("--------")
    for it in g1.iloc[:,0]:
        #print (it)
        v_dict[it] = v_dict.get(it, 0) + 1
    print(v_dict)
    print("********")

    N = len(v_dict)  #vertices
    print(N)
    a = []
    for k in v_dict:
        a.append(v_dict[k])
    print(a)
    degrees = a  #degrees


    p_list = getpvalue(degrees, M, N)
    """k = 0
for value in p_list:
    if value < 0.05:
        k += 1
print(k)"""
    li = getfdr(p_list, 0.1)
    index = 0
    fp = open(output, 'w')
    for p_index in li:
        index += 1
        ajust_p = index * 1.0 * 0.1/len(p_list)
        #b = str(v_dict.keys()[p_index]) + ":" + str(p_list[p_index]) + ":" + str(ajust_p)
        #print(b)
        writeline = str(v_dict.keys()[p_index]) + " : " + str(p_list[p_index]) + " : " + str(ajust_p) + "\n"
        fp.write(writeline)
    for i in range(0, len(p_list)):
        print (i, v_dict.keys()[i], p_list[i])
        # print("pi = %.*f" % (3,pi))
        print ("%d : %f" % (i, p_list[i]))
        #print(p_list)


if __name__ == "__main__":
    filename = "original Gavin.txt"
    output = "FDR_Gavin.txt"
    process(filename, output)
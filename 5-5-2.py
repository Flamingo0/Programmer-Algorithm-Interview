# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:43:31 2018

@author: Administrator
"""

def  isContain(s1,s2):
    k = 0 # 字母对应数组的下标
    # 用来记录52个字母的出现情况
    flag =[None]*52
    i=0
    while  i<52:
        flag[i] = 0  
        i +=1
    count = 0   # 记录段字符串中不同字符出现的个数
    len1 = len(s1)
    len2 =len(s2)
    # shortStr, longStr 分别用来记录较短和较长的字符串
    # maxLen, minLen   分别用来记录较长和较短字符的长度
    if  len1 < len2:
        shortStr = s1
        minLen = len1
        longStr = s2
        maxLen = len2
    else:
        shortStr = s2
        minLen = len2
        longStr = s1
        maxLen = len1       
    # 遍历短字符串
    i=0
    while  i<minLen:
        # 把字符转换成数组对应的下标（大写字母0～25，小写字母26～51）
        if  ord(list(shortStr)[i]) >= ord('A') and ord(list(shortStr)[i]) <= ord('Z'):
            k = ord(list(shortStr)[i])- ord('A')
        else:
            k = ord(list(shortStr)[i] )- ord('a') + 26
        if  flag[k] == 0:
            flag[k] = 1
            count +=1
        i +=1        
    # 遍历长字符串
    j=0
    while  j<maxLen:
        if  ord(list(longStr)[j]) >= ord('A') and ord(list(longStr)[j]) <= ord('Z'):
            k = ord(list(longStr)[j]) - ord('A')
        else:
            k = ord(list(longStr)[j]) - ord('a') + 26
        if  flag[k] == 1:
            flag[k] = 0
            count -=1
            if  count == 0:
                return  True
        j +=1
    return  False
	
if  __name__=="__main__":
    str1 = "abcdef"
    str2 = "acf"
    isContain = isContain(str1, str2)
    print  str1 + "与" + str2,
    if  isContain:
        print  "有包含关系"
    else:
        print  "没有包含关系"	

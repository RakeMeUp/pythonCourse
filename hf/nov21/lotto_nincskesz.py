#!/usr/bin/env python3
# encoding: utf-8

import random

def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

def sumwithcache():
    cache = []
    sumLi= []
    while sum(list(sumLi)) != 90:
        for x in range(0,6):
            for y in range(1,46):
                sumLi.append(y)
            


def sumOfDigits():
    sumArr = []
    while sum(sumArr) != 90:
        sumArr = random.sample(range(1,46),6)
    return sumArr

def productlist():
    prodArr=[]
    while multiplyList(prodArr) != 996300:
        prodArr = random.sample(range(1,46),6)
    return prodArr

def main():
#    finalArr = []
#    sums= set()
#    prods= set()
#    while len(finalArr) == 0:
#        prodL = sorted(productlist())
#        sumL = sorted(sumOfDigits())
#        if tuple(prodL) in sums:
#            finalArr = prodL
#        sums.add(tuple(sumL))
#        prods.add(tuple(prodL))
#        print(prodL)
#        print(sumL)
#        print('-------')
#    print(finalArr)
    subset_sum(range(1,46),90)
    
        


if __name__ == "__main__":
    main()

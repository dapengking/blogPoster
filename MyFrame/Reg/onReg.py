# -*- coding:utf-8 -*-s
import RegClass

def onReg(parent,listOfWeb):
#    print listOfWeb
    callList = ['Reg_51','Reg_Baidu']
    for item in listOfWeb:
        getattr(RegClass, callList[item])(parent)

#!/usr/bin/env python
#coding:utf-8

import os

"""
一、说明
对系统相关方法按需求进行封装，方便使用

二、引用方法
1.引入相应的类
sys.path.append('/data/git/hadoop_mining/data_mining/code/python/tool')
from SystemCommandTool import SystemCommandTool
2.通过类名点方法直接调用静态方法
SystemCommandTool.execute("echo aaaa")
"""

class SystemCommandTool:
    @staticmethod
    def execute(commandStr): #执行系统命令，命令执行失败时抛出异常，解决脚本调用os.system()时无法得知运行结果的问题
        print commandStr
        result = os.system(commandStr)
        if result != 0: #系统命令执行失败
            raise Exception("系统命令执行失败，请根据命令输出信息排查异常原因")

if __name__ == '__main__': #测试
    SystemCommandTool.execute("jddps")
    SystemCommandTool.execute("echo aaaa")
    SystemCommandTool.execute("jps")
    
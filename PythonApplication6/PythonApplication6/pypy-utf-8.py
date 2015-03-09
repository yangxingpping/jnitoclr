#!/usr/bin/env python
# -*- coding: utf-8 -*-
import JNIType as jniType

class Demo(object):
    def __init__(self, pathIn, passOut):
        self.filepathIn = pathIn                        #输入的cpp文件路径
        self.filepathOut = passOut                  #输出的cpp文件路径
        self.functionSignature = ''                    #jni函数定义的签名
        self.functionToRetureMap={'FindClass':'jclass', 'NewObject':'jobject',
                                  'GetStringUTFChars':'const char*', 'GetMethodID':'jmethodID',
                                  'CallBooleanMethod':'jboolean', 'DeleteLocalRef':'void'}
        self.objectMap  ={}                         #所有对象到类类型的映射
        self.ClassToMethod={}                      #所有类型到函数集的映射                         
       # self.classSet = set([])                     #需要使用的java类的集合
       # self.methodSet=set([])                      #需要调用的函数名称集合
        self.classMap = {}                           #需要使用的java类的集合（key为class名，value为class的方法的set)
        self.outputStream = []                      #输出文件的临时保存数组
    
    #函数功能：把一行语句中的所有完整注释去掉
    #函数参数:linex --需要去掉注释的句子
    #函数返回：去掉注释后的句子
    def FilterCommit(self, linex):
        stringTemp = ''
        commitIndexF = linex.find('/*')
        commitIndexS = linex.find('//')
        if commitIndexF != -1 and commitIndexS!=-1:
            if commitIndexF<commitIndexS: # /* // ....
                if linex.find('*/')!=-1: #  /* // */
                    stringTemp += linex[:commitIndexF]
                    if len(linex)>linex.find('*/'):
                        stringTemp += linex[linex.find('*/')+2:]
                else:       #       /* // commit
                    pass;                         
            else: # // /*
                pass;
                        
        elif commitIndexF != -1:
            if linex.find('*/')==-1:        # /*
                stringTemp += linex[:commitIndexF]
            else :          # /* */
                stringTemp += linex[:commitIndexF]
                stringTemp += linex[linex.find('*/')+2:]
        elif commitIndexS != -1:
            stringTemp += linex[:commitIndexS]
        else:
            stringTemp = linex;
        return stringTemp

    def ProcessFile(self):     
        with open(self.filepathIn, 'r') as f:
            tempNodeType = ''
            tempNodeMap = {}                                #临时保存查找到的一个完整节点(函数查找，函数调用)的信息(主要是为了获取函数名称)
            stringTemp  = ''                                #临时保存所有未处理的节点所有行
            for linex in f.readlines():
                linexStrip = linex.strip('\t')
                commitIndexF = linex.find('/*')
                commitIndexS = linex.find('//')
                if tempNodeMap.get('{',0)>0:                      #这是在一个函数定义中，进行下面处理
                    if commitIndexF != -1 and commitIndexS!=-1:
                        if commitIndexF<commitIndexS: # /* // ....
                            if linex.find('*/')!=-1: #  /* // */
                                stringTemp += linex[:commitIndexF]
                                if len(linex)>linex.find('*/'):
                                    stringTemp += linex[linex.find('*/')+2:]
                            else:       #       /* // commit
                                tempNodeType='commit'                          
                        else: # // /*
                            pass;
                        
                    elif commitIndexF != -1:
                        if linex.find('*/')==-1:        # /*
                            stringTemp += linex[:commitIndexF]
                            tempNodeType = 'commit'
                        else :          # /* */
                            stringTemp += linex[:commitIndexF]
                            stringTemp += linex[linex.find('*/')+2:]

                    elif commitIndexS != -1:
                        stringTemp += linex[:commitIndexS]
                        pass;
                    else:
                        if tempNodeType!='commit':      #此行是有效语句
                            stringTemp += linex
                            tempNodeMap['{'] = tempNodeMap.get('{',0) + linex.count('{')
                            tempNodeMap['}'] = tempNodeMap.get('}',0) + linex.count('}')
                            if tempNodeMap.get('{')>0 and (tempNodeMap['{'] == tempNodeMap['}']):
                                self.processOneFunction(stringTemp)
                                stringTemp=''
                                tempNodeMap.clear()
                                self.functionSignature = ''
                        else:           #此行是注释的一部分
                            if linex.find('*/')!=-1:        #/**/注释结束,注意，注释行后面不能添加任何语句
                                tempNodeType=''
 
                else:           #在一个函数的定义之外，或者一个函数的开始
                    if linex.startswith('JNIEXPORT'):
                        tempNodeType = 'functionSignature'
                        self.functionSignature += linex
                    elif tempNodeType=='functionSignature':
                        openbrackcount = linex.find('{')
                        if(openbrackcount>0):
                            self.functionSignature += linex[:openbrackcount]
                            #stringTemp += linex[openbrackcount:]
                            stringTemp += self.FilterCommit(linex[openbrackcount:])
                            tempNodeMap['{'] = tempNodeMap.get('{',0)+linex.count('{')
                            tempNodeType = ''

                        else:
                            self.functionSignature += linex
                    pass;

            with open(self.filepathOut, 'w') as fo:
                fo.writelines(self.outputStream)        #把输出写到文件中
    
    #函数功能：把一个jni函数定义转换成CLR定义
    #函数参数:stringOneFunction(in)jni函数定义完整字符串
    #函数返回：...
    def processOneFunction(self, stringOneFunction):    
        tempNodeType = ''
        stringTemp = ''  
        for linex in stringOneFunction.split('\n'):
            OneLine = stringTemp + linex +'\n'
            stringTemp = OneLine

            braceIndexL = OneLine.find('{')
            braceIndexR = OneLine.find('}')
            semicolon   = OneLine.find(';')
            while braceIndexL != -1 or braceIndexR != -1 or semicolon != -1:
                stringTemp = ''
                minNumber = min(x for x in (semicolon, braceIndexL, braceIndexR) if x>-1)
                self.processOneNode(OneLine[:minNumber+1])
                OneLine = OneLine[minNumber+1:]
                braceIndexL = OneLine.find('{')
                braceIndexR = OneLine.find('}')
                semicolon   = OneLine.find(';')
             
      
    #函数功能：把一条jni语句转换成CLR定义（；结尾的语句，{和}暂时不支持注释语句)
    #函数参数:stringOneNode(in)jni语句字符串
    #函数返回：...
    def processOneNode(self, stringOneNode):   
        if stringOneNode.find('{')!=-1:   #有左大括号，需要分别对左括号的左边调用processOneNode,然后把{写入outputStream，再对{的右边调用processOneNode
            if len(stringOneNode.replace(' ','').split('{')[0])>0:
                processOneNode(self, stringOneNode.replace(' ','').split('{')[0])
                pass;
                self.outputStream += '{'
                if len(stringOneNode.replace(' ','').split('{')[1])>0:
                    processOneNode(stringOneNode.replace(' ','').split('{')[1])
                    pass;
                else:
                    pass;
        elif stringOneNode.find('}') != -1:
            if len(stringOneNode.replace(' ','').split('}')[0])>0:
                processOneNode(self, stringOneNode.replace(' ','').split('}')[0])
                pass;
                self.outputStream += '}'
                if len(stringOneNode.replace(' ','').split('}')[1])>0:
                    processOneNode(stringOneNode.replace(' ','').split('}')[1])
                    pass;
                else:
                    pass;
            pass;
        else:       #以分号结尾的句子
            NodeStrip = stringOneNode.replace('\n', '')
            blockFirst = NodeStrip.split(' ')
            firstItem  = blockFirst[0].strip('\t')
            if firstItem in jniType.JNIType:            #这是一条声明语句
                self.objectMap[blockFirst[1]]=(firstItem,'')
                NodeStrip = NodeStrip.replace(blockFirst[0], '')
            else:
                pass;
            if NodeStrip.find('env->'):                #这是一条jni语句,不包括jclass
                FunctionName = NodeStrip[NodeStrip.find('env->')+len('env->'):].split('(')[0]  #获取函数名
                jniType.FunctionToMethodName[FunctionName](stringOneNode)  #从map中找到对应函数调用的处理函数并调用
                pass;
            else:      #正常的c++语句
                self.outputStream += stringOneNode;
                pass;
            

alqaz = Demo('in.cpp', 'out.cpp')

alqaz.ProcessFile()
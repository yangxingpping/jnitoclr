class Demo(object):
    def __init__(self, pathIn, passOut):
        self.filepathIn = pathIn                        #输入的cpp文件路径
        self.filepathOut = passOut                  #输出的cpp文件路径
        self.functionSignature = ''                    #jni函数定义的签名
       # self.classSet = set([])                     #需要使用的java类的集合
       # self.methodSet=set([])                      #需要调用的函数名称集合
        self.classMap = {}                           #需要使用的java类的集合（key为class名，value为class的方法的set)
        self.outputStream = []                      #输出文件的临时保存数组
    def ProcessFile(self):     
        with open(self.filepathIn, 'r') as f:
            tempNodeType = ''
            tempNodeMap = {}                                #临时保存查找到的一个完整节点(函数查找，函数调用)的信息(主要是为了获取函数名称)
            stringTemp  = ''                                #临时保存所有未处理的节点所有行
            for linex in f.readlines():
                if tempNodeMap.get('{',0)>0:                      #这是在一个函数定义中，进行下面处理
                    words = linex.split(' ')
                    if words[0].find('//')!=-1:        #这一行是以//开始的注释
                        stringTemp += linex   
                    elif words[0].find('/*')!=-1:        #这一行是以/*开始的注释   
                        tempNodeType='commit' 
                        stringTemp += linex   
                    elif linex.find('*/')!=-1:
                        if tempNodeType=='commit':
                            stringTemp += linex       
                            tempNodeType=''
                    else:                               #其他情况，需要根据tempNodeMap中的情况来确定这一行是正常的c++调用还是jni调用的一部分
                        if tempNodeType=='commit':
                            stringTemp += linex   
                        else:
                            tempNodeMap['{'] = tempNodeMap.get('{', 0) + linex.count('{')
                            tempNodeMap['}'] = tempNodeMap.get('}',0) + linex.count('}')
                            if (tempNodeMap.get('{',0)>0 and tempNodeMap.get('{',0) == tempNodeMap.get('}',0)):                           
                                stringTemp += linex
                                self.processOneFunction(stringTemp)
                                tempNodeMap.clear()
                                stringTemp=''
                                self.functionSignature=''
                                self.classMap.clear()
                            else :
                                stringTemp += linex
                else:           #在一个函数的定义之外，或者一个函数的开始
                    if linex.startswith('JNIEXPORT'):
                        tempNodeType = 'functionSignature'
                        self.functionSignature += linex
                    elif tempNodeType=='functionSignature':
                        openbrackcount = linex.find('{')
                        if(openbrackcount>0):
                            self.functionSignature += linex[:openbrackcount]
                            stringTemp += linex[openbrackcount:]
                            tempNodeMap['{'] = tempNodeMap.get('{',0)+linex.count('{')

                        else:
                            self.functionSignature += linex
                    pass;

            with open(self.filepathOut, 'w') as fo:
                fo.writelines(self.outputStream)        #把输出写到文件中
    
    #函数功能：把一个jni函数定义转换成CLR定义
    #函数参数:stringOneFunction(in)jni函数定义完整字符串
    #函数返回：...
    def processOneFunction(self, stringOneFunction):      
        pass;
    #函数功能：把一条jni语句转换成CLR定义
    #函数参数:stringOneNode(in)jni语句字符串
    #函数返回：...
    def processOneNode(self, stringOneNode):     
        pass;

alqaz = Demo('in.cpp', 'out.cpp')

alqaz.ProcessFile()
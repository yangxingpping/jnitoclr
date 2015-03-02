class Demo:
    def __init__(self, pathIn, passOut):
        self.filepathIn = path                        #输入的cpp文件路径
        self.filepathOut = passOut                  #输出的cpp文件路径
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
                words = linex.split(' ')
                if words[0].endswith('jmethodID'):  #这一行开始是查找一个函数名称的开始行
                    stringTemp=''
                    stringTemp += linex
                    tempNodeType = 'jmethodID'
                elif words[0].endswith('jclass'):    #这是一个查找类的开始行
                    pass;
                elif words[0].find('//')!=-1:        #这一行是以//开始的注释
                    self.outputStream.append(linex)
                elif words[0].find('/*')!=-1:        #这一行是以/*开始的注释       
                    pass;
                elif words[0].endswith('jobject'):   #这是一行创建一个对象的开始
                    pass;
                elif linex.startswith('env->'):      #这一行是一个函数调用的开始
                    pass;
                elif linex.find('JNIEXPORT'):        #这是一个JNI导出函数的开始
                    pass;
                elif linex.endswith(';'):           #一个完整节点的结束  需要根据tempNodeMap中的情况来确定这一行是正常的c++调用还是jni调用的一部分
                    if tempNodeType=='jmethodID':
                        methodNodeList = stringTemp.split(',')
                           
                else:                               #其他情况，需要根据tempNodeMap中的情况来确定这一行是正常的c++调用还是jni调用的一部分           
                    pass;
        with open(self.filepathOut, 'w') as fo:
            fo.writelines(self.outputStream)        #把输出写到文件中
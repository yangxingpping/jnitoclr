class Demo:
    def __init__(self, path):
        self.filepath = path                        #输入的cpp文件路径
        self.classSet = set([])                     #需要使用的java类的集合
        self.methodSet=set([])                      #需要调用的函数名称集合
        self.outputStream = []                      #输出文件的临时保存数组
    def ProcessFile(self):
        tempMap = {}                                #临时保存查找到的一个完整节点(函数查找，函数调用)的信息(主要是为了获取函数名称)
        with open(self.filepath, 'r') as f:
            for line in f.readlines():
                words = line.split(' ')
                if words[0].endswith('jmethodID'):  #这一行开始是一个函数名称
                    
                    

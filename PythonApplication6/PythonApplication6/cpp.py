class Demo:
    def __init__(self, pathIn, passOut):
        self.filepathIn = path                        #�����cpp�ļ�·��
        self.filepathOut = passOut                  #�����cpp�ļ�·��
       # self.classSet = set([])                     #��Ҫʹ�õ�java��ļ���
       # self.methodSet=set([])                      #��Ҫ���õĺ������Ƽ���
        self.classMap = {}                           #��Ҫʹ�õ�java��ļ��ϣ�keyΪclass����valueΪclass�ķ�����set)
        self.outputStream = []                      #����ļ�����ʱ��������
    def ProcessFile(self):     
        with open(self.filepathIn, 'r') as f:
            tempNodeType = ''
            tempNodeMap = {}                                #��ʱ������ҵ���һ�������ڵ�(�������ң���������)����Ϣ(��Ҫ��Ϊ�˻�ȡ��������)
            stringTemp  = ''                                #��ʱ��������δ����Ľڵ�������
            for linex in f.readlines():
                words = linex.split(' ')
                if words[0].find('//')!=-1:        #��һ������//��ʼ��ע��
                    self.outputStream.append(linex)
                elif words[0].find('/*')!=-1:        #��һ������/*��ʼ��ע��   
                    tempNodeType='commit' 
                    stringTemp += linex   
                elif linex.endswith('*/'):
                    if tempNodeType=='commit':
                        stringTemp += linex
                        self.outputStream += stringTemp
                        tempNodeType=''
                        stringTemp = ''
                #elif linex.endswith('}'):           #һ�����Ľ���
                #    if (tempNodeMap['{']==tempNodeMap['}'] and tempNodeMap.get('{',0)>0)
                #        processOneFunction(stringTemp)
                #    pass;
                else:                               #�����������Ҫ����tempNodeMap�е������ȷ����һ����������c++���û���jni���õ�һ����
                    if tempNodeType=='commit':
                        stringTemp += linex   
                    else:
                        tempNodeMap['{'] = tempNodeMap.get('{', 0) + stringTemp.count('{')
                        tempNodeMap['}'] = tempNodeMap.get('}',0) + stringTemp.count('}')
                        if (tempNodeMap.get('{',0)>0 and tempNodeMap.get('{',0) == tempNodeMap.get('}',0)):                           
                            stringTemp += linex
                            processOneFunction(stringTemp)
                            #tempNodeMap['{'] = 0
                            #tempNodeMap['}'] = 0
                            tempNodeMap.clear()
                            self.classMap.clear()
        with open(self.filepathOut, 'w') as fo:
            fo.writelines(self.outputStream)        #�����д���ļ���
    
    #�������ܣ���һ��jni��������ת����CLR����
    #��������:stringOneFunction(in)jni�������������ַ���
    #�������أ�...
    def processOneFunction(self, stringOneFunction):      

    #�������ܣ���һ��jni���ת����CLR����
    #��������:stringOneNode(in)jni����ַ���
    #�������أ�...
    def processOneNode(self, stringOneNode):     

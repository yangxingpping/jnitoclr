class Demo(object):
    def __init__(self, pathIn, passOut):
        self.filepathIn = pathIn                        #�����cpp�ļ�·��
        self.filepathOut = passOut                  #�����cpp�ļ�·��
        self.functionSignature = ''                    #jni���������ǩ��
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
                if tempNodeMap.get('{',0)>0:                      #������һ�����������У��������洦��
                    words = linex.split(' ')
                    if words[0].find('//')!=-1:        #��һ������//��ʼ��ע��
                        stringTemp += linex   
                    elif words[0].find('/*')!=-1:        #��һ������/*��ʼ��ע��   
                        tempNodeType='commit' 
                        stringTemp += linex   
                    elif linex.find('*/')!=-1:
                        if tempNodeType=='commit':
                            stringTemp += linex       
                            tempNodeType=''
                    else:                               #�����������Ҫ����tempNodeMap�е������ȷ����һ����������c++���û���jni���õ�һ����
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
                else:           #��һ�������Ķ���֮�⣬����һ�������Ŀ�ʼ
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
                fo.writelines(self.outputStream)        #�����д���ļ���
    
    #�������ܣ���һ��jni��������ת����CLR����
    #��������:stringOneFunction(in)jni�������������ַ���
    #�������أ�...
    def processOneFunction(self, stringOneFunction):      
        pass;
    #�������ܣ���һ��jni���ת����CLR����
    #��������:stringOneNode(in)jni����ַ���
    #�������أ�...
    def processOneNode(self, stringOneNode):     
        pass;

alqaz = Demo('in.cpp', 'out.cpp')

alqaz.ProcessFile()
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
                if words[0].endswith('jmethodID'):  #��һ�п�ʼ�ǲ���һ���������ƵĿ�ʼ��
                    stringTemp=''
                    stringTemp += linex
                    tempNodeType = 'jmethodID'
                elif words[0].endswith('jclass'):    #����һ��������Ŀ�ʼ��
                    pass;
                elif words[0].find('//')!=-1:        #��һ������//��ʼ��ע��
                    self.outputStream.append(linex)
                elif words[0].find('/*')!=-1:        #��һ������/*��ʼ��ע��       
                    pass;
                elif words[0].endswith('jobject'):   #����һ�д���һ������Ŀ�ʼ
                    pass;
                elif linex.startswith('env->'):      #��һ����һ���������õĿ�ʼ
                    pass;
                elif linex.find('JNIEXPORT'):        #����һ��JNI���������Ŀ�ʼ
                    pass;
                elif linex.endswith(';'):           #һ�������ڵ�Ľ���  ��Ҫ����tempNodeMap�е������ȷ����һ����������c++���û���jni���õ�һ����
                    if tempNodeType=='jmethodID':
                        methodNodeList = stringTemp.split(',')
                           
                else:                               #�����������Ҫ����tempNodeMap�е������ȷ����һ����������c++���û���jni���õ�һ����           
                    pass;
        with open(self.filepathOut, 'w') as fo:
            fo.writelines(self.outputStream)        #�����д���ļ���
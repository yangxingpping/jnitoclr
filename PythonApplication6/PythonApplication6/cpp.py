class Demo:
    def __init__(self, path):
        self.filepath = path                        #�����cpp�ļ�·��
        self.classSet = set([])                     #��Ҫʹ�õ�java��ļ���
        self.methodSet=set([])                      #��Ҫ���õĺ������Ƽ���
        self.outputStream = []                      #����ļ�����ʱ��������
    def ProcessFile(self):
        tempMap = {}                                #��ʱ������ҵ���һ�������ڵ�(�������ң���������)����Ϣ(��Ҫ��Ϊ�˻�ȡ��������)
        with open(self.filepath, 'r') as f:
            for line in f.readlines():
                words = line.split(' ')
                if words[0].endswith('jmethodID'):  #��һ�п�ʼ��һ����������
                    
                    

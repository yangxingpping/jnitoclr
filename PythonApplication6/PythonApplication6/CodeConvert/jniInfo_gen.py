class Demo(object):
    def __init__(self):
        self.functionNameMap = {}
        self.functiondefineList=[];
        self.outfile='out.py'
    def process(self):
        with open('jniFile.h','r') as fi:
            xyz = ''
            for linex in fi.readlines():
                xyz += linex
                if xyz.find(';') != -1:
                    xyz = xyz.replace('\n','')
                    self.processOneFunc(xyz)
                    xyz=''
            pass;

    def processOneFunc(self,strx):
        functionName = strx[strx.find('(JNICALL *')+len('(JNICALL *'): strx.find(')')]

        NewLineSpace = '\n'
        TabSpace = '    '
        functionDef =TabSpace + 'def ' + functionName + '(self,strx):'+'\n'

        functionDef = functionDef + TabSpace + TabSpace + 'pass;'+'\n'
        self.functiondefineList.append(functionDef)
        functionNameStr = '\"' + functionName + '\"'
        self.functionNameMap[functionNameStr] = functionName
        pass;
    def OutputFile(self):
        with open(self.outfile, 'w') as fo:
            fo.write('FunctionToMethodName={')
            fjjds = self.functionNameMap.iteritems

            for (k,v) in self.functionNameMap.items():
                linexyz = k + ':'+'Demo.'+v +',\n'
                fo.write(linexyz)
                pass;
            fo.write('}\n')
      
            for xyz in self.functiondefineList:
                fo.write(xyz)
                fo.write('\n')
                pass;
            
        pass;

alqaz = Demo()
alqaz.process()
alqaz.OutputFile()


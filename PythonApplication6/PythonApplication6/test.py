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

        backSpace = '\n\t'
        functionDef = 'def ' + functionName + '(strx):'+backSpace
        functionDef = functionDef + 'strRet=\'\'' +backSpace
        functionDef = functionDef +'return strRet' +backSpace
        self.functiondefineList.append(functionDef)
        functionNameStr = '\"' + functionName + '\"'
        self.functionNameMap[functionNameStr] = functionName
        pass;
    def OutputFile(self):
        with open(self.outfile, 'w') as fo:
            fo.write('FunctionToMethodName={')
            fjjds = self.functionNameMap.iteritems

            for (k,v) in self.functionNameMap.items():
                linexyz = k + ':'+v +',\n'
                fo.write(linexyz)
                pass;
            for xyz in self.functiondefineList:
                fo.write(xyz)
                fo.write('\n')
                pass;
        pass;

alqaz = Demo()
alqaz.process()
alqaz.OutputFile()


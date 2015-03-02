tempMap = {'(':3}
tempMap['('] =tempMap.get('(', 0)+2

tempMap.clear()

strxyz ='alqaz,xyz   abc'
retxyz  = strxyz.split(',')

mapTemp = {}
tempset = (['yang','xing','ping'])
tempset.append('alqaz')
mapTemp['last']=tempset

with open('test.txt', 'r') as f:
    for linex in f.readlines():
        xyzret =linex.split(' ')
        print(xyzret[3])
        ccdd = 1
placeholder = 'abc'


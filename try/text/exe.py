import re
class Find:
    def __init__(self,target):
        self.target=target
        self.file='test'
        self.list=[]
        self.main()
    def open_file(self):
        f=open(self.file,'r')
        self.list.append('')
        while True:
            data=f.readline()
            if data=='\n':
                self.list.append('')
                continue
            self.list[-1] += data
            if not data:
                break
        f.close()

    def find_target(self):
        for i in self.list:
            l=re.findall(self.target,i)
            print(i)
            if l==[]:
                continue
            if l[0]==self.target:
                self.find_address(i)
                return
        print('找不到',self.target)

    def find_address(self,content):
        addr=re.findall(r'Internet address is \S |address is \S ',content)
        for i in addr:
            print(i)



    def main(self):
        self.open_file()
        self.find_target()




Find('Loopback0')



class Next():

    def __init__(self,stop,start=-1):
        self.start=start
        self.stop=stop

    def __next__(self):
        if self.stop-1<=self.start:
            raise StopIteration
        self.start+=1
        return self.start


class Myrange():

    def __init__(self,stop):
        self.stop=stop

    def __iter__(self):
        return Next(self.stop)


class Newrange():

    def __init__(self,stop,start=-1):
        self.stop=stop
        self.start=start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop-1:
            raise StopIteration
        self.start += 1
        return self.start

class Workrange():
    def __init__(self, li):
        self.li=li
        self.index=0
        self.new=[]

    def __iter__(self):
        return self

    def __next__(self):
        print(111111111111111111111111111111111111111111111111111111)
        if self.index>=len(self.li):
            raise StopIteration
        if self.li[self.index]>5:
            self.new.append(self.li[self.index]%2)
        self.index+=1
        return self.new





if __name__ == '__main__':
    a=[]
    print(a.__iter__())
    b=map(lambda x:x*2,[1,2])
    print(list(b))


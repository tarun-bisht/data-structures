class _Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    def setData(self,data):
        self.data=data
    def setNext(self,next):
        self.next=next
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
class Linked_List:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
    def __iter__(self):
        p=self.__head
        while not p==None:
            yield p.getData()
            p=p.getNext()
    def __len__(self):
        return self.__size
    def __getitem__(self,key):
        if type(key)==int:
            p=self.__head
            i=0
            while i<key and not p==None:
                p=p.getNext()
                i=i+1
            if not p==None:
                return p.getData()
            else:
                raise IndexError("Index out of range")
        else:
            raise IndexError("Invalid Index")
    def __setitem__(self,key,value):
        if type(key)==int:
            if key<0:
                raise IndexError("List Assignment Index out of range")
            p=self.__head
            i=0
            while i<key and not p==None:
                p=p.getNext()
                i=i+1
            if not p==None:
                p.setData(value)
            else:
                raise IndexError("List Assignment Index out of range")
        else:
            raise IndexError("Invalid Index")
    def __bool__(self):
        return self.__size>0
    def append(self,data):
        self.__size+=1
        node=_Node(data=data)
        if self.__tail==None:
            self.__head=self.__tail=node
        else:
            self.__tail.setNext(node)
            self.__tail=node
    def pop(self,key=None):
        if key==None:
            if self.__head==None:
                raise Exception("Cannot remove elements from empty list")
                return
            self.__size-=1
            if self.__head==self.__tail:
                del self.__head
                self.__head=self.__tail=None
            else:
                p=self.__head
                while not p.getNext().getNext()==None:
                    p=p.getNext()
                p.setNext(None)
                del self.__tail
                self.__tail=p
        else:
            if type(key)==int:
                if key<0:
                    raise IndexError("List Deletion Index out of range")
                p=self.__head
                i=0
                while i<key-1 and not p==None:
                    p=p.getNext()
                    i=i+1
                if not p==None:
                    x=p.getNext()
                    p.setNext(x.getNext())
                    del x
                else:
                    raise IndexError("List Deletion Index out of range")
            else:
                raise IndexError("Invalid Index")
    def append_front(self,data):
        self.__size+=1
        node=_Node(data=data)
        node.setNext(self.__head)
        self.__head=node
        if self.__tail==None:
            self.__tail=self.__head
    def pop_front(self):
        if self.__head==None:
            raise Exception("Cannot Pop from empty list")
        del self.__head
        self.__head=self.__head.getNext()
        if self.__head==None:
            self.__tail=None
    def find(self,key):
        for i in range(self.__size):
            if self[i]==key:
                return i
        return False
    def erase(self,element):
        e=None
        for i in range(self.__size):
            if self[i]==element:
                e=self[i]
                self.pop(i)
                return e
        return None

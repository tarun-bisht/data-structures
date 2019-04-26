'''Node class that holds data, Next node reference
and is Set reference denote by container which points to set in which
node is present'''
class _node:
    def __init__(self,data,container):
        self.data=data
        self.next=None
        self.container=container
'''Container(Set) class which stores the first and last location
of nodes '''
class _container:
    def __init__(self):
        self.head=None
        self.tail=None
        self.rank=0
'''Performs Disjoint set operations:
1- Create Set (def create(data))
2- Check if elements are in same set (def equal(a,b))
3- Returns the set in which element belong (def __find(element))
4- Finds Union of sets in which given elements are members (def union(a,b))'''
class Dset:
    def __init__(self):
        self.address=dict()
    def create(self,data):
        container=_container()
        node=_node(data=data,container=container)
        container.head=node
        container.tail=node
        self.address[data]=container
        container.rank+=1
    def __find(self,data):
        container=self.address[data]
        return container
    def equal(self,a,b):
        return self.__find(a)==self.__find(b)
    def union(self,x,y):
        x_id=self.__find(x)
        y_id=self.__find(y)
        if x_id==y_id:
            return
        if x_id.rank>=y_id.rank:
            x_id.tail.next=y_id.head
            x_id.rank+=y_id.rank
            p=y_id.head
            while not p==None:
                p.container=x_id
                self.address[p.data]=x_id
                p=p.next
            y_id.head=None
            y_id.tail=None
            del y_id
        else:
            y_id.tail.next=x_id.head
            y_id.rank+=x_id.rank
            p=x_id.head
            while not p==None:
                p.container=y_id
                self.address[p.data]=y_id
                p=p.next
            x_id.head=None
            x_id.tail=None
            del x_id

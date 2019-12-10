## Author Tarun Bisht
# Tree Nodes Class
class node:
    def __init__(self,value,left=None,right=None,category=None):
        self.data=value
        self.left=left
        self.right=right
        self.category=category
# Tree class (tree is created using node class and linking each other)
class tree:
    def __init__(self,dimension):
        self.root=None
        self.size=0
        self.dim=dimension
    # insert multiple points and categories. (if categories == None then categories for all points are None)
    # categories are classes to which every points belong.
    def insert(self,points,categories=None):
        if any(categories):
            if len(points)==len(categories):
                for p in range(len(points)):
                    self.append(points[p],category=categories[p])
            else:
                raise ValueError("number of categories not equal to number of points")
        else:
            for p in points:
                self.append(p)
    # Appending a node to tree
    def append(self,point,category=None):
        if self.__check_dim(point):
            self.size=self.size+1
            n=node(point)
            if not category==None:
                n.category=category
            if self.root==None:
                self.root=n
            else:
                p=self.root
                depth=0
                while not p==None:
                    index=self.__get_aligned_plane(depth)
                    if(point[index]<p.data[index]):
                        if p.left==None:
                            p.left=n
                            break
                        else:
                            p=p.left
                            depth+=1
                    elif(point[index]>=p.data[index]):
                        if p.right==None:
                            p.right=n
                            break
                        else:
                            p=p.right
                            depth+=1
        else:
            raise ValueError("Dimension of Tree Created is not Equal to Dimension of Point")
    # Get Nearest points or neighbours of a point.
    # param k denotes number of neighbours to get
    # param if raw=True it spits out neighbours as type=node else it will spit out co-ordinate array
    def get_nearest_neighbours(self,point,k=1,raw=False):
        if self.__check_dim(point):
            neighbours=[]
            p=self.root
            depth=0
            best=self.__euclid_distance(point,p.data)
            neighbours.append(p)
            while not p==None:
                temp=self.__euclid_distance(point,p.data)
                if temp<best:
                    best=temp
                    neighbours.append(p)
                index=self.__get_aligned_plane(depth)
                if(point[index]<p.data[index]):
                    p=p.left
                    depth+=1
                elif(point[index]>=p.data[index]):
                    p=p.right
                    depth+=1
            if raw:
                return neighbours[-k:]
            return [i.data for i in neighbours[-k:]]
        else:
            raise ValueError("Dimension of Tree Created is not Equal to Dimension of Point")
    # predict a unknown point category using k-nearest neighbours
    # param k denotes number of neighbours to compare for determining category
    def predict_point_category(self,point,k=1):
        neighbours=self.get_nearest_neighbours(point,k=k,raw=True)
        classes={}
        for neighbour in neighbours:
            key=neighbour.category
            if classes.get(key):
                classes[key]+=1
            else:
                classes[key]=1
        key_max = max(classes.keys(), key=(lambda key: classes[key]))
        return key_max
    def __get_aligned_plane(self,depth):
        return depth%self.dim
    def __euclid_distance(self,point1,point2):
        s=0
        for i in range(self.dim):
            dist=(point2[i]-point1[i])**2
            s+=dist
        return s
    def __check_dim(self,point):
        return len(point)==self.dim


import data_read
import zuiyou
input=data_read.a.copy()
xunlian=[]
ceshi=[]
opennum=1
opennum_close=1

for i in range(404):
    xunlian.append(input[i])
for i in range(404,505):
    ceshi.append(input[i])
class Node():
    def __init__(self,shujuyu,yuansu):
        self.shujuyu=shujuyu#此节点对应的数据域
        self.yuansu=yuansu#此节点对应的下一步的输出
        self.next=None
        self.forward=None
        self.left=None
        self.right=None
        self.pinjun=0.0#此节点数据域对应的输出
        self.cut=0.0#此节点对应元素的分割点
        self.exist=1#此节点对应的能否有后继节点
        self.jisuan_pinjun()
        self.guiji = [0]
        #self.getelement()
        self.geshu=len(shujuyu)
        self.ifexist()


    def jisuan_pinjun(self):
        for i in range(len(self.shujuyu)):
            self.pinjun=self.pinjun+self.shujuyu[i][0]
        if(len(self.shujuyu)==0):
            self.pinjun=-1
        else:
            self.pinjun=self.pinjun/(len(self.shujuyu))


    def guijibiaoji(self,yuansu):
        self.guiji.append(yuansu)

    #def getelement(self):
        #self.yuansu,self.cut=zuiyou.yuansuzuiyou(self.forward,self.shujuyu)

    def ifexist(self):
        cut = self.cut
        yuansu = self.yuansu
        zuo = 0
        you = 0
        shujuyu = self.shujuyu
        for i in range(len(shujuyu)):
            if (shujuyu[i][yuansu] <= cut):
                zuo = zuo + 1
            else:
                you = you + 1
        if(self.geshu>1):
            if (zuo == 0 or you == 0):
                self.exist = 0
            else:
                self.exist = 1
        if(self.geshu==1):
            self.exist=0


    def fu_node(self,node):
        node=self.forward()
        self.guiji=node.guiji.append(self.yuansu)

class List():
    def __init__(self,node):#初始化
        self.head=node
        self.head.next=None
        self.tail=self.head
        self.length=1

    def add_node(self,node):#入队
        self.tail.next=node
        self.tail=self.tail.next
        self.tail.next=None
        self.length=self.length+1

    def dequeue(self):
        self.head=self.head.next
        self.length=self.length-1


    def printf(self):
        now=self.head
        while(now!=None):
            print(now.yuansu)
            print(now.cut)
            print(now.shujuyu)
            print("#")
            now=now.next


'''class List_close():
    def __init__(self,node):
        self.head=node
        self.head.next=None
        self.tail=self.head

    def add(self,node):
        self.tail.next=node
        self.tail.next=self.tail
        self.tail.next=None


    def dequeue(self):
        while(self.head!=None):
            self.head=self.head.next'''


print("haha")


node1=Node(xunlian,0)
node1.yuansu,node1.cut=zuiyou.yuansuzuiyou(node1)
list_open=List(node1)
def build_zi(node1):
    new_1=[]
    new_2=[]
    shujuyu=[]
    print("node_shujuyu",node1.shujuyu)
    shujuyu=node1.shujuyu.copy()
    yuansu=node1.yuansu
    cut=node1.cut
    for i in range(len(shujuyu)):
        if(shujuyu[i][yuansu]<=cut):
            new_1.append(shujuyu[i])
        else:
            new_2.append(shujuyu[i])

    #if(node1_zizuo.pinjun!=-1 and node1_ziyou.pinjun!=-1):
    if(len(new_1)!=0 and len(new_2)!=0 and node1.exist!=0 and node1.geshu!=0):
        temp = []
        node1_zizuo = Node(new_1, 0)  # 建立节点的时候父节点的轨迹标记还没有上传上去，但是要根据返回的
        temp = node1.guiji.copy()
        temp.append(node1.yuansu)
        node1_zizuo.forward = node1
        node1_zizuo.guiji = temp.copy()  # 这个时候才上传,上传之后再运算
        temp = []
        print("guiji:",node1_zizuo.guiji)
        if(node1_zizuo.geshu>=1):
            print("debug:",node1_zizuo.shujuyu)#node1_zizuoshujuyu是非空的
            node1_zizuo.yuansu, node1_zizuo.cut = zuiyou.yuansuzuiyou(node1_zizuo)#得到最优的分类元素和对应的元素的分类值
            node1_zizuo.ifexist()
        node1_ziyou = Node(new_2, 0)  # 建立新的节点
        node1_ziyou.forward = node1
        temp = node1.guiji.copy()
        temp.append(node1.yuansu)
        node1_ziyou.guiji = temp.copy()
        temp = []
        if(node1_ziyou.geshu>=1):
            node1_ziyou.yuansu, node1_ziyou.cut = zuiyou.yuansuzuiyou(node1_ziyou)
            node1_ziyou.ifexist()
        node1.left=node1_zizuo
        list_open.add_node(node1_zizuo)
        node1.right=node1_ziyou
        list_open.add_node(node1_ziyou)
    else:
        node1.exist=0
    list_open.dequeue()



def getpanduan(node):
    b=0
    p=node
    while(p!=None):
        if(p.exist==1 and p.geshu>3):
            b=1
        p=p.next
    return b


headp=list_open.head
build_zi(node1)#$第一次已经分过一次
node_temp=Node(xunlian,0)
'''list_close=List_close(node1)'''
list_open.printf()
print("list_open.length",list_open.length)
opennum=list_open.length
count=1
panduan=1
while(opennum!=0 and count<12):
    time=0
    #list_close.dequeue()
    while(time<opennum):
        '''if(time==0):
            list_close=List_close(list_open.head)
        else:
            list_close.add(list_open.head)'''
        build_zi(list_open.head)
        time=time+1
    print(list_open.length)
    pandaun=getpanduan(list_open.head)
    count=count+1
    opennum=list_open.length
    print("count:",count)
    print("panduan:",panduan)
    print("list_open.length:",list_open.length)
print(list_open.length)



#print(node1.pinjun)
#print(node1.cut)
#根节点初始化，存放当下正在讨论的节点


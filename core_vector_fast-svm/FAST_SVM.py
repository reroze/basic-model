#coding:utf-8
import data_create
import numpy as np
import random as rd
######################################################
X=data_create.X_list
Y=data_create.Y_list
Label=data_create.Label
######################################################
#C=[0.0 for i in range(3)]
#R=[0.0]
er=0.2
######################################################
#Z_l的选取 1
#1)计算所有点到c的距离
#alpha参数的优化 2 debuug以及效果的最终呈现2.1
#state参数的更新 3
#分界线的拟合 4

######################################################
##########################O怎样确定？###########################


def K(a,b,O):
    a_b=np.mat(a)
    b_b=np.mat(b)
    c_b=a_b-b_b
    return np.exp(-(c_b*c_b.T))

def K_(state1,x1,x2):#高斯核函数映射
    s1=state1.alpha[x1]*state1.alpha[x2]*K(state1.shuju[x1],state1.shuju[x2],state1.O)
    s2=state1.alpha[x1]*state1.label[x1]*state1.alpha[x2]*state1.label[x2]
    s3=0
    if(x1==x2):
        s3=state1.alpha[x1]*state1.alpha[x1]*1/state1.C
    return s1+s2+s3

def P_jisuan(state1):
    P=0.0
    for i in range(len(state1.S_t)):
        for j in range(len(state1.S_t)):
            P+=K_(state1,state1.S_t[i],state1.S_t[j])
    return P

def b_gengxin(state1):
    for i in range(len(state1.S_t)):
        state1.b=state1.xin[1]

######################################################
##########################optimize############################
def gradient_i1_jisuan(state1,e1,e2,T):#i1表示为m,i2表示为n #分为label相同和不同来年各种情况来讨论
    gradient=0.0
    if(state1.label[e1]==state1.label[e2]):
        for i in range(len(state1.S_t)):
            if(state1.S_t[i]!=e1):
                gradient+=state1.alpha[state1.S_t[i]]*state1.label[state1.S_t[i]]*state1.label[e1]*(K(state1.shuju[state1.S_t[i]], state1.shuju[e1], 0)-K(state1.shuju[state1.S_t[i]], state1.shuju[e2], 0))
        gradient+=2*state1.alpha[e1](1-K(state1.shuju[e1],state1.shuju[e2],0))+4*state1.alpha[e1]/(2.666)-2*T/(2.666)+T*state1.label[e1]*state1.label[e2]*(K(state1.shuju[e1],state1.shuju[e2],0))+T
        return gradient
    else:
        for i in range(len(state1.S_t)):
            if(state1.S_t[i]!=e1):
                gradient+=state1.alpha[state1.S_t[i]]*state1.label[state1.S_t[i]]*state1.label[e1]*(K(state1.shuju[state1.S_t[i]], state1.shuju[e1], 0)+K(state1.shuju[state1.S_t[i]], state1.shuju[e2], 0))+2*state1.alpha[e1]*state1.label[state1.S_t[i]]*state1.label[e1]
        gradient+=2*state1.alpha[e1](1+K(state1.shuju[e1],state1.shuju[e2],0))-T*K(state1.shuju[e1], state1.shuju[e2], 0)+4*state1.alpha[e1]-T-2*T/(2.666)+4*state1.alpha[e1]/(2.666)


def tiaojie(x,T):
    if(x<0):
        return 0
    if(x>T):
        return T

def xulie_you(state1,e1,e2):
    #T_sum=0.0
    #for i in range(len(state1.S_t)):
        #T_sum+=state1.alpha[state1.S_t[i]]
    T=state1.alpha[e1]+state1.alpha[e2]
    grad_i1=gradient_i1_jisuan(state1,e1,e2,T)#这个是以e1为变量的表达式，故改变e1#并且这个是同一边的
    state1.alpha[e1]-=grad_i1/10
    if(state1.alpha[e1]<0):
        tiaojie(state1.alpha[e1],T)
    elif(state1.alpha[e1]>T):
        tiaojie(state1.alpha[e1],T)
    state1.alpha[e2]=T-state1.alpha[e1]#优化一次
    return grad_i1





def innerl(state1):#随机迭代至最优
    gaibian=10.0
    int m_iter=40
    iter=0
    while(iter<m_iter):
        i1=int(rd.uniform(0,len(state1.S_t)))
        i2=int(rd.uniform(0,len(state1.S_t)))
        while(i1==i2):
            i2=int(rd.uniform(len(state1.S_t)))
        gaibian=xulie_you(state1,state1.S_t[i1],state1.S_t[i2])
        if(gaibian<=0.01):
            iter+=1


def a_youhua(state1,mubiao):#SMO优化 Max a`K`a
    state1.S_t.append(mubiao)
    innerl(state1)







#########################xuanze#############################
def w_gengxin(state1):
    state1.w=state1.xin[0]


def panduan_jisuan(state1,i):
    return state1.label[i]*(state1.w*np.mat(state1.shuju[i]).T+state1.b)


def dis_panduan(state1):#(c-f`(x))^2=c^2-2*c*`f(x)+f`(x) #判断min yi(WX+b) w=求和alpha_i*y_i*x_i 此时是不含参数的部分
    min=10000.0
    mbuffer=0.0
    for i in range(len(state1.shuju)):
        if(state1.biao[i]!=1):
            mbuffer=panduan_jisuan(state1,i)
            if(mbuffer<=min):
                min=mbuffer
    for i in range(len(state1.shuju)):
        if(state1.biao[i]!=1):
            mbuffer=panduan_jisuan(state1,i)
            if(mbuffer==min):
                return i
            

def distance(state1):
    max=0.0
    mbuffer=0.0
    mubiao=dis_panduan(state1)
    #print(mubiao)
    a_youhua(state1,mubiao)









#######################################################
class state:
    def __init__(self,X,Y,Label,C,O):
        self.shuju=[[X[i],Y[i]] for i in range(len(X))]
        self.label = Label
        self.xiangliang=np.empty([len(X),3,1])
        self.biao=[0 for i in range(100000)]#用来标记是否是S_t中的coreVec
        self.b=0
        self.C=C
        self.alpha=[0.0 for i in range(len(X))]
        self.O=100
        self.xin = [0.0 for i in range(3)]
        self.R=0
        self.w=np.empty([1,2])
        self.S_t=[]
        #self.K=[[0.0 for i in range(len(self.shuju))] for i in range(len(self.shuju))]
        #self.K_yingshe(self)

    '''def K_yingshe(self):
        for i in range(len(self.shuju)):
            for j in range(len(self.shuju)):
                self.K[i][j]=K(self.shuju[i],self.shuju[j],0)
                print(i*100000+j)'''


def initialize(state1):#初始化C和R都做好了
    x1=int(rd.uniform(0,100000))
    x2=int(rd.uniform(0,100000))
    while(x1==x2):
        x2 = int(rd.uniform(0, 100000))
    state1.xin[0]=1/2*(state1.label[x1]*np.array(state1.shuju[x1])+state1.label[x2]*np.array(state1.shuju[x2]))
    state1.xin[1]=1/2*(state1.label[x1]+state1.label[x2])
    ei_x1=np.zeros([1,len(state1.shuju)])
    state1.biao[x1]=1
    state1.alpha[x1]=1/2
    state1.S_t.append(x1)
    ei_x2=np.zeros([1,len(state1.shuju)])
    state1.biao[x2]=1
    state1.alpha[x2]=1/2
    state1.S_t.append(x2)
    ei_x1[0][x1]=1
    ei_x2[0][x2]=1
    state1.xin[2]=1/2*(ei_x1+ei_x2)
    state1.R=3.66-P_jisuan(state1)#常熟K算的3.66
    #C_1=np.mat(C[1])
    C_2=np.mat(state1.xin[2])
    b_gengxin(state1)
    w_gengxin(state1)


state1=state(X,Y,Label,0.6,0)
initialize(state1)

distance(state1)

#print(state1.xin)
#print(state1.b)
#print(state1.w)
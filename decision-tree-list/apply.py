import data_read
import huiguishu
import cartbuild
headp=cartbuild.headp
X=[]
X=huiguishu.ceshi.copy()
yuansu=0
cut=0.0
y_=[0.0 for i in range(101)]
y=[0.0 for i in range(101)]
x=X[0]
loss=0.0
for k in range(101):
    x=X[k]
    p = headp
    while(p.left!=None and p.right!=None and p.exist==1):
        yuansu=p.yuansu
        cut=p.cut
        if(x[yuansu]<+cut):
            p=p.left
        else:
            p=p.right
    y_[k]=p.pinjun
    y[k]=x[0]
    loss=loss+(y[k]-y_[k])**2
print(y)
print(y_)
print(loss)


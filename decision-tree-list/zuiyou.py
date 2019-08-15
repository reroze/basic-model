def findmax(a,yuansu):
    b=0.0
    for i in range(len(a)):
        if(a[i][yuansu]>b):
            b=a[i][yuansu]
    return b


def findmin(a,yuansu):
    b=1.0
    for i in range(len(a)):
        if(a[i][yuansu]<b):
            b=a[i][yuansu]
    return b


def jisuan(a,yuansu,cut):
    c1_num=0
    c2_num=0
    c1=0.0
    c2=0.0
    loss=0.0
    for i in range(len(a)):
        if(a[i][yuansu]<=cut):
            c1_num=c1_num+1
            c1=c1+a[i][0]
        else:
            c2_num=c2_num+1
            c2=c2+a[i][0]
    if(c1_num==0):
        c1=0.0
    else:
        c1=c1/c1_num
    if(c2_num==0):
        c2=0.0
    else:
        c2=c2/c2_num
    for i in range(len(a)):
        if(a[i][yuansu]<=cut):
            loss=loss+(a[i][0]-c1)**2
        else:
            loss=loss+(a[i][0]-c2)**2
    return c1,c2,loss,c1_num,c2_num


def guijiindex(guiji,yuansu):
    b=0
    for i in range(len(guiji)):
        if(guiji[i]==yuansu):
            b=1
            return b
    return b


def yuansuzuiyou(node):
    #print("normal")正常运行
    a=node.shujuyu
    zongtizuiyou=100.0
    thiszuiyou=[100.0 for i in range(1,14)]
    c1=[[0.0 for i in range(10)] for i in range(1,14)]
    c2=[[0.0 for i in range(10)] for i in range(1,14)]
    c1_zuiyou=[0.0 for i in range(1,14)]
    c2_zuiyou=[0.0 for i in range(1,14)]
    c1_num=[[0 for i in range(10)] for i in range(1,14)]
    c1_num_best=[0 for i in range(1,14)]
    c2_num=[[0 for i in range(10)] for i in range(1,14)]
    c2_num_best=[0 for i in range(1,14)]
    loss_now=[[0.0 for i in range(10)] for i in range(1,14)]
    thiszuiyou_cut=[0.0 for i in range(1,14)]
    thiszuiyounum=[0 for i in range(1,14)]
    all_num=len(a)
    #print("normal",all_num)
    if (node.forward != None):
        for i in range(1,14):
           if(guijiindex(node.guiji,i)==0):
                max=findmax(a,i)
                min=findmin(a,i)
                cut=min+1.0*(max-min)/20
                time=0
                while(time<10):
                    c1[i-1][time],c2[i-1][time],loss_now[i-1][time],c1_num[i-1][time],c2_num[i-1][time]=jisuan(a,i,cut)
                    if(loss_now[i-1][time]<thiszuiyou[i-1]):
                        thiszuiyou[i-1]=loss_now[i-1][time]
                    cut=cut+1.0*(max-min)/11
                    time=time+1
                for j in range(10):
                    if(loss_now[i-1][j]==thiszuiyou[i-1]):
                        thiszuiyounum[i-1]=j
                        thiszuiyou_cut[i-1]=min+1.0*(max-min)/20+j*(max-min)/11
                        c1_zuiyou[i-1]=c1[i-1][j]
                        c1_num_best[i-1]=c1_num[i-1][j]
                        c2_zuiyou[i-1]=c2[i-1][j]
                        c2_num_best[i-1]=c2_num[i-1][j]

        for i in range(1, 14):
            if(guijiindex(node.guiji,i)==0):
                if (thiszuiyou[i - 1] < zongtizuiyou and ((c1_num_best[i - 1] / (all_num + 1)) > 0.05 and (
                        c1_num_best[i - 1] / (all_num + 1)) < 0.95)):
                    zongtizuiyou=thiszuiyou[i - 1]
        for i in range(1, 14):
            if (guijiindex(node.guiji, i) == 0):
                if (thiszuiyou[i - 1] == zongtizuiyou):
                    #print("normal?:",i,thiszuiyou_cut[i-1])
                    return i, thiszuiyou_cut[i - 1]  # ,c1_zuiyou[i-1],c2_zuiyou[i-1]

    else:
        for i in range(1,14):
            max=findmax(a,i)
            min=findmin(a,i)
            cut=min+1.0*(max-min)/20
            time=0
            while(time<10):
                c1[i-1][time],c2[i-1][time],loss_now[i-1][time],c1_num[i-1][time],c2_num[i-1][time]=jisuan(a,i,cut)
                if(loss_now[i-1][time]<thiszuiyou[i-1]):
                    thiszuiyou[i-1]=loss_now[i-1][time]
                cut=cut+1.0*(max-min)/11
                time=time+1
            for j in range(10):
                if(loss_now[i-1][j]==thiszuiyou[i-1]):
                    thiszuiyounum[i-1]=j
                    thiszuiyou_cut[i-1]=min+1.0*(max-min)/20+j*(max-min)/11
                    c1_zuiyou[i-1]=c1[i-1][j]
                    c1_num_best[i-1]=c1_num[i-1][j]
                    c2_zuiyou[i-1]=c2[i-1][j]
                    c2_num_best[i-1]=c2_num[i-1][j]
    #print(a)
        #print("normal")
        for i in range(1,14):
            if(thiszuiyou[i-1]<zongtizuiyou and ((c1_num_best[i-1]/(all_num+1))>0.05 and (c1_num_best[i-1]/(all_num+1))<0.95)):
                zongtizuiyou=thiszuiyou[i-i]
        for i in range(1,14):
            if(thiszuiyou[i-1]==zongtizuiyou):
                print(i,thiszuiyou[i-1])
                return i,thiszuiyou_cut[i-1]#,c1_zuiyou[i-1],c2_zuiyou[i-1]


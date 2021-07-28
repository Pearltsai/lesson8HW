a=[]
A=[]
cc=[]
ap=int(input('有幾個蘋果?'))
m=int(input('一個多少錢?'))
a.append(ap)
i=0
sell = 1

while i<1:
    print('_'*20)
    print('請選擇功能')
    c=['a)進貨','b)出貨','c)顯示營業額','d)顯示庫存','e)離開']
    j=0
    while j<5:
        print(c[j])
        j=j+1
    x=(input('輸入字母'))
    
    if x=="a":
        l=int(input('加幾顆蘋果?'))
        a.append(l)
        print('現在有',sum(a),'顆蘋果')
    elif x=="b":
        
        g=int(input('賣出幾顆蘋果?'))
        ap=int(ap)-int(g)
        v=('賣出',g,'顆')
        a.append(ap)
        r=g*m
        A.append(r)
        print('賺了',r,'元')
        cc.append(sell)
        cc.append(v)
        sell = sell +1
    elif x=="c":
        print(cc)
        print('共有',sell-1,'筆交易')
        print('賺了' ,sum(A),'元')
        
    elif x=="d":
        print('有',sum(a),'顆')
    elif x=="e":
        i=i+1

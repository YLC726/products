products = []
#讀取既有檔案
with open ('products.csv','r',encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line
            continue
        name,price = line.strip().split(',')#去除換行符號(/n) #用逗點切割字串定義為name,price
        products.append([name,price])
print(products)
#讓使用者輸入
while True:
    name = input('名稱,輸入完請按q:')
    if name == 'q':
    	break
    price = input('價格:')
    products.append([name , price])
print(products)
#印出購買紀錄
for p in products:
	print(p)

for p in products:
	print(p[0], '的價格是', p[1])
#寫入檔案
with open ('products.csv','w',encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')#名稱,價錢 (換行)
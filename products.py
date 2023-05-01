products = []
while True:
    name = input('名稱,輸入完請按q:')
    if name == 'q':
    	break
    price = input('價格:')
    products.append([name , price])
print(products)


for p in products:
	print(p)

for p in products:
	print(p[0], '的價格是', p[1])
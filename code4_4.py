is_awake=True
count=0
while is_awake==True:
    count +=1
    print(f'羊が{count}匹・・・')
    key=input('もうねむりそうですか？(y/n)>>')
    if key=='y':
        is_awake=False
print('おやすみなさい（　＾ω＾）・・・')
count=1
is_eat=True
print('カレーを召し上がれ')
while is_eat==True:
    print(f'{count}皿のカレーをたべました。')
    key=input('おかわりはいかがでしょうか。？(y/n)>>')
    if key=='y':
        count +=1
        
    else :
        is_eat=False
print('ごちそうさまでした。')

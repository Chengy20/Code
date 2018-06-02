x = int(input())
z = int(input())

ah = 0
bet = str(x)
for i in range(z+1):
    ah += int(bet)
    bet += '0'
print(ah)

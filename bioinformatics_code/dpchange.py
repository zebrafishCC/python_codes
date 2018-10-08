
def DPChange(money, Coins):
	MinNumCoins = []
	MinNumCoins.append(0)
	for m in range(1,money+1):
		MinNumCoins.append(100000)
		for coin in Coins:
			if m >= coin:
				if MinNumCoins[m-coin]+1 < MinNumCoins[m]:  
					MinNumCoins[m] = MinNumCoins[m-coin] + 1
	return MinNumCoins[money]

money = 19259
Coins = [24,22,5,3,1]

print DPChange(money,Coins)
	
'''
def DPchange(money, coins):
	lastNumCoins = {}
	for coin in coins:
'''		

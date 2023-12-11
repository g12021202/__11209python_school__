import random
PlayerDices = [random.randint(1,6) for x in range(4)]
firstTime = PlayerDices[0]
secondTime = PlayerDices[1]
thirdTime = PlayerDices[2]
fourthTime = PlayerDices[3]
print(f"第1次: {firstTime} , 第2次: {secondTime} , 第3次: {thirdTime} , 第4次: {fourthTime}")
PlayerDices.sort()
print(f"點數由小到大為: {PlayerDices[0]} ,  {PlayerDices[1]} ,  {PlayerDices[2]} ,  {PlayerDices[3]}")
if PlayerDices[0] == PlayerDices[1] == PlayerDices[2] == PlayerDices[3] == 6:
    print("豹子")
elif PlayerDices[0] == PlayerDices[1] == PlayerDices[2] == PlayerDices[3]:
    print("一色")
elif PlayerDices[0] == PlayerDices[1] != PlayerDices[2] != PlayerDices[3] or PlayerDices[0] == PlayerDices[1] != PlayerDices[2] == PlayerDices[3]:
    result = PlayerDices[2] + PlayerDices[3]
    print(f"點數: {result}") 
elif PlayerDices[0] != PlayerDices[1] == PlayerDices[2] != PlayerDices[3] :
    result = PlayerDices[1] + PlayerDices[3]
    print(f"點數: {result}") 
elif PlayerDices[0] != PlayerDices[1] != PlayerDices[2] == PlayerDices[3]:
    result = PlayerDices[0] + PlayerDices[1]
    print(f"點數: {result}") 
elif PlayerDices[0] == PlayerDices[1] == PlayerDices[2] or PlayerDices[1] == PlayerDices[2] == PlayerDices[3]:
    print("3個相同的數字，作廢")
elif PlayerDices[0] != PlayerDices[1] != PlayerDices[2] != PlayerDices[3]:
    print("4個數都不同，作廢")




# BossDices = [random.randint(1,6) for x in range(4)]
# BossDices.sort()
# if BossDices[0] == BossDices[1] == BossDices[2] == BossDices[3]:
#     pass
# else:
#     pass
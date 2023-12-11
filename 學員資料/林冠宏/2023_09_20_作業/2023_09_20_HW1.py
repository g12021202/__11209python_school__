import pyinputplus as pyip
height = pyip.inputInt("請輸入身高,單位為(公分):")
weight = pyip.inputInt("請輸入體重,單位為(公斤):")

BMI = weight / ((height/100)**2)
print(f"您的BMI是{BMI}")
if BMI < 18.5:
    print("您的體重太輕")
elif BMI <= 25:
    print("您的體重正常")
elif BMI <= 30:
    print("您的體重過重")
else:
    print("您的體重肥胖")
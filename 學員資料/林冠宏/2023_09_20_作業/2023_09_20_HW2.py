sbp = int(input("請輸入收縮壓"))
dbp = int(input("請輸入舒張壓"))

if sbp < 120 and dbp < 80 :
    print("正常")
elif 120 <= sbp <= 129 and dbp < 80 :
    print("血壓升高")
elif 130 <= sbp <= 139 and 80 <= dbp <= 89 :
    print("高血壓第一期")
elif sbp >= 140 and dbp >= 89 :
    print("高血壓第二期")
elif sbp >= 130 and dbp < 80 :
    print("單純收縮期高血壓")
else:
    print("不存在")
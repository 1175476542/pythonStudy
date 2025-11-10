brand_list = ["神州","宏碁","联想","机械革命","华硕天选","联想拯救者"]
brand_name = input("请输入需要查找的品牌：")
if brand_name in brand_list:
    print(f'{brand_name}位于第{brand_list.index(brand_name)+1}位')
else:
    print("您输入的品牌不存在")
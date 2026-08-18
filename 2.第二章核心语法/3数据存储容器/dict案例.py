# 购物车系统shopping_menu = { xx:{ },xx:{}... }
shopping_cart = {}
menu = """
###########购物车系统##########
#        1.添加购物车         #
#        2.修改购物车         #
#        3.删除购物车         #
#        4.查询购物车         #
#        5.退出购物车         #
#############################
"""

print("欢迎使用购物车系统")
while True:
    print(menu)
    choice = input("请输入要执行的操作(1-5):")
    match choice:
        case "1":

            shopping_names = input("请输入商品名称:")


            if shopping_names in shopping_cart:
                print("商品已存在,请重新选择")
            else:
                shopping_pieces = float(input("请输入商品价格:"))
                shopping_num = int(input("请输入商品数量:"))
                shopping_cart[shopping_names] = {"price": shopping_pieces, "num": shopping_num}
                print("商品添加完毕")

        case "2":
            shopping_names = input("请输入修改的商品名称:")


            if shopping_names not in shopping_cart:
                print("商品不存在,请重新选择")
            else:
                shopping_pieces = float(input("请输入商品最新的价格:"))
                shopping_num = int(input("请输入商品最新的数量:"))
                shopping_cart[shopping_names] = {"price": shopping_pieces, "num": shopping_num}
                print("商品修改完毕")
        case "3":
            shopping_names = input("请输入删除的商品名称:")

            if shopping_names not in shopping_cart:
                print("商品不存在,请重新选择")
            else:
                del shopping_cart[shopping_names]
                print("商品删除完毕")
        case "4":

            for shopping_names in shopping_cart.keys():
                shopping_information = shopping_cart[shopping_names]

                print(
                    f"商品名称:{shopping_names},商品价格:{shopping_information["price"]},商品数量:{shopping_information["num"]}")
        case "5":
            print("886~")
            break
        case _:
            print("操作错误,不支持!!!")


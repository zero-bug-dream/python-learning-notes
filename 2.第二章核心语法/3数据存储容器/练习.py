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
            good_names = input("请输入商品名称:")
            if good_names in shopping_cart:
                print("商品已存在,请重新选择")

            else:
                good_prices = float(input("请输入商品价格:"))
                good_num = int(input("请输入商品数量:"))
                shopping_cart[good_names] = {"price": good_prices, "num": good_num}
        case "2":
            good_names = input("请输入商品名称:")

            if good_names not in shopping_cart:
                print("商品不存在,请重新选择")

            else:
                good_prices = input("请输入商品价格:")
                good_num = input("请输入商品数量:")
                shopping_cart[good_names] = {"price": good_prices, "num": good_num}
        case "3":
            good_names = input("请输入要删除商品名称:")

            if good_names not in shopping_cart:
                print("商品不存在,请重新选择")
            else:
                del shopping_cart[good_names]
        case "4":
            for good_names in shopping_cart.keys():
                good_infor = shopping_cart[good_names]
                print(f"商品名称:{good_names},商品价格:{good_infor["price"]},商品数量:{good_infor["num"]}")

        case "5":
            print("886~")
            break
        case _:
            print("操作错误,不支持!!!")
"""
案例2:定义一个用于根据传入的一批商品信息(商品名,价格,数量),优惠(优惠券,积分折扣),运费信息计算订单价格函数
规则如下:
    1:优惠劵需要商品金额满5000才能使用,且优惠金额不能大于商品总价
    2:积分折扣需要商品金额满5000才可以使用,100抵1元(且折扣金额不能大于商品总价,积分只能整百抵扣)
"""
# 先义一个函数
def calc_goods_date(*args,yhj = 0,jfzk = 0,yf = 0):# 后面代码要缩进!!!
    """
    根据传入的一批商品信息(商品名,价格,数量),优惠(优惠券,积分折扣),运费信息计算订单价格函数
    :param args: 商品信息(商品名,价格,数量)
    :param yhj: 优惠券
    :param jfzk: 积分折扣
    :param yf: 运费
    :return: 订单总金额
    """


# 1:计算商品总金额,一批商品信息可以用列表
    total_price = (goods[1] * goods[2] for goods in args)
    total_cost = sum(total_price)

# 2;扣减优惠劵
    if total_cost >= 5000 and yhj <= total_cost:
        total_cost -= yhj

# 3:扣减积分
    if total_cost >= 5000 and jfzk //100 <= total_cost:
         total_cost -= jfzk //100

# 4:添加运费
    total_cost += yf

    return total_cost# 少返回会输出none

total = calc_goods_date(("鼠标",99,3),("小丑",9999,1),("游戏皮肤",168,2),yhj = 12,jfzk = 400,yf = 9.9)
print(total)
"""
案例2:定义一个用于根据传入的一批商品信息(商品名,价格,数量),优惠(优惠券,积分折扣),运费信息计算订单价格函数
规则如下:
    1:优惠劵需要商品金额满5000才能使用,且优惠金额不能大于商品总价
    2:积分折扣需要商品金额满5000才可以使用,100抵1元(且折扣金额不能大于商品总价,积分只能整百抵扣)
"""
# 定义一个函数
def calc_product_cost(*args: tuple[str,float,int],coupon: float = 0,score: int = 0,express: float = 0.0 )->float:
    """
    用于根据传入的一批商品信息(商品名,价格,数量),优惠(优惠券,积分折扣),运费信息计算订单价格函数
    :param args: 商品信息
    :param coupon: 优惠劵
    :param score: 积分折扣
    :param express: 运费
    :return: 订单总金额
    """
# 1商品原价args
    total_price =(product[1] * product[2] for product in args)
    total_cost = sum(total_price)
# 2优惠后金额coupon
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -=  coupon
# 3积分折扣后金额score
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -=  score // 100
# 4运费express
    total_cost += express

    return total_cost

total = calc_product_cost(("mate60",6999,2),("键盘",199,2),coupon=20,score=500,express=9.9)
print(total)


# python 中用于明确标识变量函数参数的数据类型 a:数据类型 = 数据
a = 123
a1: int =123

score = 12.3
score1: float = 12.3

hobby = "python"
hobby1: str = "python"

flsg = True
flsg1: bool = True

pic = None
pic1: None = None

names = ["A","B","C","D"]
names1: list[str | int] = ["A","B","C","D"]
names1.append(323)
print(names1)


phones = {"19707336172","13899757904"}
phones1: set[str] = {"19707336172","13899757904"}

options = {"counts":0,"total":1,"round":2}
options1: dict[str,int] = {"counts":0,"total":1,"round":2}

goods = ("键盘",299,2)
goods1: tuple[str,int,int] = ("键盘",299,2)
goods2 = ("鼠标",299,1)
print(goods1)

# 类型推断:当我们在对变量进行直接赋值,Python解释权会自动推断变量数据类型(光标放在names4会自动推断类型)只是提示作用
names4 = ["童家豪","何以","桃正"]


# 函数类型注解 形参: 数据类型
def circle_area_len(r: float) \
        -> tuple[float, float]:
    return round(3.14 * r * r,2),round(2 * 3.14 * r ,2)
al = circle_area_len(3)
print(al)

def calc_data(score: list[int]) ->tuple[int,int,float]:
    max_v = max(score)
    min_v = min(score)
    avg_v = round(sum(score) / len(score),1)
    return max_v, min_v, avg_v
a4 = calc_data([121,213,123,31,4,123.21])
print(a4)
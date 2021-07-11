from typing import List, Dict

Vector = List[str]  # 类型提示的别名


def scale(scalar: float, vector: Vector, dic: Dict[str, int]) -> Vector:
    for item in vector:
        print(item.replace("", ""))  # 在有类型提示的情况下直接使用.符号ide可以知道该类型。
    print(scalar, vector, dic)
    return ["10", "20", "30"]


new_vector = scale(2.0, ["10", "20", "30"], {"a": 10})







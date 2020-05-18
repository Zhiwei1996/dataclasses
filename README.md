PEP 557， `dataclasses` 在 Python 2.7 上移植实现

> !!! 只是初步移植，未跑完测试用例

[English](./README-en.rst)

原项目地址: https://github.com/ericvsmith/dataclasses

官方文档: https://docs.python.org/3/library/dataclasses.html

[PEP 557 -- Data Classes](https://www.python.org/dev/peps/pep-0557/)

数据类相关文章推荐阅读：
- [Data classes](https://typeclasses.com/python/data-classes) - Type Classes
- [Python 工匠：做一个精通规则的玩家](https://www.zlovezl.cn/articles/a-good-player-know-the-rules/)

### 使用示例

原模块

```python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

item = InventoryItem('hammers', 10.49, 12)
print(item.total_cost())
```

移植后
```python
from dataclasses import dataclass

@dataclass
class InventoryItem(object):
    """Class for keeping track of an item in inventory."""
    __annotations__ = {'quantity_on_hand': int, 'name': str, 'unit_price': float}
    quantity_on_hand = 0

    def total_cost(self):
        return self.unit_price * self.quantity_on_hand

item = InventoryItem(name='hammers', unit_price=10.49, quantity_on_hand=12)
# 或者传入字典解包初始化
# data = {'name': 'hammers', 'unit_price': 10.49, 'quantity_on_hand': 12}
# item = InventoryItem(**data)
print(item.total_cost())
``` 

Tips:
- Python 2 中不支持类型注解特性，类没有`__annotations__` 属性，需要通过自定义添加 `__annotations__` 
- 由于自定义的 `__annotations__`  为无序字典，须以关键字显式传参，确保传参顺序正确
- `dataclasses.make_dataclass` 暂不可用
- 由于 python 2 类的 `__doc__` 属性不可写，暂时移除 `class doc-string`


引用模块:
- [dictproxyhack](https://github.com/eevee/dictproxyhack)


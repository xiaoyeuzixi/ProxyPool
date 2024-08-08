import pkgutil
import importlib
import inspect
from .base import BaseTester

# 存储所有 BaseTester 的子类
classes = []

# 遍历当前包中的所有模块
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    if is_pkg:
        continue  # 忽略包，只处理模块

    # 动态加载模块
    module = importlib.import_module(f'.{name}', package=__name__)

    # 遍历模块中的所有成员
    for name, value in inspect.getmembers(module):
        if inspect.isclass(value) and issubclass(value, BaseTester) and value is not BaseTester:
            # 如果是 BaseTester 的子类且不被忽略，添加到 classes 列表
            if not getattr(value, 'ignore', False):
                classes.append(value)

# 设置 __all__ 以公开所有的 BaseTester 子类
__all__ = classes

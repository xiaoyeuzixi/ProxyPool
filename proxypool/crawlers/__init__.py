import pkgutil
import importlib
import inspect
from .base import BaseCrawler

# 存储所有 BaseCrawler 的子类
classes = []

# 遍历当前包中的所有模块
for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    if is_pkg:
        continue  # 忽略包，只处理模块

    # 动态加载模块
    module = importlib.import_module(f'.{name}', package=__name__)

    # 遍历模块中的所有成员
    for name, value in inspect.getmembers(module):
        if inspect.isclass(value) and issubclass(value, BaseCrawler) and value is not BaseCrawler:
            # 如果是 BaseCrawler 的子类且不被忽略，添加到 classes 列表
            if not getattr(value, 'ignore', False):
                classes.append(value)

# 设置 __all__ 以公开所有的 BaseCrawler 子类
__all__ = classes

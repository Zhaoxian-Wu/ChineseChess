# alpha-beta剪枝项目
人工智能课程设计：使用alpha-beta剪枝算法实现中国象棋AI

# 特点
- 使用python在后台进行Alpha-Beta剪枝计算
- 实现中不涉及任何浏览器特性，所以不存在浏览器兼容性问题.
- 代码结构极其简洁明了，你可以轻易的阅读，修改成自己版本.

# AI行为
- 使用Hash记录已计算的格局，减少重复计算
- 剪枝：当某一方被将军时，只有应将的着法才会被继续搜索

# 运行环境
Linux ubuntu 18.04  
python3.6

# 安装依赖
pip install flask

# 运行
```bash
$ python server.py
```
在浏览器访问地址：localhost:8080

# 代码引用
[itlwei/chess](https://github.com/itlwei/chess)：移植了UI界面
[axios/axios](https://github.com/axios/axios)：异步请求组件
# Snake AI

<img src="https://github.com/Ackeraa/snake/blob/master/snake.gif" style="zoom:10%;" />

使用遗传算法和简单神经网络实现贪吃蛇，其中
* 遗传算法进化神经网络的参数
* 神经网络预测移动方向

## 遗传算法
* 交叉算子：单点交叉
* 变异算子：高斯变异
* 选择算子：轮盘赌选择

## 神经网络
* 网络结构：[32, 10, 4]
* 隐含层激活函数：Relu
* 输出层激活函数：Sigmoid
* 输入层包括：
  * 蛇首方向：[0, 1, 0, 0]
  * 蛇尾方向：[1, 0, 0, 0]
  * 蛇首八个方向上
    * 是否有食物
    * 是否有自身
    * 与边缘的距离
* 输出层表示四个移动方向


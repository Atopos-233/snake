# Snake🐍
🎈*Just do some magic things in summer vacation, due to its dull time*🎈
## Todo List🎏
*1.Rewritte a bit of mini-games（snake， Tetris）*

*2.Add deeeplearning(CNN, GAN,...)*

*3.Train models to complete games*

*4.Using trained model to challenge WeChat Games*

# NLP基本公式

查准率

$$Precision(\%) = \frac{True positive}{(True positive+False positive)} \times 100$$


查全率

$$Recall(\%) = \frac{True positive}{(True positive+False negative)} \times 100$$


F1-score

$$F1-Score = \frac{2}{\frac{1}{p}+\frac{1}{r}}$$



错误率

$$Error = \frac{1}{m_{dev}}\sum_{i=1}^{m_{dev}}L\{{\hat y^{(i)} \neq y^{(i)}}\}$$



惩罚值

$$w^{i}=\begin{cases}

1 & \text{ if } x^{i}\ \text{is non-pornographic} \\

100 & \text{ if } x^{i}\ \text{is pornographic}

\end{cases}$$



softmax

$$softmax(x)_i = \frac {e^{x_i}}{\sum _j e^{x_j}}$$



softmax property

$$softmax(x) = softmax(x + c)$$


$$softmax(x+c)_i = \frac {e^{(x_i+c)}}{\sum _j e^{(x_j+c)}} = \frac {e^{c}e^{x_i}}{e^{c}\sum _j e^{x_j}} = \frac {e^{x_i}}{\sum _j e^{x_j}} = softmax(x)$$


sigmoid

$$\sigma(x) = \frac{1}{1+e^{-x}}$$



gradient of sigmoid

$$σ′(x) = σ(x)(1 − σ(x))$$




softmax for word2vec:

$$softmax(u_o^Tv_c) = p(o|c) = \hat y_o = \frac {e^{u_o^Tv_c}}{\sum _{w=1}^W e^{u_w^Tv_c}}$$



cross-entropy cost

$$CE(y,\hat y) = − \sum_i y_ilog(\hat y_i)$$


$$J_t(\theta) =log \sigma(u_o^Tv_c)$$



gradient of CE with regard to theta

$$\frac{\partial CE(y,\hat y)}{\partial \theta}$$


overall objeective function by negtive sample:

$$J(\theta) = \frac{1}{T}\sum _{t=1}^TJ_t(\theta)$$


negtive sample cost:

$$J_t(\theta) =log \sigma(u_o^Tv_c)+\sum_{i=1}{k}\mathbb{E}_{j~P(w)}[log\sigma(-u_j^Tv_c)]$$

$$J_t(\theta) =-log \sigma(u_o^Tv_c)-\sum_{k=1}^{K}log\sigma(-u_k^Tv_c)$$


negtive sample derivative

$$\frac {\partial J}{\partial v_c} = (\sigma(u_o^Tv_c)-1)u_o-\sum _{k=1}^K(\sigma (-u_k^Tv_c)-1)u_k$$

$$\frac {\partial J}{\partial u_o} = (\sigma(u_o^Tv_c)-1)v_c$$

$$\frac {\partial J}{\partial u_k} = -(\sigma(-u_k^Tv_c)-1)v_c, for all k = 1,2,\dots,K$$


gradient of 

$$\frac {\partial J}{\partial v_c} = U(\hat y - y)$$



gradient of

$$\frac {\partial J}{\partial U} = v_c(\hat y - y)^T$$

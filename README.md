# jupyterlab-jbturtle
Simple turtle module for JupyterLab

## JBTurtle
* This module uses **Pillow**
* Attention: Almost impractical with FireFox because of FOUC. **Do not use with FireFox.**

## PyPI Project
* https://pypi.org/project/jbturtle/

## Install
```
pip install Pillow
pip install jbturtle
``` 
## Sample
```
from jbturtle import *

turtle = JBTurtle(640, 400)
nn = 0
for count in range(100):
  turtle.line_hsv(nn, 1, 1)
  turtle.forward(100)
  turtle.turn_right(85)
  nn += 5
```
## Functions
* JBTurtle(xs, ys)
  * Constructor
  * xs: x-size of workspace
  * ys: y-size of workspace
* init(xs, ys)
  * Initialization
  * xs: x-size of workspace
  * ys: y-size of workspace
* forward(dst)
* turn_right(angle)
* turn_left(angle)
* move(x, y)
* pen_up()
  * default state
* pen_down()       
* pen_speed(spd)
  * default is 2
* pen_width(lw)
  * default is 2
* pen_color((r, g, b))
  * default is (0, 0, 0) or #000000
* pen_rgb(r, g, b)
* pen_hsv(h, s, v)

## Acknowledgments
This system was created inspired by

"JupyterLab によるPython 学習のはじめかた", 
新村 正明, 小林 一樹, 小形 真平

電子情報通信学会 通信ソサイエティマガジン 2022 年 15 巻 4 号 p. 333-338

https://www.jstage.jst.go.jp/article/bplus/15/4/15_333/_article/-char/ja/

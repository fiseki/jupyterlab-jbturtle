# jupyterlab-jbturtle
Simple Turtle module for JupyterLab

## Install
```
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
## Function
* JBTurtle(xs, ys)
  * Constructor
  * xs: x-size of workspace
  * ys: y-size of workspace
* init(xs, ys)
  * Initialization
  * xs: x-size of workspace
  * ys: y-size of workspace
*

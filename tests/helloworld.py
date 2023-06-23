import sys 

sys.path.append('../tapp')
from tapp import *

app = tapp().start()
app.onkey('q',app.stop)
Text('hello world',app)

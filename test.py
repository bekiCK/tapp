from tapp import *

app = tapp().start()
app.onkey('q',app.stop)

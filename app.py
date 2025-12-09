
from flask import Flask

<<<<<<< HEAD
=======

>>>>>>> dev-hello-world-app
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

<<<<<<< HEAD
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
def my_function():
    # This is a local variable
    local_variable = "I am local to my_function"
    print(local_variable)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
#one line comment
# one more comment
# one more comment added
>>>>>>> dev-hello-world-app

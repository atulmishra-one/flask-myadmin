# Flask MyAdmin
A Flask Based MySQL Web Management Extension

### Installation

```bash
git clone https://github.com/atulmishra-one/flask-myadmin
cd flask-myadmin
python setup.py install
```


#### registering

in your app

```python
from flask import Flask
from flask_myadmin import FlaskMyAdmin

app = Flask(__name__)


# Initialize the extension
flask_myadmin = FlaskMyAdmin(host="localhost")
flask_myadmin.init_app(app)

go to : http://localhost:5000/flask-myadmin

```
# Hind Vadodara (Gujarati)

Create python virtual environment (Python 2.7)

Note: *Older hindkit version is used here*
```
virtualenv v2.7-env --python=python2.7
source v2.7-env/bin/activate
pip install -r requirements2.7.txt
```

*OR*

Create python virtual environment (Python 3.7)

Note: *Latest hindkit library code used*
```
python3.7 -m venv v-env
source v-env/bin/activate
pip install -r requirements3.7.txt
```

Core library used [hindkit](https://github.com/itfoundry/hindkit).

Inside virtual environment run
```
python build.py # For python 3.7
python build-p27.py $ For python 2.7
```


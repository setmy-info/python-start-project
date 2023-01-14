export PYTHONPATH=${pwd}
python -m unittest discover -s ./ -p *_test.py

# commands and stuff
## unit tests
### basic usage
```bash
python3 -m unittest -v path/to/your/test/file/:3
```
### examples
Suppose we are in the `neetcode/python` directory. 

If we want to run tests for, say, `validate_bst.py`, we write:
```bash
python3 -m unittest -v test/trees/validate_bst_test.py
```

To just run *all* the tests for the python code, we write:
```bash
python3 -m unittest -v test/*/*.py
```

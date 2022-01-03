# python_template


## Install library:

```
pip install -e src/
```

## Run pytests:

To run the tests, make sure that the lib is installed first:
```
pip install -e src/
python -m pytest tests/ -v
```

## Run black:

```
python -m black --check .
```

## Run mypy:

```
python -m mypy src/
```



## CodeBuild:

Log:
```
[Container] 2022/01/03 21:30:49 Waiting for agent ping
[Container] 2022/01/03 21:30:50 Waiting for DOWNLOAD_SOURCE
[Container] 2022/01/03 21:30:51 Phase is DOWNLOAD_SOURCE
[Container] 2022/01/03 21:30:51 CODEBUILD_SRC_DIR=/codebuild/output/src390121250/src/github.com/saidvandeklundert/python_template
[Container] 2022/01/03 21:30:51 YAML location is /codebuild/output/src390121250/src/github.com/saidvandeklundert/python_template/buildspec.yml
[Container] 2022/01/03 21:30:51 No commands found for phase name: install
[Container] 2022/01/03 21:30:51 Processing environment variables
[Container] 2022/01/03 21:30:51 Selecting 'python' runtime version '3.9' based on manual selections...
[Container] 2022/01/03 21:30:51 Running command echo "Installing Python version 3.9 ..."
Installing Python version 3.9 ...

[Container] 2022/01/03 21:30:51 Running command pyenv global  $PYTHON_39_VERSION

[Container] 2022/01/03 21:30:54 Moving to directory /codebuild/output/src390121250/src/github.com/saidvandeklundert/python_template
[Container] 2022/01/03 21:30:54 Configuring ssm agent with target id: codebuild:194ed1a7-14c6-48e8-bd1a-bce0501764f7
[Container] 2022/01/03 21:30:54 Successfully updated ssm agent configuration
[Container] 2022/01/03 21:30:54 Registering with agent
[Container] 2022/01/03 21:30:54 Phases found in YAML: 4
[Container] 2022/01/03 21:30:54  PRE_BUILD: 9 commands
[Container] 2022/01/03 21:30:54  BUILD: 2 commands
[Container] 2022/01/03 21:30:54  POST_BUILD: 1 commands
[Container] 2022/01/03 21:30:54  INSTALL: 0 commands
[Container] 2022/01/03 21:30:54 Phase complete: DOWNLOAD_SOURCE State: SUCCEEDED
[Container] 2022/01/03 21:30:54 Phase context status code:  Message: 
[Container] 2022/01/03 21:30:54 Entering phase INSTALL
[Container] 2022/01/03 21:30:54 Phase complete: INSTALL State: SUCCEEDED
[Container] 2022/01/03 21:30:54 Phase context status code:  Message: 
[Container] 2022/01/03 21:30:54 Entering phase PRE_BUILD
[Container] 2022/01/03 21:30:54 Running command uname -a
Linux ef07f158a66a 4.14.252-195.483.amzn2.x86_64 #1 SMP Mon Nov 1 20:58:46 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

[Container] 2022/01/03 21:30:54 Running command pip install -r requirements.txt
Collecting pytest==6.2.4
  Downloading pytest-6.2.4-py3-none-any.whl (280 kB)
Collecting mypy==0.910
  Downloading mypy-0.910-cp39-cp39-manylinux2010_x86_64.whl (23.2 MB)
Collecting black
  Downloading black-21.12b0-py3-none-any.whl (156 kB)
Collecting packaging
  Downloading packaging-21.3-py3-none-any.whl (40 kB)
Collecting iniconfig
  Downloading iniconfig-1.1.1-py2.py3-none-any.whl (5.0 kB)
Collecting toml
  Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
Requirement already satisfied: attrs>=19.2.0 in /root/.pyenv/versions/3.9.5/lib/python3.9/site-packages (from pytest==6.2.4->-r requirements.txt (line 1)) (21.2.0)
Collecting pluggy<1.0.0a1,>=0.12
  Downloading pluggy-0.13.1-py2.py3-none-any.whl (18 kB)
Collecting py>=1.8.2
  Downloading py-1.11.0-py2.py3-none-any.whl (98 kB)
Collecting mypy-extensions<0.5.0,>=0.4.3
  Downloading mypy_extensions-0.4.3-py2.py3-none-any.whl (4.5 kB)
Collecting typing-extensions>=3.7.4
  Downloading typing_extensions-4.0.1-py3-none-any.whl (22 kB)
Requirement already satisfied: click>=7.1.2 in /root/.pyenv/versions/3.9.5/lib/python3.9/site-packages (from black->-r requirements.txt (line 3)) (7.1.2)
Collecting pathspec<1,>=0.9.0
  Downloading pathspec-0.9.0-py2.py3-none-any.whl (31 kB)
Collecting tomli<2.0.0,>=0.2.6
  Downloading tomli-1.2.3-py3-none-any.whl (12 kB)
Requirement already satisfied: platformdirs>=2 in /root/.pyenv/versions/3.9.5/lib/python3.9/site-packages (from black->-r requirements.txt (line 3)) (2.4.0)
Collecting pyparsing!=3.0.5,>=2.0.2
  Downloading pyparsing-3.0.6-py3-none-any.whl (97 kB)
Installing collected packages: pyparsing, typing-extensions, tomli, toml, py, pluggy, pathspec, packaging, mypy-extensions, iniconfig, pytest, mypy, black
Successfully installed black-21.12b0 iniconfig-1.1.1 mypy-0.910 mypy-extensions-0.4.3 packaging-21.3 pathspec-0.9.0 pluggy-0.13.1 py-1.11.0 pyparsing-3.0.6 pytest-6.2.4 toml-0.10.2 tomli-1.2.3 typing-extensions-4.0.1
WARNING: Running pip as root will break packages and permissions. You should install packages reliably by using venv: https://pip.pypa.io/warnings/venv
WARNING: You are using pip version 21.1.2; however, version 21.3.1 is available.
You should consider upgrading via the '/root/.pyenv/versions/3.9.5/bin/python3.9 -m pip install --upgrade pip' command.

[Container] 2022/01/03 21:31:04 Running command pwd
/codebuild/output/src390121250/src/github.com/saidvandeklundert/python_template

[Container] 2022/01/03 21:31:04 Running command ls -ltr
total 24
-rw-r--r-- 1 root root   31 Jan  3 21:30 requirements.txt
-rw-r--r-- 1 root root  524 Jan  3 21:30 mypy.ini
-rw-r--r-- 1 root root 1045 Jan  3 21:30 buildspec.yml
-rw-r--r-- 1 root root  295 Jan  3 21:30 README.md
drwxr-xr-x 2 root root 4096 Jan  3 21:30 tests
drwxr-xr-x 3 root root 4096 Jan  3 21:30 src

[Container] 2022/01/03 21:31:04 Running command ls -ltr  tests/
total 8
-rw-r--r-- 1 root root 300 Jan  3 21:30 test_example.py
-rw-r--r-- 1 root root  75 Jan  3 21:30 pytest.ini

[Container] 2022/01/03 21:31:04 Running command pip install -e src/
Obtaining file:///codebuild/output/src390121250/src/github.com/saidvandeklundert/python_template/src
Installing collected packages: example
  Running setup.py develop for example
Successfully installed example-0.1
WARNING: Running pip as root will break packages and permissions. You should install packages reliably by using venv: https://pip.pypa.io/warnings/venv
WARNING: You are using pip version 21.1.2; however, version 21.3.1 is available.
You should consider upgrading via the '/root/.pyenv/versions/3.9.5/bin/python3.9 -m pip install --upgrade pip' command.

[Container] 2022/01/03 21:31:05 Running command python -m pytest tests/ -v
============================= test session starts ==============================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.11.0, pluggy-0.13.1 -- /root/.pyenv/versions/3.9.5/bin/python
cachedir: .pytest_cache
rootdir: /codebuild/output/src390121250/src/github.com/saidvandeklundert/python_template/tests, configfile: pytest.ini
collecting ... collected 3 items

tests/test_example.py::test_something PASSED                             [ 33%]
tests/test_example.py::test_human PASSED                                 [ 66%]
tests/test_example.py::test_beast PASSED                                 [100%]

============================== 3 passed in 0.01s ===============================

[Container] 2022/01/03 21:31:05 Running command python -m mypy src/
Success: no issues found in 4 source files

[Container] 2022/01/03 21:31:07 Running command python -m black --check .
All done! ✨ 🍰 ✨
5 files would be left unchanged.

[Container] 2022/01/03 21:31:07 Phase complete: PRE_BUILD State: SUCCEEDED
[Container] 2022/01/03 21:31:07 Phase context status code:  Message: 
[Container] 2022/01/03 21:31:07 Entering phase BUILD
[Container] 2022/01/03 21:31:07 Running command echo "we are in the build block"
we are in the build block

[Container] 2022/01/03 21:31:07 Running command echo "we will run some tests"
we will run some tests

[Container] 2022/01/03 21:31:07 Phase complete: BUILD State: SUCCEEDED
[Container] 2022/01/03 21:31:07 Phase context status code:  Message: 
[Container] 2022/01/03 21:31:07 Entering phase POST_BUILD
[Container] 2022/01/03 21:31:07 Running command echo "we are in the post build phase"
we are in the post build phase

[Container] 2022/01/03 21:31:07 Phase complete: POST_BUILD State: SUCCEEDED
[Container] 2022/01/03 21:31:07 Phase context status code:  Message: 
```
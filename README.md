# Introduction
Goal is to deploy a simple ML workload (object detection) and scale it using kubernetes
# Getting started with development 
## installation 
```
# make new venv
python -m venv E:\venvs\ml-kubernetes
# activate venv
E:\venvs\ml-kubernetes\Scripts\activate.bat
```
## running in dev
```
uvicorn server:app --reload
```

## runnning tests
```
pytest
```

# Notes
## dependencies
- fastapi
- "uvicorn[standard]"  # server
- httpx # http client for testing
- pytest # test framework
- pytest-asyncio # for async functions

## dev dependencies
- flake8 # code linting
- black # code formatting 

## useful commands
```
pip freeze > api\requirements.txt

```

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
cd api && uvicorn server:app --reload
```

## runnning tests
```
cd api && pytest
```

# Notes
## dependencies
- fastapi
- "uvicorn[standard]"  # server
- httpx # http client for testing
- pytest # test framework
- pytest-asyncio # for async functions
- opencv # for yolo
- requests # for downloading model

## dev dependencies
- flake8 # code linting
- black # code formatting 

## useful commands
```
cd api && pip freeze > requirements.txt

```

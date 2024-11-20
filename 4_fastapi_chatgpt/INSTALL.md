### Virtual Environment  (Python 3.10.9)
    python3 -m venv myenv
    source myenv/bin/activate
    pip install fastapi uvicorn openai
    deactivate (optional)

### Run
    uvicorn app.main:app --reload

### Test
    http://127.0.0.1:8000/docs

### requirements.txt
    pip freeze > requirements.txt

### Run container

docker build -t fastapi-app .
docker run -d -p 8000:8000 fastapi-app
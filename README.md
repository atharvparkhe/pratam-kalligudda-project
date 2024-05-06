## Pratam ka project

A simple FastAPI Server that accets an audio file via "/upload/" route, reprocesses it and returns a score for the audio file.


### 💻 Run Locally

***Step#1 : Clone Project Repository***

```bash
git clone https://github.com/atharvparkhe/pratam-kalligudda-project.git && cd pratam-kalligudda-project
```

***Step#2 : Create Virtual Environment***

* If *virtualenv* is not istalled :
```bash
pip install virtualenv && virtualenv env
```
* **In Windows :**
```bash
env/Scripts/activate
```
* **In Linux or MacOS :**
```bash
source env/bin/activate
```

***Step#3 : Install Dependencies***

```bash
pip install --upgrade pip -r requirements.txt
```

***Step#4 : Run Server***

```bash
fastapi dev main.py
```

- Open `http://127.0.0.1:8000/` or `http://localhost:8000/` on your browser.

*Check the terminal if any error.*


### 🔗 Endpoints

- **`/upload/`** - Upload an audio file with name "file" through form-data.


from fastapi import FastAPI
import joblib

model = joblib.load("best_model.joblib")
app = FastAPI()


# define a root `/` endpoint
@app.get("/")
def homepage():
    return "welcome"

# define a root `/` endpoint


@app.get("/hello")
def hello():
    return "hello"

# define a root `/` endpoint
@app.get("/quote")
def index():
    return {"quote": "Hey life is beautiful"}

# define a root `/` endpoint


@app.get("/predict")
def index(day, time):

    y_pred = model.predict([[int(day), int(time)]])[0]
    print(y_pred)

    return {"prediction": float(y_pred)}

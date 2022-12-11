import pickle
import numpy as np
__model=None
def load_artifacts():
    print("Loading saved artifacts")
    global __model
    with open("./artifacts/Annadata.pickle","rb") as f:
        __model=pickle.load(f)
    print("Artifacts loaded")

def suggest(N,P,K,temp,humi,ph,rainfall):
    load_artifacts()
    data=np.array([[N,P,K,temp,humi,ph,rainfall]])
    return __model.predict(data)[0]





if __name__=="__main__":
    load_artifacts()
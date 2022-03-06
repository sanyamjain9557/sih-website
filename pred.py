import pickle
#from sklearn import model_selection
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
model=pickle.load(open("SVM_trained_model","rb"))
data=pd.read_csv("Train.csv")
data.drop(["Unnamed: 0"],inplace=True,axis=1)
d=data.head(1)
def prediction(speed,rot,course):
    d["speed"]=speed
    d["course"]=course
    d["rot"]=rot
    
    return model.predict(d)
a=prediction(51.2,292,10)
if(a==1):
    print("YES, There is Risk")
else:
    print("NO")
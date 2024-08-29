import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
print("Started clas.....")

rf_class=load_model=pickle.load(open("Thyrostream_clas.sav","rb"))

input_data=(0,1,0,0,1,1,54,1,1,0,0)
input_data2=np.array(input_data)
input_data3=input_data2.reshape(1,-1)
# reg_prediction=rf_reg.predict(input_data3)
class_prediction=rf_class.predict(input_data3)
print("/n",class_prediction)
if class_prediction[0]==0:
    print("It can be cured")
else:print("it cant be cured")
# print(f"the chances of curing it is : {reg_prediction}%")


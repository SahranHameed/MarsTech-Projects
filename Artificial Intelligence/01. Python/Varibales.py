import pickle
loaded_model = pickle.load(open("finalized_model_linear.sav",'rb'))
result = loaded_model.predict([[850]])
result

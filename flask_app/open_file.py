import pickle

file_path='threat_model.pkl'

with open(file_path,'rb') as file:
    data=pickle.load(file)

print ("Type of data loaded:",type(data))
print("\nPreview:\n",data)    
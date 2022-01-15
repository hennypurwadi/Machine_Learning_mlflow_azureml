
def trigger_train(): 
   
    import sklearn
    from sklearn.metrics import confusion_matrix
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report,accuracy_score
    from sklearn.ensemble import IsolationForest
    import joblib
    import datetime
    import requests
    import warnings
    warnings.filterwarnings('ignore')
       
    filedf = 'fraud_detector.csv'
    df= pd.read_csv(filedf)
    X = df.drop("Category",axis=1)
    y = df.Category
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3,random_state=40)

    model= IsolationForest(n_estimators=100, max_samples=len(X_train),random_state=0, verbose=0)   
    model.fit(X_train,y_train)
    #model = joblib.load(open("model.pkl", 'rb'))
   
    ypred= model.predict(X_test)
    ypred[ypred == 1] = 0 #normal
    ypred[ypred == -1] = 1 #possibly fraud 
    
    #Freeze Model with joblib
    filename_pkl = 'model.pkl'
    joblib.dump(model, open(filename_pkl, 'wb'))
    print("model.pkl saved")
    
#Automate scheduled training    
#mlflow.autolog({"run_id":"749eb2eaf2a84e1992110481c7a7a7a9"})  
trigger_train()

import schedule
schedule.every(720).hours.do(trigger_train)

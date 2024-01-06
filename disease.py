#separate file for code understanding

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
    
def learner(bloodPressure,cholestrol,bmi,smoker,heartDisease,physicalActivity,alcohol,generalHealth,mentalHealth,physicalHealth,diffWalking,gender,age,education,fruit,veggies):                                                                                                   
    file = pd.read_csv('diabetes_01.csv')
    featured=['HighBP','HighChol','BMI','Smoker','HeartDiseaseorAttack','PhysActivity','HvyAlcoholConsump','GenHlth','MentHlth','PhysHlth','DiffWalk','Sex','Age','Education','Fruits','Veggies']
    x=file[featured]
    y=file.Diabetes
    x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7)

    model=LogisticRegression(max_iter=253000)

    model.fit(x_train.values,y_train)
    y_predict=model.predict([[int(bloodPressure),int(cholestrol),int(bmi),int(smoker),int(heartDisease),int(physicalActivity),int(alcohol),int(generalHealth),int(mentalHealth),int(physicalHealth),int(diffWalking),int(gender),int(age),int(education),int(fruit),int(veggies)]])
    # y_predict=model.predict([[1,1,40,1,0,0,0,5,18,15,1,0,9,4,0,1]])  #sample input
    return(y_predict)

    # # print(model.score(x_test,y_test))
    



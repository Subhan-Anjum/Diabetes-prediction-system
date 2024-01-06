from flask import Flask, render_template, request
app = Flask(__name__, template_folder="templates")
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def ageConvertor(age):
    if age>=18 and age<=24:
        age=1
    elif age>=25 and age<=29:
        age=2
    elif age>=30 and age<=34:
        age=3
    elif age>=35 and age<=39:
        age=4
    elif age>=40 and age<=44:
        age=5
    elif age>=45 and age<=49:
        age=6
    elif age>=50 and age<=54:
        age=7
    elif age>=55 and age<=59:
        age=8
    elif age>=60 and age<=64:
        age=9
    elif age>=65 and age<=69:
        age=10
    elif age>=70 and age<=74:
        age=11
    elif age>=75 and age<=79:
        age=12
    elif age>=80:
        age=13
    return age

@app.route("/")
def hello():
    return render_template("base.html")

@app.route("/checkPatient")
def addProd():
    return render_template("base.html")

@app.route("/", methods=['POST','GET'])
def patientData():
    file = pd.read_csv('diabetes_01.csv')
    featured=['HighBP','HighChol','BMI','Smoker','HeartDiseaseorAttack','PhysActivity','HvyAlcoholConsump','GenHlth','MentHlth','PhysHlth','DiffWalk','Sex','Age','Education','Fruits','Veggies']
    x=file[featured]
    y=file.Diabetes
    x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7)
    model=LogisticRegression(max_iter=253000)
    model.fit(x_train.values,y_train)

    data = request.form
    name = data['name']
    age=data['age']
    gender=data['gender']
    bmi=data['bmi']
    cholestrol=data['chol']
    heartDisease=data['heart']
    smoker=data['smoker']
    physicalActivity=data['pactivity']
    alcohol=data['alcohol']
    generalHealth=data['ghealth']
    mentalHealth=data['mhealth']
    physicalHealth=data['phealth']
    diffWalking=data['walking']
    education=data['education']
    fruit=data['fruit']
    bloodPressure=data['bloodpressure'] 
    veggies=data['veggies']
    
    age=int(age)
    initial=int(age)
    
    (prediction)=str(model.predict([[int(bloodPressure),int(cholestrol),int(bmi),int(smoker),int(heartDisease),int(physicalActivity),int(alcohol),int(generalHealth),int(mentalHealth),int(physicalHealth),int(diffWalking),int(gender),int(age),int(education),int(fruit),int(veggies)]]))

    if prediction=='[0]':
        prediction="Non-Diabetic"
        health_tips='Avoid smoking,Do physical activity for 30 minutes daily,Drink water,Eat food with fibre'
    else:
        prediction="Diabetic"
        health_tips='Quit smoking and alcohol,Eat less salt,Avoid red and processed meat,Eat more fruits & vegetables,Cut down sugar, Be physically active'
        
    if prediction=="Non-Diabetic":
        statement="Based on current parameters, you might get diabetes by age of "

        for i in range(4,60,4):
            age=int(age)+i
            ageConverted=ageConvertor(age)
            ageConverted=str(ageConverted)
            
            bmi=int(bmi)
            bmi+=2
            bmi=str(bmi)
                       
            physicalHealth=int(physicalHealth)
            if physicalHealth>=20:
                physicalHealth-=1
            physicalHealth=str(physicalHealth)
            if i==10:   
                bloodPressure=int(bloodPressure)
                bloodPressure==1
                bloodPressure=str(bloodPressure)
                
                generalHealth=int(generalHealth)
                if generalHealth>=2:
                    generalHealth-=1
                generalHealth=str(generalHealth)
                
                diffWalking=int(diffWalking)
                diffWalking==1
                diffWalking=str(diffWalking)
                
            cholestrol=int(cholestrol)
            cholestrol=1
            cholestrol=str(cholestrol)
                
            if i==20:
                heartDisease=int(heartDisease)
                heartDisease==1
                heartDisease=str(heartDisease)
                
                physicalActivity=int(physicalActivity)
                physicalActivity==0
                physicalActivity=str(physicalActivity)
                
                mentalHealth=int(mentalHealth)
                if mentalHealth>=20:
                    mentalHealth-=1
                    
                mentalHealth=str(mentalHealth)
                
            future=str(model.predict([[int(bloodPressure),int(cholestrol),int(bmi),int(smoker),int(heartDisease),int(physicalActivity),int(alcohol),int(generalHealth),int(mentalHealth),int(physicalHealth),int(diffWalking),int(gender),int(ageConverted),int(education),int(fruit),int(veggies)]]))
            if future=='[1]':
                newAge=initial+i
                break
            else:
                newAge="90"
        return render_template("result.html",name=name,prediction=prediction,statement=statement,newAge=newAge,health_tips=health_tips)
    return render_template("result.html",name=name,prediction=prediction,health_tips=health_tips)


if __name__=="__main__":
    app.run(debug=True)
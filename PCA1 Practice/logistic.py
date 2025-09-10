from sklearn.datasets import load_iris 

# loading the iris dataset 
iris = load_iris()

# extracting the data & target part 
data = iris.data
target = iris.target

x = data 
y = target 

print(data)
print(target)

# now split the data into training and testing set
from sklearn.model_selection import train_test_split 
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# loading logistic regression 
from sklearn.linear_model import LogisticRegression 
log_reg = LogisticRegression()

# fit the training data
log_reg.fit(x_train,y_train)

# predict the output 
y_pred = log_reg.predict(x_test)
print(y_pred) 

# calculating confusion matrix,accuracy score,classification report
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report 
print(confusion_matrix(y_test,y_pred))
print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))


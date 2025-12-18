import math 

# function to calculate sigmoid function value 
def sigmoid(z):
    return (1/(1+math.exp(-z)))

# function to calculate loss function value 
def loss_function(sigma,yg):
    res = -((yg*math.log(sigma)) + ((1-yg)*math.log(1-sigma)))
    return res

with open("F:\\Machine Learning Lab - 5th sem\\PCA1 Practice\\review.txt",'r') as file:
    data = file.read()
    data = data.lower()
    print(data)
    words = data.split()
    print(words)

    pos_words = ["good","best","awesome","outstanding","fantastic","marvelous","nice","enjoyable","amazing","beautiful","great"]
    neg_words = ["hokey","2nd-grade","bad","worst","worse","ugly","not","boring"]
    pronouns = ["i","me","you","she","he"]

    features = [0,0,0,0,0,0]
    
    for word in words:
        features[5] += 1
        if word in pos_words:
            features[0] += 1
        if word in neg_words:
            features[1] += 1 
        if word == 'no':
            features[2] += 1
        if word in pronouns:
            features[3] += 1
        if word == '!':
            features[4] += 1
    features[5] = math.log(features[5])
    print(features)

#given weights
weights = [2.5,-5.0,-1.2,0.5,2.0,0.7]
#given bias 
b = 0.1

# calculate (z = w*x + b) for all features 
z = 0
for i in range (len(features)):
    z += weights[i]*features[i]
z = z + b 
print(" The value of z = ",z)

# print the sigmoid function 
sigmoid_function = sigmoid(z)
print("The sigmoid function value = ",sigmoid_function)

if(sigmoid_function < 0.5):
    print("The review is negative")
elif(sigmoid_function > 0.5):
    print("The review is positive")
else:
    print("the review is neutral")

# loss function calculation
pos_loss = loss_function(sigmoid_function,1)
neg_loss = loss_function(sigmoid_function,0)

print("The posiotive loss = ",pos_loss)
print("The negative loss =",neg_loss)
import math 

def sigmoid(z):
    return (1/(1+math.exp(-z)))

def loss_function(sigma,y):
    res = -((y*math.log(sigma)) + ((1-y)*math.log(1-sigma)))
    return res 

with open("F:\\Machine Learning Lab - 5th sem\\PCA1 Practice\\review.txt","r")as file:
    data = file.read()
    data = data.lower()
    print(data)
    words = data.split()
    print(words)

    pos_words = ["good","nice","awesome","outstanding","best","beautiful","enjoyable","well","amazing","great","fantastic","marvelous"]
    neg_words = ["bad","hokey","2nd-grade","worse","worst","ugly","boring"]
    pronouns = ["i","me","he","she","you","your","his","her","we","they","their"]

    features = [0,0,0,0,0,0]

    for word in words:
        features[5] += 1 # feature 6 will contain total no of words in the review
        if word in pos_words:
            features[0] += 1
        if word in neg_words:
            features[1] += 1
        if word == "no":
            features[2] += 1
        if word in pronouns:
            features[3] += 1 
        if word == "!":
            features[4] += 1
    features[5] = math.log(features[5])
    #print(features)
    print("Positive words :",features[0])
    print("Negative words :",features[1])
    print("Contains No:",features[2])
    print("Pronouns :",features[3])
    print("Contains ! :",features[4])
    print("logarithm of total no of words :",features[5])

# given weights 
w = [2.5,-5.0,-1.2,0.5,2.0,0.7]
# given bias 
b = 0.1 
# calculate z=(w*x)+b for all feature values x 
z = 0
for i in range(len(features)):
    z += w[i]*features[i]
z=z+b 
print("The value of z = ",z)
# print the value of sigmoid(z)
sigmoid_function = sigmoid(z)
print("The value of sigmoid function = ",sigmoid_function)
# decision rules 
if sigmoid_function<0.5:
    print("The review is negative.")
else:
    print("The review is positive.")
# Loss function calculation 
positive_loss = loss_function(sigmoid_function,1)
negative_loss = loss_function(sigmoid_function,0)

print("Positive loss = ",positive_loss)
print("Negative loss = ",negative_loss)



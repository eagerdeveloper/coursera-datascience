trainData <- read.csv("../train.csv")

head(trainData)

#Titanic Survival Story

plot(trainData$survived, trainData$age, 
     pch=19,col="blue",ylab="Survivors",xlab="Age")

logTrain <- glm(trainData$survived ~ trainData$age,family="binomial")
summary(logTrain)

confint(logTrain)


testData <- read.csv("../test.csv")


plot(as.factor(testData$survived), logTrain$fitted, 
     pch=19,col="blue",ylab="Survivors",xlab="Age")






##
## SVM
##
library(e1071)
formula3 <- as.factor(survived) ~ pclass + sex + age
tune <- tune.svm(formula3, data=trainData, gamma=10^(-4:-1), cost=10^(1:4))
# summary(tune)
tune$best.parameters

titanic.svm <- svm(formula3, 
                   data=titanic.train, 
                   type="C-classification", 
                   kernel="radial", 
                   probability=T, 
                   gamma=tune$best.parameters$gamma, 
                   cost=tune$best.parameters$cost)
ps$svm <- as.numeric(predict(titanic.svm, newdata=titanic.test))-1
tb <- table(titanic.test$survived, ps$svm)
# tb
results$svm <- (tb[1,1]+tb[2,2])/sum(tb)
results$svm

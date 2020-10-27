from sklearn.tree import DecisionTreeClassifier

creditScoreAndIncomeTrain = [
[700,80000],
[800,50000],
[550,40000],
[570,70000],
[500,75000]
]

approvedTrain = [
["Yes"],
["Yes"],
["No"],
["No"],
["No"]
]

creditScoreAndIncomeTest = [
[840,90000],
[450,40000]
]

approvedTest = [
"Yes",
"No"
]

tree = DecisionTreeClassifier().fit(creditScoreAndIncomeTrain, approvedTrain)

print(tree.predict(creditScoreAndIncomeTest))
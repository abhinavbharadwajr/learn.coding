userInput = list(map(str, input().split()))

principle = float(userInput[0])
interest = float(userInput[1])
time = float(userInput[2])

simpleinterest = (principle * interest * time) / 100

print(round(simpleinterest, 2))
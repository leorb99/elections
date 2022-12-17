import pandas as pd

data = pd.read_csv("data.csv", encoding="iso-8859-1")

print("Parties")
print(data["_Candidate__party"].value_counts(normalize=True)*100)

print("\nMarital Status")
print(data["_Candidate__marital_status"].value_counts(normalize=True)*100)

print("\nSchooling")
print(data["_Candidate__schooling"].value_counts(normalize=True)*100)

print("\nStates")
print(data["_Candidate__state"].value_counts(normalize=True)*100)

print("\nStatus")
print(data["_Candidate__status"].value_counts(normalize=True)*100)

print("\nGenders")
print(data["_Person__gender"].value_counts(normalize=True)*100)

print("\nColors")
print(data["_Person__color"].value_counts(normalize=True)*100)

print("\nProfession") 
print(data["_Candidate__profession"].value_counts(normalize=True)*100)

print("\nReelection") 
p = data["_Candidate__reelected"].value_counts(normalize=True)
print(p*100) # expected True=3.084995
print(0.03084995*9530)

print(0.5731*513) # 294 reeleitos - resultado real
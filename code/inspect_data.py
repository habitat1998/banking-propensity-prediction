import pandas as pd
import matplotlib.pyplot as plt

#  y = has the client subscribed a term deposit? (binary: "yes","no")
file = r"data/bank-full.csv"
df = pd.read_csv(file, header=0, sep=";")
target_distribution = df["y"].value_counts()
keys = target_distribution.keys()
print(target_distribution)
plt.bar(keys, target_distribution, color="blue")
plt.title("Class Distribution")
plt.xlabel("Answer")
plt.ylabel("Frequency")
plt.show()

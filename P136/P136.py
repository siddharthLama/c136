import pandas as pd

df =pd.read_csv("filteredStars.csv")
df.head()

df.drop(["Unnamed: 0"], axis=1, inplace=True)

name = df["Star_name"].tolist()
mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
distance = df["Distance"].tolist()
gravity = df["Gravity"].tolist()

final_star_list = []

temp_dict = {}
for i in range(len(name)):
    temp_dict["name"] = name[i]
    temp_dict["mass"] = mass[i]
    temp_dict["radius"] = radius[i]
    temp_dict["distance"] = distance[i]
    temp_dict["gravity"] = gravity[i]
    final_star_list.append(temp_dict)
    temp_dict = {}

print(final_star_list)


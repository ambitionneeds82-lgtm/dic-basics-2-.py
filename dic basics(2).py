import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = {
    "Code": ["00","01","02","03","04","05","06","07"],
    "Access_to_basic_amenities": [
        "None of these", "Cooking facilities", "Tap water that is safe to drink",
        "Kitchen sink", "Refrigerator", "Bath or shower", "Toilet", "Electricity supply"
    ],
    "Occupied_private_dwellings": [5979,1512414,1481133,1513830,1481430,1514472,1515042,1503675]
}

df = pd.DataFrame(data)

total = 1529901  # from your data
df["Percentage"] = (df["Occupied_private_dwellings"] / total * 100).round(2)

print(df)

# Plot
plt.figure(figsize=(10,5))
plt.barh(df["Access_to_basic_amenities"], df["Percentage"])
plt.xlabel("Percentage of Dwellings (%)")
plt.ylabel("Basic Amenity")
plt.title("Access to Basic Amenities in Occupied Private Dwellings")
plt.show()

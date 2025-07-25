import pandas as pd

df = pd.DataFrame(columns=["Name", "Kalorien (kcal)","Protein (g)","Kohlenhydrate (g)", "Fett (g)"])
df.loc[0] = ["Mehl", 348, 10, 72.3, 1]
df.loc[1] = ["Zucker", 405, 0, 99.8, 0]
df.loc[2] = ["Kakao", 389, 23.3, 10, 21.9]
df.loc[3] = ["Eier", 156, 13, 1.1, 11.3]
df.loc[4] = ["Backpulver", 100, 0.1, 25, 0]
df.loc[5] = ["Milch", 38, 0.8, 4.1, 1.8]
df.loc[6] = ["Butter", 741, 0.7, 0.6, 83]
df.loc[7] = ["Schokochunks", 520, 6.3, 53.5, 29.4]
print(df)

multipliers = [1.3, 2.0, 0.6, 1.1, 0.04, 1.6, 1.6, 1]

print("\n")
naehrwerte = pd.DataFrame(columns=["Name", "Kalorien (kcal)","Protein (g)","Kohlenhydrate (g)", "Fett (g)"])

for i in range(8):
    naehrwerte.loc[i] = [df.iloc[i].iloc[0], df.iloc[i].iloc[1]*multipliers[i], df.iloc[i].iloc[2]*multipliers[i],
                         df.iloc[i].iloc[3]*multipliers[i], df.iloc[i].iloc[4]*multipliers[i]]

print(naehrwerte)

print("\n")
finalTable = pd.DataFrame(columns=["Name", "Kalorien (kcal)","Protein (g)","Kohlenhydrate (g)", "Fett (g)"])
finalTable.loc[0] = ["Muffin", naehrwerte["Kalorien (kcal)"].sum()/12, naehrwerte["Protein (g)"].sum()/12,
                     naehrwerte["Kohlenhydrate (g)"].sum()/12, naehrwerte["Fett (g)"].sum()/12]
print(finalTable)

# Mehl zucker kakao eier backpulver vanillearoma milch butter chunks


print(f"\033[93m>Analyse läuft...")
print(f"\033[93m>")
print(f"\033[93m>")
print(f"\033[93m>Analyse erfolgreich. Probleme festgestellt:")
print(f"\033[93m>Team ist unzufrieden")
print(f"\033[93m>Überbelastung im Team")
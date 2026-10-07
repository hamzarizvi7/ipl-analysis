import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("matches.csv")

# Drop the almost-empty column
df = df.drop(columns=["method"])

# Remove matches with no winner (no result / abandoned)
df = df.dropna(subset=["winner"])

# Fix team names that changed over the years
names = {
    "Royal Challengers Bengaluru": "Royal Challengers Bangalore",
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings",
    "Rising Pune Supergiants": "Rising Pune Supergiant",
}
for col in ["team1", "team2", "toss_winner", "winner"]:
    df[col] = df[col].replace(names)

print("Matches with a result:", len(df))

# Question 1: Which teams won the most matches?
wins = df["winner"].value_counts()
print(wins)

wins.plot(kind="barh", title="Total IPL Wins by Team", figsize=(9, 6))
plt.xlabel("Wins")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("wins_by_team.png")
plt.show()

# Question 2: Does winning the toss help win the match?
toss_win = (df["toss_winner"] == df["winner"]).mean() * 100
print("Toss winner also won the match:", round(toss_win, 1), "%")

# Question 3: Do teams prefer to bat or field after winning the toss?
print(df["toss_decision"].value_counts())

# Question 4: Top 10 run scorers (uses deliveries.csv)
deliveries = pd.read_csv("deliveries.csv")
top_batters = (
    deliveries.groupby("batter")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_batters)

top_batters.plot(kind="barh", title="Top 10 IPL Run Scorers", figsize=(9, 6))
plt.xlabel("Runs")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_run_scorers.png")
plt.show()
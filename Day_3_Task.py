import pandas as pd

# Load the CSV directly from GitHub
url = "https://raw.githubusercontent.com/Nido09/Movies_dataset/main/Day%202%20Task.csv.csv"
df = pd.read_csv(url)

# Display basic statistics for numeric columns
summary_stats = df.describe()
print(summary_stats)

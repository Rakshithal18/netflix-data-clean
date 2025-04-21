from IPython.display import display
from tabulate import tabulate
import seaborn as sns
import pprint
import warnings
import pandas as pd

warnings.filterwarnings("ignore")

# ----------------------------
# 📥 Load the CSV directly
# ----------------------------
df = pd.read_csv(r"C:\internship\netflix_titles.csv.zip")


# ----------------------------
# 🧹 Data Cleaning
# ----------------------------

# 1. Clean column names
print("📌 Original Columns:\n", df.columns.tolist())
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("✅ Cleaned Columns:\n", df.columns.tolist())

# 2. Handle missing values
print("🕳️ Null values before filling:\n", df.isnull().sum())

df['country'].fillna("Unknown", inplace=True)
df['director'].fillna("Not Specified", inplace=True)
df['cast'].fillna("Not Specified", inplace=True)
df['rating'].fillna(df['rating'].mode()[0], inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'].fillna(pd.to_datetime("2000-01-01"), inplace=True)
df['duration'].fillna("0", inplace=True)

# 3. Drop remaining rows with nulls (if any)
df.dropna(inplace=True)

# 4. Remove duplicates
df.drop_duplicates(inplace=True)

# 5. Standardize text fields
df['type'] = df['type'].str.strip().str.lower()
df['title'] = df['title'].str.strip()
df['genre'] = df['listed_in'].str.lower().str.strip()

# ----------------------------
# 📊 Data Summary & Visuals
# ----------------------------

# Styled view
styled_df = df.style.set_caption("🎬 Netflix Titles Dataset 🎬") \
    .background_gradient(cmap='YlGnBu') \
    .set_properties({'text-align': 'center'}) \
    .set_table_styles([{
        'selector': 'th',
        'props': [('font-size', '14px'), ('background-color', '#f2f2f2')]
    }])

display(styled_df)

# Show final column names
print("📑 Final Columns:\n", df.columns.tolist())

# Fancy preview table
print(tabulate(df.head(), headers='keys', tablefmt='fancy_grid'))

# First row dictionary preview
print("\n📦 First Row (dict format):")
pprint.pprint(df.iloc[0].to_dict())

# Count plot for type (movie vs tv show)
sns.countplot(data=df, x='type')

# Show datatypes
print("\n📘 Data Types:\n", df.dtypes)

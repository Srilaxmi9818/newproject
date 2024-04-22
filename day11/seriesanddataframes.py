import pandas as pd


# 1. Create a Series and DataFrame:

# Create a Pandas Series from a list of favorite movies
movies = pd.Series(['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump'])

# Create a DataFrame with additional columns for 'Year Released' and 'Genre'
data = {'Movie': movies,
        'Year Released': [1994, 1972, 2008, 1994, 1994],
        'Genre': ['Drama', 'Crime', 'Action', 'Crime', 'Drama']}

df = pd.DataFrame(data)

print("Series of favorite movies:")
print(movies)
print("\nDataFrame with additional columns:")
print(df)

# 2. Basic DataFrame Operations:

# Add a new column to indicate if the movie is 'Classic'
current_year = pd.Timestamp.now().year
df['Is Classic'] = current_year - df['Year Released'] > 25

# Sort the DataFrame by the year released in descending order
df_sorted = df.sort_values(by='Year Released', ascending=False)

print("DataFrame with 'Is Classic' column:")
print(df)
print("\nDataFrame sorted by year released in descending order:")
print(df_sorted)


# 3. Data Selection

# Select only the movies that are classified as 'Classic'
classic_movies = df[df['Is Classic']]

# Select and print only the 'Genre' and 'Year Released' columns for all movies
selected_data = df[['Genre', 'Year Released']]

print("Classic Movies:")
print(classic_movies)
print("\nSelected Data (Genre and Year Released):")
print(selected_data)



# Select rows based on multiple conditions: 'Year Released' after 2000 and genre is not 'Action'
condition = (df['Year Released'] > 2000) & (df['Genre'] != 'Action')
filtered_rows = df[condition]

# Filter rows where genre is either 'Comedy' or 'Horror' using isin method
genre_filter = df['Genre'].isin(['Comedy', 'Horror'])
filtered_genre_rows = df[genre_filter]

print("Rows where 'Year Released' is after 2000 but genre is not 'Action':")
print(filtered_rows)

print("\nRows where genre is either 'Comedy' or 'Horror':")
print(filtered_genre_rows)  

# Group by 'Genre' and count the number of movies in each genre
movies_per_genre = df.groupby('Genre')['Movie'].count().reset_index()

print("Total number of movies per genre:")
print(movies_per_genre)
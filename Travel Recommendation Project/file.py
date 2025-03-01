import pandas as pd

# Load Dataset
df = pd.read_csv('India_travel.csv')  # Replace with the actual dataset filename

def calculate_rank(row):
    """A simple ranking algorithm combining ratings, popularity, and distance."""
    return row['Rating'] * 2 + row['Reviews'] * 1.5 - row['Distance']

def recommend_places(city_name):
    city_name = city_name.lower().strip()
    
    # Filter places near the given city (assuming 'City' column exists)
    nearby_places = df[df['City'].str.lower().str.contains(city_name, case=False)]

    if nearby_places.empty:
        print(f"No travel destinations found near '{city_name}'. Please try another city.")
        return

    # If the dataset has 'Distance' column, it's used directly; otherwise, add logic to calculate
    if 'Distance' not in df.columns:
        nearby_places['Distance'] = 50  # Default, you can add distance calculation logic here
    
    # Apply ranking logic
    nearby_places['RankScore'] = nearby_places.apply(calculate_rank, axis=1)

    # Sort by rank
    ranked_places = nearby_places.sort_values(by='RankScore', ascending=False)

    print(f"\nTop weekend travel destinations near {city_name.title()}:\n")
    for idx, row in ranked_places.head(5).iterrows():
        print(f"{row['Place Name']} - Rating: {row['Rating']} (Reviews: {row['Reviews']})")

if __name__ == '__main__':
    city = input("Enter your current city name: ")
    recommend_places(city)

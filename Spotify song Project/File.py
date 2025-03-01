import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load Dataset
df = pd.read_csv('Spotify_Songs.csv')  # Replace with actual dataset filename

# Combine useful columns into one text feature (adjust according to dataset)
df['combined_features'] = df['track_name'] + " " + df['artist_name'] + " " + df['lyrics'].fillna("")

# Vectorize text data
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['combined_features'])

# Nearest Neighbors Model
model = NearestNeighbors(n_neighbors=5, metric='cosine')
model.fit(X)

def find_song(snippet):
    query_vec = vectorizer.transform([snippet])
    distances, indices = model.kneighbors(query_vec)

    print("\nTop matching songs:")
    for i, idx in enumerate(indices[0]):
        row = df.iloc[idx]
        print(f"{i+1}. {row['track_name']} by {row['artist_name']} (Similarity: {1 - distances[0][i]:.2f})")

if __name__ == '__main__':
    while True:
        snippet = input("\nEnter a snippet of lyrics or description (or type 'exit' to quit): ").strip()
        if snippet.lower() == 'exit':
            break
        find_song(snippet)

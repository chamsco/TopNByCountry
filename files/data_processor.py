# Function to process the daily streams data and update the weekly streams counts for each country
def process_streams(daily_streams, weekly_counts):
    for stream in daily_streams:
        country = stream['country']
        sng_id = stream['sng_id']
        if country not in weekly_counts:
            weekly_counts[country] = {}
        weekly_counts[country][sng_id] = weekly_counts[country].get(
            sng_id, 0) + 1

# Function to get the top N songs for each country


def get_top_n_songs(weekly_counts, n=50):
    top_n_songs = {}
    for country, song_counts in weekly_counts.items():
        sorted_songs = sorted(song_counts.items(),
                              key=lambda x: x[1], reverse=True)
        top_n = sorted_songs[:n]
        top_n_songs[country] = top_n
    return top_n_songs

# Function to write the top N songs for each country to the output file
def write_top_n_songs_to_file(top_n_songs, output_file):
    with open(output_file, 'w') as file:
        for country, top_n in top_n_songs.items():
            if top_n:  # Only write non-empty countries
                top_n_str = ','.join(
                    [f'{sng_id}:{count}' for sng_id, count in top_n])
                file.write(f'{country}|{top_n_str}\n')

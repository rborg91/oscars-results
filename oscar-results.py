import pandas as pd
from imdb import Cinemagoer
import sqlite3
import time

# Improve data format for the full dataset and save it to a new CSV file
# Also new column called IMDBid which is essentially FilmId without tt at
# the beginning
oscars_results = pd.read_csv("input/full_data.csv", sep=None)
oscars_results = oscars_results.rename(columns={"FilmId": "IMDBid"})
oscars_results["IMDBid"] = oscars_results["IMDBid"].str.replace("tt", "")
# Place the IMDBid column at the beginning
oscars_results = oscars_results[["IMDBid"] + [col for col in oscars_results.columns if col != "IMDBid"]]
# Only keep the rows where category is Best Picture or its previous names
oscars_results = oscars_results[
    oscars_results["Category"].isin(["OUTSTANDING PICTURE",
                                     "OUTSTANDING PRODUCTION",
                                     "OUTSTANDING MOTION PICTURE",
                                     "BEST MOTION PICTURE",
                                     "BEST PICTURE"])
                                ]
# Save the new dataframe to a CSV file
oscars_results.to_csv("output/oscars_best_pictures.csv", index=False)

# Retrieve the information on the unique IMDB ids from oscar_results
# and write it to a new dataframe which will also be saved to a CSV file
imdb_ids = oscars_results["IMDBid"].unique()
ia = Cinemagoer()
imdb_data = []
for id in imdb_ids:
    try:
        movie = ia.get_movie(id)
        print(f"Retrieving data for IMDB ID: {id}")
        imdb_data.append({
            "IMDBid": id,
            "Title": movie["title"],
            "Year": movie["year"],
            "Genres": ", ".join(movie["genres"]),
            "Directors": ", ".join(
                                sorted(
                                    set(
                                        person['name']
                                        for person in movie.get("director", [])
                                        if person.get('name') and person.getID()
                                    )
                                )
                            ),
            "Rating": movie["rating"],
            "Runtime": movie["runtimes"][0],
            "Countries": ", ".join(movie["countries"]),
            "Languages": ", ".join(movie["languages"])
        })
    except Exception as e:
        print(f"Error retrieving data for IMDB ID: {id} - {e}")
        continue

    time.sleep(1)  # Sleep for 1 second to avoid hitting the API too hard

imdb_data = pd.DataFrame(imdb_data)
imdb_data.to_csv("output/imdb_data.csv", index=False)

# Create (or connect to) a SQLite database file
conn = sqlite3.connect('output/results.db')

# Write the data to tables in the SQLite database
oscars_results.to_sql('best_pictures', conn, if_exists='replace', index=False)
imdb_data.to_sql('imdb', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

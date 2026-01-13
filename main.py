import requests

TMDB_API_KEY = "789b5aae481f5d6911b1845871166668"

def get_movie(title):
    url = (
        "https://api.themoviedb.org/3/search/movie"
        f"?query={title}&api_key={TMDB_API_KEY}"
    )
    response = requests.get(url)
    data = response.json()

    # Common TMDB error responses
    if "success" in data and data["success"] is False:
        raise ValueError(
            "TMDB API request failed.\n"
            "This usually means your API key is missing or invalid.\n\n"
            "What to check:\n"
            "- Did you paste your TMDB API key into TMDB_API_KEY?\n"
            "- Is the key inside quotation marks?\n"
            "- Did you save the file before running it?\n\n"
            f"TMDB message: {data.get('status_message', 'Unknown error')}"
        )
    if "results" not in data:
        raise ValueError(
            "TMDB did not return movie search results.\n"
            "This may mean your API key is incorrect or the request failed.\n\n"
            f"TMDB response: {data}"
        )

    if len(data["results"]) == 0:
        raise ValueError(
            "TMDB returned zero results for this movie title.\n"
            "Try a different title or check your API key."
        )

    return data["results"][0]

if __name__ == "__main__":
    movie = get_movie("Inception")
    print(movie)
    print(movie["title"])

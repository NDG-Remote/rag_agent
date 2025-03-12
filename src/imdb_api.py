import os
import json
from dotenv import load_dotenv
import http.client
import urllib.parse

load_dotenv()

rapid_api_key = os.getenv("RAPID_API_KEY")

conn = http.client.HTTPSConnection("imdb236.p.rapidapi.com")

headers = {
    'x-rapidapi-key': rapid_api_key,
    'x-rapidapi-host': "imdb236.p.rapidapi.com"
}

def get_imdb_api_data(query: str) -> dict:
    encoded_query = urllib.parse.quote(query)
    conn.request("GET", f"/imdb/autocomplete?query={encoded_query}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

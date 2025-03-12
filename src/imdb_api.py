import os
import logging
import json
from dotenv import load_dotenv
import http.client
import urllib.parse
from gui import updating_chat_display, root

load_dotenv()

rapid_api_key = os.getenv("RAPID_API_KEY")

conn = http.client.HTTPSConnection("imdb236.p.rapidapi.com")

headers = {
    'x-rapidapi-key': rapid_api_key,
    'x-rapidapi-host': "imdb236.p.rapidapi.com"
}

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)

def get_imdb_api_data(query: str) -> dict:
    try:
        encoded_query = urllib.parse.quote(query)
        conn.request("GET", f"/imdb/autocomplete?query={encoded_query}", headers=headers)
        res = conn.getresponse()
        data = res.read()

        if res.status == 200:
            updating_chat_display("Result: Data fetched from IMDB API", "result_message")
            root.update()
            return json.loads(data.decode("utf-8"))
        else:
            response = f"Failed to fetch data from IMDb API. Status code: {res.status}"
            logger.error(response)
            updating_chat_display(response, "error_message")
            root.update()
            return {}
    except Exception as e:
        response = f"An error occurred while fetching data from the IMDb API: {str(e)}"
        logger.error(response)
        updating_chat_display(response, "error_message")
        root.update()
        return {}

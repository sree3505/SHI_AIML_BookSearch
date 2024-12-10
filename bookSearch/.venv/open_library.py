import  requests

class search_api:
    def __init__(self):
        self.apiurl = "https://openlibrary.org/search.json"

    def call_bookapi(self, title, limit):
        params = {
            "title": title,
            "limit": limit
        }
        #call Open Search API get the search results
        response = requests.get(self.apiurl, params=params)
        if response.status_code == 200:
            data = response.json()
            minimized_data = []
            for each in data.get("docs", []):
                minimized_data.append({
                    "title": each.get("title", "N/A"),
                    "authors": each.get("author_name", []),  # List of authors
                    "first_publish_year": each.get("first_publish_year", "N/A")
                })
            return minimized_data
        else:
            return {"error": "Failed to get search results from Open Search API"}
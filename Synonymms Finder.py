import requests

def get_synonyms(word):
    try:
        # Define the base URL of the WordsAPI
        base_url = "https://api.wordsapi.com/v1/words/"

        # Make a GET request to the API to get synonyms
        response = requests.get(f"{base_url}{word}/synonyms")
        data = response.json()

        # Check if the API returned synonyms
        if "synonyms" in data:
            synonyms = data["synonyms"]
            return synonyms
        else:
            return f"No synonyms found for '{word}'."

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    word = input("Enter a word: ")
    synonyms = get_synonyms(word)

    if isinstance(synonyms, list):
        if synonyms:
            print(f"Synonyms for '{word}':")
            for i, synonym in enumerate(synonyms, start=1):
                print(f"{i}. {synonym}")
        else:
            print(f"No synonyms found for '{word}'.")
    else:
        print(synonyms)

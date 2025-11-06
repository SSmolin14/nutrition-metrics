import requests

# Replace with your actual USDA API key
API_KEY = "ut9hNfWKxDDMN0eH78YfY9gxXpGCjR32HxhuyWUv"

# Food to search
search_term = "apple"

# API URL
url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={search_term}&api_key={API_KEY}"

# Make the request
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    foods = data.get("foods", [])
    for food in foods[:5]:  # show first 5 results
        print("Name:", food.get("description"))
        print("Brand:", food.get("brandOwner", "N/A"))
        print("Calories:", next((n['value'] for n in food.get("foodNutrients", []) if n['nutrientName'] == "Energy"), "N/A"))
        print("Protein:", next((n['value'] for n in food.get("foodNutrients", []) if n['nutrientName'] == "Protein"), "N/A"))
        print("Fat:", next((n['value'] for n in food.get("foodNutrients", []) if n['nutrientName'] == "Total lipid (fat)"), "N/A"))
        print("-" * 40)
else:
    print("Error:", response.status_code, response.text)
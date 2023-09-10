import openai

# Your OpenAI API Key
API_KEY = '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'
openai.api_key = API_KEY

# Mock criteria for demonstration
SOIL_TYPE = "loamy"
CLIMATE = "temperate"

# Define our mock crop database
CROP_DATABASE = {
    "loamy": {
        "temperate": ["wheat", "barley", "potato"]
    },
    # ... you can add more criteria and crops here
}

# Query the LLM via OpenAI API for detailed instructions
def get_growing_instructions(crop):
    prompt = f"How to grow {crop}?"
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150)
    instructions = response.choices[0].text.strip()
    return instructions

# Recommend crops based on criteria
def recommend_crops(soil_type, climate):
    return CROP_DATABASE.get(soil_type, {}).get(climate, [])

def main():
    recommended_crops = recommend_crops(SOIL_TYPE, CLIMATE)
    
    if not recommended_crops:
        print("No crops recommended for the given criteria.")
        return
    
    print(f"Recommended crops for {SOIL_TYPE} soil in {CLIMATE} climate are:")
    for crop in recommended_crops:
        print(f"- {crop}")
    
    # Now, get growing instructions from LLM
    for crop in recommended_crops:
        instructions = get_growing_instructions(crop)
        print(f"\nGrowing {crop}:")
        print(instructions)

if __name__ == "__main__":
    main()

import openai

openai.api_key = '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'

SOIL_TYPE = "loamy"
CLIMATE = "temperate"

CROP_DATABASE = {
    "loamy": {
        "temperate": ["wheat", "barley", "potato"]
    },
}

def recommend_crops(soil_type, climate):
    return CROP_DATABASE.get(soil_type, {}).get(climate, [])

def get_growing_instructions(crop):
    response = openai.Completion.create(
      engine="davinci",
      prompt=f"How to grow {crop}?",
      max_tokens=150
    )
    
    instructions = response.choices[0].text.strip()
    return instructions

def main():
    recommended_crops = recommend_crops(SOIL_TYPE, CLIMATE)
    
    if not recommended_crops:
        print("No crops recommended for the given criteria.")
        return
    
    print(f"Recommended crops for {SOIL_TYPE} soil in {CLIMATE} climate are:")
    for crop in recommended_crops:
        print(f"- {crop}")
    
    for crop in recommended_crops:
        instructions = get_growing_instructions(crop)
        print(f"\nGrowing {crop}:")
        print(instructions)

if __name__ == "__main__":
    main()

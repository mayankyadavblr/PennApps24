import openai

# Your OpenAI API Key
API_KEY = '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'
openai.api_key = API_KEY

# Mock crop database for demonstration
CROP_ROTATION_LIST = ['wheat', 'mangoes', 'apples', 'grapes', 'orange']

# Query the LLM via OpenAI API for crop rotation table
def get_crop_rotation(crops):
    prompt = "what is the best crop rotation method that should be used with {}, {}, {}, {} and {} in each year? " \
             "make it into a table format with one of the columns as the seasons. Just give the table. " \
             "Prioritize first crop in the list since it will earn more money".format(crops[4], crops[3], crops[2], crops[1], crops[0])
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=300)
    return response.choices[0].text.strip()

def main():
    print("Crops for rotation are:")
    for crop in CROP_ROTATION_LIST:
        print("- {}".format(crop))

    rotation_table = get_crop_rotation(CROP_ROTATION_LIST)
    print("\nCrop Rotation Table:")
    print(rotation_table)

if __name__ == "__main__":
    main()

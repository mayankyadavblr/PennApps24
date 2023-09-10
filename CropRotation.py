import openai
import os
import pandas as pd
import time

openai.api_key = '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'

def main_rotation(crops):

    a="what is the best crop rotation method that should be used with {}, {}, {}, {} and {} in each year? make it into a table format with one of the columns as the seasons. Just give the table. Prioritize first crop in the list since it will earn more money".format(crops[4], crops[3], crops[2], crops[1], crops[0])

    prompt = a

    response = get_completion(prompt)
    return response

def get_completion(prompt, model="ada"):

    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(

        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,

    )

    return response.choices[0].message["content"]


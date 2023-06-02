#!/usr/bin/python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=10&category=20&difficulty=medium&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    for q in data['results']:
        question= q['question']
        correct= q['correct_answer']
        incorrect= q['incorrect_answers']
        answers= incorrect + [correct]

        print(f"{question}\n{answers}")
        #print(answers, "\n")
        #print(type(correct),type(incorrect))
    #print(data['results'][0]['question'])
    #question= data['question']
    #print(question)



if __name__ == "__main__":
    main()


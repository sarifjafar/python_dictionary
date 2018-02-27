import json
import difflib 

data = json.load(open("data.json"))

def getMeaning(input_word):
    input_word = input_word.lower()
    if input_word in data:
        return data[input_word]
    elif len(difflib.get_close_matches(input_word,data.keys())) > 0:
        predict_word = difflib.get_close_matches(input_word,data.keys())
        choice = input("Did you mean \"%s\" instead? Enter Y/N/Q: " % predict_word[0])
        if choice == "Y":
            return data[str(predict_word[0])]
        elif choice == "N":
            for x in predict_word:
                if x != predict_word[0]:
                    if len(x)>1:
                        sec_choice = input("Did you mean %s instead? Enter Y/N/Q: " % x)
                        if sec_choice == "Y":
                            return data[str(x)] 
                        if sec_choice == "Q":
                            exit()
            print("Sorry!! No Word for your Matching")        
        else:
            return                 
    else:
        return "Sorry!! No Word for your Matching"    


inp = str(input("Enter Word :"))
result = getMeaning(inp)
# print(type(result))
if type(result) == list:
    i = 1
    print("-----------------------------------------------------------------\n")
    for meaning in result:
        print(str(i)+" "+str(meaning)+"\n")
        i = i+1

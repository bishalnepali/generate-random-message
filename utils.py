
import pandas as pd
import random
import re

# message template
MT='''<greeting> <reader_adjective> <reader>, <time> <reader_action1> your <trophy> for 
<reader_action2> <history>. <we> <with help> <experts> and <consent>, <created> a 
<book_adjective> <book_noun> for <superlative>. <reader_action3> [Link] <see> how 
<book_adjective> the <book_noun> is.
'''


    


def get_random_word(word_key,df):
    try:
        word = random.choice([x.strip() for x in df[word_key].to_list() if type(x) == str])
    except:
        word = ''
    return word
def main():

    # read the excel file word_key.xlsx
    message = MT
    df= pd.read_excel('word_key.xlsx')
    variable_template = re.findall(r'(<.*?>)',message)
    message_dict = {variable_template[i]:get_random_word(variable_template[i],df) for i in range(len(variable_template))}
    for key,value in message_dict.items():
        message = message.replace(key,value)
    # replaing the keys values with the values from the dictionary
    
    return message

    # permutate the pandas dataframe
   
# permuta



if __name__ == '__main__':
    print("Generating message")
    for i in range(10):
        print(main())
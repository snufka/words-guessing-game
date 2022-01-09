import random

word_list = ["brand","sandy","value","dealy","daily", "creek", "lands"]

random_word = random.choice(word_list)
print(random_word)

guess_num_one = input("Enter your first guess: ")
print (guess_num_one)

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1


random_list = Convert(random_word)
guess_one_list = Convert(guess_num_one)

#finding the smae letters
same_chars = set(random_list).intersection(guess_one_list)

if len(same_chars) > 0: 
    print('Correct guesses: ',list(same_chars))
else: 
    print('You guessed 0 chars')

#checking if the char location is correct
def main():
    correct = []    
    for x,y in enumerate(random_list):
        if guess_one_list[x] == y:
            correct.append([y,random_list.index(y)])    
    print(correct)
main()

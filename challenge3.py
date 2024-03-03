import random

def word_generator(N):
    if N < 1 or N > 200000:
        return "Invalid input"
    
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        # creating an empty list  
        word = []
        i = 0 
        while i <  N:
            # generating a random letter from the alphabets 
            random_char = random.choice(alphabet)
            
            if random_char not in word:
                word.append(random_char)
            i += 1    
            
        
        print("".join(word)) 
    


word_generator(3)  

word_generator(5) 
 

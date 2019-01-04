import math

def vowel(words):
    v ="aeiou"
    length = len(v)
    count = 0
    resultflage = 1
    for char in words:
        if char in v:
            if count >= length or char != v[count]:
                resultflage= 0
                return resultflage 
            count = count+1
    if(count == length):
        resultflage= 1
        return resultflage
    else:
        resultflage= 0
        return resultflage
            



def main():
    with open ("dictionary.txt","r") as f:
        for line in f:
            x = line
            words = x.lower();
            if vowel(words) == 1:
                print (words)

main()

# results :
#abstemious

#abstemiously

#abstentious

#acheilous

#acheirous

#acleistous

#aeiou

#aeiouyw

#aeiouzc

#affectious

#annelidous

#arsenious

#artemidorus

#arterious

#bacterious

#caesious

#facetiously

#fracedinous

#majestious

#tragedious

#transtendinous

#travertinous

                
     

       

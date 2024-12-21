with open("/Users/faisal/workspace/github.com/ElectricDoodle/bookbot/books/frankenstein.txt") as f:
    file_contant=f.read()
with open("/Users/faisal/workspace/github.com/ElectricDoodle/bookbot/books/frankenstein.txt") as f:
    file_contant=f.read()

def count_word(txt):
    words=txt.split()
    count=0
    for word in range(len(words)):
        count+=1
    return count

def countCharacters (text):
    count_char={}
    for i in text.lower():
        if i not in count_char:
            count_char[i]=1
        else:
            count_char[i]+=1
    return count_char
def sortList(dic):
    alph=[]
    num=[]
    for k,v in dic.items():
        alph.append(k)
        num.append(v)
    for i in range(len(alph)):
        print(f" The '{alph[i]}' character was found {num[i]} times")



print('--- Begin report of books/frankenstein.txt ---')
print(f'{count_word(file_contant)} words found in the document')
sortList(countCharacters(file_contant))
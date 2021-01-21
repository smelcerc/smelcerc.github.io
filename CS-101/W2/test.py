sample_word = input()

prefix = 'a'

vowels = ('a', 'e', 'i', 'o', 'u')

vowel_start = sample_word.startswith(vowels)

if vowel_start:
    prefix = 'an'



print(prefix)
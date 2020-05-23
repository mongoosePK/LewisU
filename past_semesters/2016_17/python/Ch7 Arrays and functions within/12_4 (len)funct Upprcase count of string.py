def main() :
    sentence = input('Enter a sentence: ')
    ##initialize counter
    uppercase_count = int(0)
    #loop through sentence and count uppercase variables
    for index in range(0, len(sentence)):
        if sentence[index].isupper() :
            uppercase_count += 1

    #display number of uppercase characters
            print('The string has ', uppercase_count, 'uppercase letters.')

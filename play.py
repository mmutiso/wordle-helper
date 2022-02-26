import json

def positional_exclusion(config, word):
    '''
    if any of the characters in the phrase are  in the word at that position return false else return true
    '''
    positional_exclusion = config["positional_exlusions"]

    for key in positional_exclusion:
        position_index = int(key) - 1
        for character in positional_exclusion[key]:
            if word[position_index] == character:
                return False

    return True

def mask_match(config, current_word):
    '''
    if the given letter is in the given position, return true

    But if no letter is given then also return true
    '''
    word_mask = config["word"]

    if word_mask is None:
        return True

    if len(word_mask) == 0:
        return True

    for i in range(5):
        mask_character = word_mask[i]
        actual_character = current_word[i]

        if mask_character == "?":
            continue
        else:
            if mask_character != actual_character:
                return False

    return True

def word_includes(config, word):
    '''
    Determine if a set of characters is available in the word
    and return true if all of the characters are available
    '''
    available_characters = config["inclusion"]
    n = len(available_characters)
    availability = [False] * n
    for position in range(n):
        character_is_available = available_characters[position] in word
        availability[position] = character_is_available


    if False in availability:
        return False
    else:
        return True

def word_excludes(config, word):
    '''
    Determine if a set of characters is available in the word
    and return False if any of the characters are available
    '''
    available_characters = config["exclusion"]
    for character in available_characters:
        if character in word:
            return False

    return True

def the_word_matches(config, word):
    '''
    Perform all checks and check if the word matches giving priority to the mask
    '''   

    mask_is_matched = mask_match(config, word)
    positional_exlusion_is_matched = positional_exclusion(config, word)
    included_letters_match = word_includes(config, word)
    excluded_letters_match = word_excludes(config, word)

    #print("word={} mask is={}, exclusion is={}".format(word, mask_is_matched, exlusion_is_matched))
    if not mask_is_matched:
        return False
    
    return mask_is_matched and positional_exlusion_is_matched and included_letters_match and excluded_letters_match



def main():
    f = open("config.json")
    lines = f.readlines()
    content = str.join("", lines)
    config = json.loads(content)
    f.close()

    words = open("five_letter_words.txt")
    counter  = 0
    for word in words.readlines():
        word = word.strip()
        
        if not the_word_matches(config, word):
            #print("not matched")
            continue
        
        counter += 1
        print(word)

    words.close()
    print("Matched {} words".format(counter))

if __name__ == "__main__":
    main()

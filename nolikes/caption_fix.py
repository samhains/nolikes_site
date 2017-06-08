from pattern.en import lemma, lexeme, parsetree, Sentence, tag
# sentence = "a man holding a cell phone in his hand"
sentence = "a man and a woman eating a piece of pizza"


def fix_caption(str):
    s = parsetree(str, lemmata=True)
    string = ''
    for sentence in s:
        if "and a" in str:
            string = str+' '
        else:
            for i, chunk in enumerate(sentence.chunks):
                if chunk.type == 'VP' and len(chunk) == 2:
                    verb = chunk[1].string
                    string += lexeme(verb)[1]+' '
                else:
                    for j, w in enumerate(chunk.words):
                        if i == 0 and j == 0 and (w.string == 'a' or w.string == 'A'):
                            print('chuk', chunk)
                            pass
                        else:
                            string = string + w.string+' '

    string = string[:1].upper() + string[1:-1]
    if string.startswith('A'):
      string = string[2].upper() + string[3:]
    if string.endswith('.'):
      string = string[:-1]
    return string


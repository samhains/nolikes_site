from pattern.en import verbs, lemma, lexeme, parsetree, Sentence
sentence = "a man holding a cell phone in his hand"


def fix_caption(str):
    s = parsetree(str, lemmata=True)
    string = ''
    for sentence in s:
        for i, chunk in enumerate(sentence.chunks):
            print(chunk)
            if chunk.type == 'VP' and len(chunk) == 2:
                print('@!!')
                verb = chunk[1].string
                string += lexeme(verb)[1]+' '
            else:
                for j, w in enumerate(chunk.words):
                    if i == 0 and j == 0 and (w.string == 'a' or w.string == 'A'):
                        print w.string
                        pass
                    else:
                        string = string + w.string+' '

    return string[:1].upper() + string[1:-1]


print(fix_caption(sentence))

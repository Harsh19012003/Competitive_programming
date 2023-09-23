def encode(strings):

    og = ""
    for str in strings:
        if str == ":":
            og += "::;"
        else:
            og += str
            og += ":;"

    print("encoded: ", og)
    
    return og




def decode(sequence):

    strings = []

    word = ""

    for i in range(len(sequence)):
        
        if sequence[i] != ":":
            print(sequence[i])
            if sequence[i] == ";":
                continue
            word += sequence[i]
            print(word)
        else:
            # print(word)
            strings.append(word)
            word = ""

            if sequence[i+1] == ":":
                strings.append(":")
            
            if sequence[i+1] == ";":
                continue
        
    print("decoded: ", strings)



sequence = encode(["lint","code","love","you"])
sequence = encode(["we", "say", ":", "yes"])




decode(sequence)
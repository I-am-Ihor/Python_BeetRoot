def words_counter(string):
    
    words = string.split(" ")
    result = {}
    
    for word in words:
        if word not in result:
            result[word] = 1
        elif word in result:
            result[word] += 1

    return result

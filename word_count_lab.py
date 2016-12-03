def words(phrase):
    coll_words = {}
    split_phrase = phrase.split()

    for i in split_phrase:
        if str(i) not in coll_words:
            coll_words[i] = 1
        else:
            coll_words[i] += 1

    return coll_words
print words("one fish two fish red fish blue fish ! j%^&&* .")
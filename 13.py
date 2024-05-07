def count_common(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    top_four = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:4]
    return top_four

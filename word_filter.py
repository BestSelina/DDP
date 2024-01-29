import re

def word_filter_counter(text, filter_words):
    text = text.lower()
    words = re.split(r'[,!?. ]+', text)
    # print(words) 
    words = list(filter(None, words))
    count = {}
    for str in words:
        if str in count:
            count[str] += 1
        else:
            count[str] = 1
    # print(count)
    ans = {}
    if len(filter_words) == 1:
        ans[filter_words[0]] = count[filter_words[0]]
        return ans
    else:
        for str in filter_words:
            ans[str] = count[str]
        return ans


# Test cases
print(
    word_filter_counter("Hello world, hello!", ["hello"])
)  # Expected output: {'hello': 2}
print(
    word_filter_counter("The quick brown fox.", ["the"])
)  # Expected output: {'the': 1}
print(
    word_filter_counter(
        "Is this real life? Is this just fantasy?", ["is", "this", "just"]
    )
)  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(
    word_filter_counter(
        "Do we see the big picture or just small details?", ["we", "the", "or"]
    )
)  # Expected output: {'we': 1, 'the': 1, 'or': 1}

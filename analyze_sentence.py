def analyze_sentence():
    sentence = input("Enter a sentence ending with a period (e.g. 'Hello world.'):\n")

    if not sentence.endswith('.'):
        print("Error: The sentence must end with a period.")
        return

    sentence_without_dot = sentence[:-1]
    char_count = len(sentence_without_dot)
    word_count = len(sentence_without_dot.split())
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for ch in sentence_without_dot if ch in vowels)

    print("Number of characters:", char_count)
    print("Number of words:", word_count)
    print("Number of vowels:", vowel_count)

if __name__ == "__main__":
    analyze_sentence()

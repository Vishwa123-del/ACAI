def check_membership(corpus, stream):
    """
    Optimized membership check: converts corpus to set for O(1) lookups,
    then maps stream to booleans indicating presence in corpus.
    """
    corpus_set = set(corpus)
    return [item in corpus_set for item in stream]

if __name__ == "__main__": 
    # Get input from user
    print("Enter corpus elements (space-separated):")
    corpus_input = input().strip()
    corpus = [int(x) for x in corpus_input.split()]
    
    print("Enter stream elements (space-separated):")
    stream_input = input().strip()
    stream = [int(x) for x in stream_input.split()]
    
    # Perform membership check
    result = check_membership(corpus, stream)
    print("Membership results:", result)
    
    # Show which elements are in corpus
    for i, item in enumerate(stream):
        status = "in" if result[i] else "not in"
        print(f"{item} is {status} the corpus")

#tuthang102 on github

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    #base case:
    #if the length of sequence is 1, return only the sequence    
    if len(sequence) == 1:
        return [sequence]
    #store all permutations
    result = []
    #iterate through sequence getting the character and its index
    for i, let in enumerate(sequence):
        #iterate through this function's return result 
        #pass in as sequence: 
        #slice of the beginning of sequence up to current index
        #concatted to slice of one greater than current index to the end 
        for p in get_permutations(sequence[:i] + sequence[i + 1:]):
            #result equals current result plus
            #an array containing current letter concatted to current 
            #iteration of this function's return result
            #WTF
            result = result + [let + p]
    return result




if __name__ == '__main__':
#    #EXAMPLE
#   example_input = 'abc'
#   print('Input:', example_input)
#   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#   print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
    example_input_1 = 'a'
    print('Input:', example_input_1)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example_input_1))
    
    example_input_2 = 'hi'
    print('Input:', example_input_2)
    print('Expected Output:', ['hi', 'ih'])
    print('Actual Output:', get_permutations(example_input_2))
    
    example_input_3 = 'bot'
    print('Input:', example_input_3)
    print('Expected Output:', ['bot', 'obt', 'otb', 'bto', 'tbo', 'tob'])
    print('Actual Output:', get_permutations(example_input_3))
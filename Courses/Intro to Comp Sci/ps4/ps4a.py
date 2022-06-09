# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

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
    if len(sequence) == 1:
        return [sequence]

    c1 = sequence[0] # first letter of sequence
    perm_list = []   
    for p in get_permutations(sequence[1:]): # everything else
        for i in range(len(sequence)):
            perm_list.append( p[:i] + c1 + p[i:] ) # insert at different places

    return perm_list
    # i'm dumb, why did this take so long

if __name__ == '__main__':
    #    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

    print('\n===== Test =====')

    print('\n3 chars')
    example_input = 'def'
    print('Input:', example_input)
    print('Expected Output:', ['def', 'dfe', 'edf', 'efd', 'fed', 'fde'])
    print('Actual Output:', get_permutations(example_input))

    print('\n2 chars')
    example_input = 'ab'
    print('Input:', example_input)
    print('Expected Output:', ['ba', 'ab'])
    print('Actual Output:', get_permutations(example_input))

    print('\n1 char')
    example_input = 'a'
    print('Input:', example_input)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example_input))
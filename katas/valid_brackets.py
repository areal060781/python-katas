'''
validBracketSequence (Task 1 of 3)
(1:29:03)
Codewriting

Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether
or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.
Example

For sequence = "()", the output should be validBracketSequence(sequence) = true;
For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
For sequence = "(]", the output should be validBracketSequence(sequence) = false;
For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.
Input/Output

[execution time limit] 4 seconds (php)

[input] string sequence

A bracket sequence, consisting of the characters (, ), [, ], {, and }.

Guaranteed constraints:
0 ≤ sequence.length ≤ 106.

[output] boolean

true if sequence is a valid bracket sequence and false otherwise.
'''


def valid_bracket_sequence(sequence):
    # Declaraing a stack.
    stack = []
    # Iterating over the entire string
    for paren in sequence:
        # If the input string contains an opening parenthesis,
        # push in on to the stack.
        if paren == '(' or paren == '[' or paren == '{':
            stack.append(paren)
        else:
            # In the case of valid parentheses, the stack cannot be
            # be empty if a closing parenthesis is encountered.
            if not stack:
                return False
            else:
                # If the input string contains a closing bracket,
                # then pop the corresponding opening parenthesis if
                # present.
                top = stack[-1]
                if paren == ')' and top == '(' or \
                        paren == ']' and top == '[' or \
                        paren == '}' and top == '{':
                    stack.pop()
    # Checking the status of the stack to determine the
    # validity of the string.
    if not stack:
        return True
    else:
        return False

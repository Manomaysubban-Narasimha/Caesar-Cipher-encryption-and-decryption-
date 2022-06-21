# Author: Manomay Subban Narasimha
# Python 3.9.7
'''
Description: This project models the Caesar Cipher by taking an input text from the user,
and either encrypting it or decrypting it by shifting each letter within the original input 
text by the number of places that the user desires. 
Skills applied: binary search, linear search, time and space complexity analysis, 
modular arithmetic, lists, and functions
'''
from UXEnhancer import logo

def binarySearch(array, target, start, end):
    '''
    An iterative approach for implementing binary search since recursive 
    approach would take more space in the worst case, log(26) = 5 stack frames created.
    Time complexity: O(1) since the array would always be of size 26 in this program
    Space complexity: O(1) since recursion is not being used and the space requirement 
    doesn't scale as input size increases
    '''

    while start <= end:
        midIndex = (start + end) // 2
        mid_element = array[midIndex]
        if mid_element == target:
            return midIndex
        elif mid_element < target:
            start = midIndex + 1
        else:
            end = midIndex - 1
    return -1
        

def caesar(text, shift, cipher_direction):
    '''
        Time complexity: O(n) where n is the length of the text
        Space complexity: O(n) where n is the length of the text
    '''
    text = list(text)
    if cipher_direction == 'decode':
            shift *= -1
    for index, character in enumerate(text):
        '''
        Python's index() function on lists makes use of the linear search
        algorithm. Although, using this method wouldn't affect the asymptotic
        representation of the time complexity of this program, there would 
        definitely be more computations while compared to making use of the 
        binary search algorithm which seems appropriate for this scenario since
        the elements within the alphabets list are sorted in lexicographical order.
        Both algorithms would end up taking constant time in this case, since
        the number of computations required to find the index of an alphabet within
        the list does not grow as the input size increases.
        '''
        # current_index = alphabets.index(character) would take slightly longer
        # in the worst case scenario, 26 units of time
        current_index = binarySearch(alphabets, character, 0, len(alphabets) - 1) # worst case: log(26) units of time
        if current_index == -1:
            continue
        new_index = (current_index + shift) % len(alphabets)
                
        text[index] = alphabets[new_index]

    # copy the elements of the coded list into a string for being displayed 
    coded_text = ""
    for coded_char in text:
        coded_text += coded_char
    print(f"The {direction}d text is {coded_text}")


def get_input():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    direction = direction.lower()

    # do not proceed unless the user types a valid direction with proper spelling
    correct_directions = ['encode', 'decode']
    while direction not in correct_directions:
        print(f'Invalid input: "{direction}". Please enter a valid option.')
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")    
    
    text = input("Type your message:\n").lower()

    # continuously prompt the user to enter a number if they enter other characters
    shift = input("Type the shift number:\n")
    while not shift.isdigit():
        print("Please enter a NUMBER for the shift number")
        shift = input("Type the shift number:\n")
    shift = int(shift)

    return (text, shift, direction)

            
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

end = False
while not end:
    text, shift, direction = get_input()
    caesar(text, shift, direction)
    preference = input("Type 'yes' to go again. Type 'no' to quit: ").lower()
    while preference != 'no' and preference != 'yes':
        preference = input("Type 'yes' to go again. Type 'no' to quit: ").lower()
    if preference == 'no':
        end = True
    print("\n--------------------------------------------------------------------------------\n")

print("Thank you for trying out caesar cipher! Have a great day!")

"""
Sample output 1:

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
Coding is fun!
Type the shift number:
3
The encoded text is frglqj lv ixq!
------------------------------------------------------------
Sample output 2:

Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
Python is amazing!
Type the shift number:
5
The decoded text is ktocji dn vhvudib!
"""

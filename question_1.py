"""
++++++++++++++++++++++++++++++++
Twilio Screening Interview
Questions 1
5-13-20

++++++++++++++++++++++++++++++++
Longest Prefix Match

When Twilio handles outbound phone calls, we need to route them based on which 
carriers give us the best rates for the call. The call gets routed based on the 
longest prefix that matches the number. For example, a phone number of 
+14123334444 would best match the area prefix +1412 and be routed to the carrier
that gives us the best rates for the calls to Pittsburgh, PA.

Given an array of prefixes and an array of phone numbers, determine the longest
prefix matches for each of the phone numbers. The output must be an array of 
prefixes corresponding to the longest matches for each input phone number.

Contraints:
- All prefixes will be of shorter length than all phone numbers
- The second input parameter (numbers) may have repeat elements
- The output array should contain a subset of the input array of phone numbers
- Numbers and prefixes will the in the E.164 format, i.e. a plus (+) followed 
by up to 15 digits (0-9)

"""

import unittest


def match2(prefixes, numbers):
    """find the best prefix match for each phone number given as an input. 
    If there is no prefix match for a given phone number, return an empty string. 

    Inputs: 
    prefixes: an array of strings
    numbers: an array of strings


    Discussion: This is the second solution that I thought of. The run time 
    complexity is high because there is a for loop in line 33 and that additionally
    compunds with a list slice on line 37. 

    It would be more time efficient to 'pop' the last value from each number 
    (instead of the list slice in line 43),  but the .pop() method is not 
    available to strings in Python. An alternative could be converting each number 
    in the numbers array to a 'list' type, but the conversion would also add O(n) 
    computation time and therefore doesn't offer much advantage.
    
    runtime complexity: (O)n^2

    """

    matching = [] #make a new list to save the matching prefixes
    
    # iterate through numbers to find a match for each
    for i, num in enumerate(numbers): 

        #look for matching prefixes, ignoring the first index which will always be '+'
        while len(num) > 1: 
            num = num[:-1] # reduce the length of the phone number by 1 value
            if num in prefixes: # take the first prefix value that matches
                matching.append(num)
                break

        if len(matching) < i + 1: # add an empty string if no match is found
            matching.append("")

    return matching


def match(prefixes, numbers):
    """
    find the best prefix match for each phone number given as an input. 
    If there is no prefix match for a given phone number, return an empty string. 

    Inputs: 
    prefixes: an array of strings
    numbers: an array of strings

    Discussion: This is the first solution that I though of, but it has disadvantages. 
    There are many lines of code and the runtime complexity is high.

    Runtime complexity: (O)n^2
    """

    matching = [] #make a new list to save the matching prefixes
    
    # iterate through numbers to find a match for each
    for num in numbers: 

        best_pre = "" # create an empty string to store the best prefix value
        count = 0 # store the number of matching characters for each prefix
        
        # count the number of matching characters from each prefix for the num
        for pre in prefixes:

            i = 1 # index for the num, start at 1 to skip the '+' sign
            chars = 0 # number of matching variables

            # update char if matching numbers are found
            while  i < len(num) and i < len(pre):
                if num[i] == pre[i]:
                    chars += 1
                    i += 1
                # if numbers don't match then break the while loop
                else:
                    break

        # update count and best_pre if a better match is found
            if count < chars and len(pre) == i:
                best_pre = pre
                count = chars

        # append the best prefix (or an empty list) to matching
        matching.append(best_pre)

    return matching

            
class testMatch(unittest.TestCase):
    """Test the match function."""

    def test_match(self):

        # general case with len > 1 for prefixes and numbers
        prefixes1 = ['+1415123', '+1415000', '+1412', '+1510', '+1', '+44']
        numbers1 = ['+14151234567', '+99999999999', '+14121234567', '+19999999999']
        expected1 = ['+1415123', "", '+1412', '+1']
        self.assertEqual(match2(prefixes1, numbers1), expected1)

        # edge case of an empty prefixes list
        prefixes2 = [] 
        numbers2 = ['+14151234567', '+99999999999', '+14121234567', '+19999999999']
        expected2 = ['', '', '', '']
        self.assertEqual(match2(prefixes2, numbers2), expected2)

        # edge case of an empty numbers list
        prefixes3 = ['+1415123', '+1415000', '+1412', '+1510', '+1', '+44'] 
        numbers3 = []
        expected3 = []
        self.assertEqual(match2(prefixes3, numbers3), expected3)

        # edge case of an empty numbers list and an empty prefixes list
        prefixes4 = [] 
        numbers4 = []
        expected4 = []
        self.assertEqual(match2(prefixes3, numbers3), expected3)

        # edge case of a single value in numbers list and in prefix list
        prefixes5 = ['+1415123'] 
        numbers5 = ['+14151234567']
        expected5 = ['+1415123']
        self.assertEqual(match2(prefixes5, numbers5), expected5)

        # edge case of a single value in numbers list and in prefix list
        prefixes6 = ['+1415123'] 
        numbers6 = ['+99999999999']
        expected6 = ['']
        self.assertEqual(match2(prefixes6, numbers6), expected6)


if __name__ == '__main__':
    
    # print(match2(['+1415123', '+1415000', '+1412', '+1510', '+1', '+44'], ['+14151234567', '+99999999999', '+14121234567', '+19999999999']))
    # print(match2(['+1415123', '+1415000', ], ['+14151234567']))

    unittest.main()

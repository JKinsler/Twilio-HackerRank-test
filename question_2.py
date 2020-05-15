"""
++++++++++++++++++++++++++++++++
Twilio Screening Interview
Questions 2
5-13-20

++++++++++++++++++++++++++++++++
SMS compliance

Problem statement:
Given an input string of arbitrary length, output SMS-complliant segments with suffixes
- A SMS-compliant segment is of length 160 characters or less.
- do not generate segments if the input fits in a single message
- A segment suffix looks like '(1/5)' for the first five segments
- the segment content nd suffix must both fit in the segment

Inputs will only consist of A-Z, a-z, spaces ( ), commas (, ), and periods (.)
You implementation can expect a maximum of 9 segments per input.
"""

import unittest

def sms_maker(message):

    """create SMS compliant segments of 160 chars or less from an original message

    Input: string
    Output: list of strings"""

    # if the message is already SMS complient, return message.
    if len(message) <= 160:
        return message

    # if the message is not already SMS complient, divide it into segments.

    # store the segments as a list of strings
    segments = []

    # create the first and middle segments, leaving character space for the sms suffix
    while len(message) > 155:
        seg = message[:155] # take the first 155 elements, leave five spaces for the suffix
        segments.append(seg)
        message = message[155:] # remove the first 155 elements from the message

    # create the last segment
    if len(message) > 0:
        # create a new segment, starting, with a space, and then add remaining message characters
        seg = message[:]
        segments.append(seg)

    # add the suffix to each sms segment
    segs = len(segments) # get the total number of segments

    for i, seg in enumerate(segments):
        segments[i] = seg + f"({i+1}/{segs})"

    return segments


class testSMSMaker(unittest.TestCase):
    """Test the sms_maker function."""

    def test_sms_maker(self):

        message1 = "Hello, this is a test message."
        expected1 = "Hello, this is a test message."
        self.assertEqual(sms_maker(message1), expected1)

        message3 = "On the far-away island of Sala-ma-Sond, Yertle the Turtle was king of the pond. A nice little pond. It was clean. It was neat. The water was warm. There was plenty to eat. The turtles had everything turtles might need. And they were all happy. Quite happy indeed."
        message3 = ['On the far-away island of Sala-ma-Sond, Yertle the Turtle was king of the pond. A nice little pond. It was clean. It was neat. The water was warm. There wa(1/2)', 's plenty to eat. The turtles had everything turtles might need. And they were all happy. Quite happy indeed.(2/2)']
        self.assertEqual(sms_maker(message3), message3)

        message4 = ""
        message4 = ""
        self.assertEqual(sms_maker(message3), message3)

if __name__ == '__main__':

    unittest.main()


    """
    Discussion:
    Runtime complexity:O(n)

    Remaining steps for extra credit:
    - split the message over white space
    - append characters to the segments as long as the line count remains less than 155 (for middle segments)
    - start a new line when line count excedes what is desired
    """

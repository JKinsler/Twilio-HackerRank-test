"""
++++++++++++++++++++++++++++++++
Twilio Screening Interview
Questions 2
5-13-20

++++++++++++++++++++++++++++++++
"""

def sms_maker(message):

    """create SMS compliant segments of 160 chars or less from an original message

    Input: string
    Output: list of strings"""

    # if the message is already SMS complient, return message.
    if len(message) <= 160:
        return message

    # if the message is not SMS complient, divide it into segments.

    # store the segments as a list of strings
    segments = []

    # create the first segment, leaving character space for the sms suffix
    seg = message[:155] # take the first 155 elements from the message and add the suffix
    segments.append(seg)
    message = message[155:] # remove the first 155 elements from the message

    # create the middle segments, leaving character space for the sms suffix
    while len(message) > 154:
        # create a new segment, starting, with a space, and then add 154 more characters
        seg = " " + message[:154] # MAY NOT NEED THE SPACE, re-read problem instructions
        message = message[154:]
        segments.append(seg)

    # create the last segment
    if len(message) > 0:
        # create a new segment, starting, with a space, and then add remaining message characters
        seg = " " + message[:]
        segments.append(seg)

    # add the suffix to each sms segment
    segs = len(segments) # get the total number of segments

    for i, seg in enumerate(segments):
        segments[i] = seg + f"({i+1}/{segs})"

    return segments


if __name__ == '__main__':

    res = sms_maker('hello my name is johanna and Im applying for the twilio hatch program. Its late a night and I’m checking this code for bugs. Right now, I’m trying to type something that will be more than 160 characters. This is a lot of characters for me to type when I’m not trying to say anything in particular. It would be very exciting for me to be a part of the hatch program. There are many jobs out there but what I like about the hatch program is the culture at twilio and the opportunity to hit the ground with lots of learning. There are so many reasons I can think of that this would be a great job for me. ')
    print(res)

    """
    Discussion:
    Runtime complexity:O(n)
    Space complexity:O(n)

    Remaining steps for extra credit:
    split the message over white space
    append characters to the segments as long as the line count remains less than 154 (for middle segments)
    start a new line when line count excedes what is desired
    """

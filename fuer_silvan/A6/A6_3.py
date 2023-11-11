#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.keywords = keywords
        self.template = template
        pass

    def filter(self, msg):
        lower_keys = [k.lower() for k in self.keywords]
        upper = [l.isupper() for l in msg]
        for word in lower_keys:
            if word in msg.lower():
                rep = self.template*len(word)
                msg = msg.lower().replace(word, rep[:len(word)])

        for i in range(len(msg)):
            if upper[i]:
                msg = msg[:i] + msg[i].upper() + msg[i+1:]
        return msg


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    #clean_msg = f.filter(offensive_msg)
    #print(clean_msg)  # abc defghi ?#$?#$? jklmno
    offensive_msg = "aBc defghi maStaRd jklmno duck shotteeeeer batc, fishotter."
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno ?#$?#$? ?#$?#$?, fi?#$?ter.

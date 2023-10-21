# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.


def analyze(posts):
    index_dictionary = {}
    for i in posts:
        # make a whitespace infront of #:
        i = i.replace("#", " #")
        i = "".join([c if c.isalnum() or c == "#" else " " for c in i])
        for j in i.split():
            if j.startswith("#") and len(j) > 1 and not j[1].isdigit():
                if j[1:] not in index_dictionary:
                    index_dictionary[j[1:]] = 1
                else:
                    index_dictionary[j[1:]] += 1
    return index_dictionary

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3 #nothing #236",
    "Ohhhhhooo#IHATE #zurich",
    "I love #zurich.com",
    "I love #sbb.com",]
# print(analyze(posts))
print(analyze(posts))



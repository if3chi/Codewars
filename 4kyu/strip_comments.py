"""
Complete the solution so that it strips all text that follows any of a set of comment 
markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


def solution(string, markers):
    words = string.split("\n")
    for s in markers:
        words = [w.split(s)[0].rstrip() for w in words]
    return "\n".join(words)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

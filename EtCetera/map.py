def main():
    yell("This", "is", "CS50")
    yell_map("This", "is", "CS50")
def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

def yell_map(*words):
    uppercased_map = map(str.upper, words)
    print(*uppercased_map," 2")
    """
    Those two functions do the same thing, but yell_map is using map function.
    """

if __name__ == "__main__":
    main()
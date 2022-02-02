from random import randint


def randomWord():
    """
    Gets a random word from the dictionary on file

    :return: a random 5 letter word
    """
    with open("dictionary.txt", "r") as f:
        lines = 0
        words = []

        for line in f:
			if line[0] != "<":
				words.append(line.rstrip("\n"))
				lines += 1

        idx = randint(0, lines-1)
        word = words[idx]

        f.close()
        return word


if __name__ == "__main__":
    for i in range(10):
        print(randomWord())
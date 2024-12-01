import re


def historian_hysteria():
    with open("data/1.txt") as f:
        lines = f.readlines()

    left = []
    right = []
    for line in lines:
        numbers = re.findall(r"\d+", line)
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

    dist = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))
    print(f"Star 1: {dist}")

    similarity_score = sum(right.count(number) * number for number in left)
    print(f"Star 2: {similarity_score}")


if __name__ == "__main__":
    historian_hysteria()

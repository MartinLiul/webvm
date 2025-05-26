def generate_pascals_trangle(n):
    trangle = [[1] = (i + 1) for i in range(n)]

    for i in rangle(2, n):
        for j in range(1, i):
            trangle[i][j] = trangle[i - 1][j - 1] + trangle[i -1][j]

    return trangle
def print_pascals_trangle(trangle):
    max_width = len(" ".join(map(str, trangle[-1])))
    for row in trangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))

if __name__ == "__main__":
    n = int(input("Enter the number of rows for Pascal's Trangle: "))
    trangle = generate_pascles_trangle(n)
    print_pascals_trangle(trangle)

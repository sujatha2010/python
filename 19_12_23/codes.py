if __name__ == '__main__':
    n = int(input().strip())

    # Print the pattern
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
    
    # Move to the next line after printing the pattern
    print()

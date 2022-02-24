
def frequency(note, n):
    minVal = 30.0
    maxVal = 4000.0

    for i in range(n-1):
        j=2*i
        prev = note[j]
        curr = note[j+2]
        relation = note[j+3]

        if(prev > curr):
            if(relation == "closer"):
                maxVal = min([curr + (prev-curr)/2, maxVal])
            elif relation == "further":
                minVal = max([curr + (prev-curr)/2, minVal])
        elif(curr > prev):
            if(relation == "closer"):
                minVal = max([prev + (curr-prev)/2, minVal])
            elif relation == "further":
                maxVal = min([prev + (curr-prev)/2, maxVal])

    return minVal, maxVal

def main():
    n = int(input())

    notes=[]
    notes.append(float(input()))
    notes.append("!")

    for i in range(n-1):
        num, str = input().split()
        notes.append(float(num))
        notes.append(str)

    min, max = frequency(notes, n)
    print(min, max)

if __name__ == '__main__':
    main()





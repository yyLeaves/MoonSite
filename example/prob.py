from matplotlib import pyplot as plt

#calculate probability
#japan=13736837
Countries = ["Country 1","Country 2","Country 3","Country 4","Country 5"]
sentimentScore = [0.04,0.11,0.08,0.08,0.06]
TotalScore = 0
"""
(in meters)
C1: 6611507
C2: 3943375
C3: 12538639
C4: 203107
C5: 3923258"""

Cost = [6611507,3943375,12538639,203107,3923258]
TotalCost = 0
Probability = []

for ele in range (0, len(sentimentScore)):
    TotalScore = TotalScore + sentimentScore[ele]

for ele in range (0, len(Cost)):
    TotalCost = TotalCost + Cost[ele]

for x in range (0, len(Countries)):
    Probability.append((sentimentScore[x]/TotalScore) * (1-(Cost[x]/TotalCost)))

print ("Calculated Probability: ")

for x in range (0, len(Countries)):
    print(Countries[x] + ' = ', round(Probability[x],4))

# getMax method
def getMax(array_A):
    max = array_A[0]
    for i in range(len(array_A)):
        if array_A[i] > max:
            max = array_A[i]

    return max


def shellSort(A, n):
    # set the initial gap to floor of n/2
    gap = n // 2

    # Rearrange the array elements at n/2, n/4, ..., 1 intervals
    while gap > 0:

        for i in range(gap, n):
            temp = A[i]
            j = i

            while j >= gap and A[j - gap] < temp:
                A[j] = A[j - gap]

                j -= gap

            A[j] = temp
        gap //= 2


arr = Probability.copy()
shellSort(arr, len(arr))
print('\nSorted Probability: ')

for x in range (0, len(arr)):
    print(x+1,'->', round(arr[x],4))

Sorted_Sequence_of_Country = []

for x in range(0, len(arr)):
    for y in range(0, len(Probability)):
        if arr[x] == Probability[y]:
            Sorted_Sequence_of_Country.append(y)


print("\nCountries Ranking:")

for x in range (0, len(Sorted_Sequence_of_Country)):
    print(x+1,'->', Countries[Sorted_Sequence_of_Country[x]])

#shows data in pie chart
def plotPie():
    mylabels = ["C1","C2","C3","C4","C5"]
    y = [Probability[0],Probability[1],Probability[2],Probability[3],Probability[4]]
    plt.pie(y, labels=mylabels, explode=[0, 0.2, 0, 0, 0], shadow=True, autopct=lambda p: '{:.2f}%'.format(p), startangle = 180)
    plt.title("Probability of Selecting Country to Expand Business")
    plt.show()

plotPie()
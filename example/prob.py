from matplotlib import pyplot as plt
from django.shortcuts import render
import base64
from io import BytesIO
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

def getMax(array_A):
    max = array_A[0]
    for i in range(len(array_A)):
        if array_A[i] > max:
            max = array_A[i]

    return max

def get_prob(request):
    ctx = {}
    if request.POST:
        r_dict = request.POST
        print(request.POST)
        countries = [r_dict['n1'],
                     r_dict['n2'],
                     r_dict['n3'],
                     r_dict['n4'],
                     r_dict['n5'],
                     ]

        scores = [
            r_dict['s1'],
            r_dict['s2'],
            r_dict['s3'],
            r_dict['s4'],
            r_dict['s5'],
        ]

        scores = [float(s) for s in scores]

        costs = [
            r_dict['c1'],
            r_dict['c2'],
            r_dict['c3'],
            r_dict['c4'],
            r_dict['c5']
        ]

        costs = [float(c) for c in costs]

        n = 5
        total_score = 0
        total_cost = 0
        probability = []
        for score in scores:
            total_score += score

        for cost in costs:
            total_cost += cost

        for i in range(n):
            p = scores[i] / total_score * (1 - (costs[i]) / total_cost)
            probability.append(p)
            ctx[f"p{i + 1}"] =f"{p:.5f}"

        arr = probability.copy()
        shellSort(arr, n)

        sorted_sequence_of_country = []
        for x in range(n):
            for y in range(n):
                if arr[x] == probability[y]:
                    sorted_sequence_of_country.append(y)

        for i in range(n):
            ctx[f"r{i + 1}"] = sorted_sequence_of_country[i] + 1

        print(probability)
        print(scores)
        print(costs)
        print(probability)
        print(countries)

        plotPie(countries, probability)

    return render(request, "app/prob.html", ctx)

def plotPie(countries, probability):
    prob_sum = 0
    for p in probability:
        prob_sum += p
    probability = [p /prob_sum for p in probability]
    fig = plt.figure()
    plt.pie(probability, labels=countries, explode=[0, 0, 0.2, 0, 0], shadow=True, autopct=lambda p: '{:.2f}%'.format(p), startangle = 180)
    plt.title("Probability of Selecting Country to Expand Business")
    plt.legend()
    plt.savefig("pchart.png")

    # save image to html

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    html = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)

    with open('templates/app/pchart.html', 'w') as f:
        f.write(html)
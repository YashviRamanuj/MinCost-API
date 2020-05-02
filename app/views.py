from .serializers import OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def cpd(n):  # cost per distance
    if n>5:
        ans=10 + 8*(int( n/5 ))
    elif n == 0:
        ans = 0
    else:
        ans = 10
    return ans


def mincost(arr):  #minimum cost
    w1 = 3*arr[0] + 2*arr[1] + 8*arr[2]
    w2 = 12*arr[3] + 25*arr[4] + 15*arr[5]
    w3 = 0.5*arr[6] + 1*arr[7] + 2*arr[8]

    if w2 == 0:
        if w3 == 0:
            if w1 != 0: # 1 0 0
                cost = 3*cpd(w1)
            else:  # 0 0 0
                cost = 0
        elif w1 == 0:  # 0 0 1
            cost = 2*cpd(w3)
        else:  #1 0 1
            cost = 3* cpd(w1) + 2*10 + 2*cpd(w3)

    elif w1 == 0:
        if w3 == 0:  # 0 1 0
            cost = 2.5*cpd(w2)
        else:  # 0 1 1
            cost1 = 3*cpd(w2) + 2*cpd(w2 + w3)  #c2-c3-l1
            cost2 = 3*cpd(w2) + 2*10 + 2*cpd(w3) #c2-l1-c3-l1
            cost =  min(cost1,cost2)

    elif w3==0:  # 1 1 0
        cost1 = 4*cpd(w1) + 2.5*cpd(w1+w2) #c1-c2-l1
        cost2 = 3*cpd(w1) + 2.5*10 + 2.5*cpd(w2) #c1-l1-c2-l1
        cost = min(cost1, cost2)
    else:  # 1 1 1
        cost1 = 4*cpd(w1) + 3*cpd(w2+w1) + 2*cpd(w1+w2+w3)   #c1-c2-c3-l1
        cost1 = min(cost1, 4*cpd(w1) + 2.5*cpd(w2+w1) + 2*10 + 2*cpd(w3)) # c1-c2-l1-c3-l1
        cost1 = min(cost1, 3*cpd(w1) + 2.5*10 + 3*cpd(w2) + 2*cpd(w2+w3))  # c1-l1-c2-c3-l1
        cost1 = min(cost1, 3*cpd(w1) + 2*10 + 3*cpd(w3) + 2.5*cpd(w2+w3))  # c1-l1-c3-c2-l1
        cost1 = min(cost1, 3*cpd(w1) + 2.5*10 + 2.5*cpd(w2) + 2*10 + 2*cpd(w3)) # c1-l1-c2-l1-c3-l1
        cost1 = min(cost1, 4*cpd(w2) + 3*cpd(w2+w1) + 2*10 + 2*cpd(w3))  # c2-c1-l1-c3-l1
        cost1 = min(cost1, 3*cpd(w2) + 2*cpd(w2+w3) + 3*10 + 3*cpd(w1))  #c2-c3-l1-c1-l1
        cost1 = min(cost1, 2*cpd(w3) + 3*10 + 4*cpd(w1) + 2.5*cpd(w2+w1))  # c3-l1-c1-c2-l1
        cost1 = min(cost1, 3*cpd(w3) + 2.5*cpd(w2+w3) + 3*10 + 3*cpd(w1))  # c3-c2-l1-c1-l1
        
        cost = cost1

    return float(cost)


@api_view(http_method_names=["POST"])
def MinCost(request):
    item_serializer = OrderSerializer(data=request.data)
    item_serializer.is_valid(raise_exception=True)
    arr = item_serializer.data['order']   # var 'arr' is list of quantity for the order
    cost = mincost(arr)
    return Response(cost)

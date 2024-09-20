def knapsack_recursive(weight, value, capacity, n):
    if n == 0 :
          return 0
    if capacity == 0:
          return 0
 
    if (weight[n-1]>capacity):
        return knapsack_recursive(weight, value, capacity ,n-1)
    else:
        return max(
             value[n-1]+knapsack_recursive(weight, value,capacity-weight[n-1], n-1),knapsack_recursive(weight,value,capacity,n-1))



def main():
    weights, values = [1, 3, 4, 5], [1, 4, 5, 7]
    capacity, n = 7, len(weights)
    result = knapsack_recursive(weights, values, capacity, n)
    print(result)  # Output: 9 because of weights four and five with value 5 and 7


if __name__ == '__main__':
    main()

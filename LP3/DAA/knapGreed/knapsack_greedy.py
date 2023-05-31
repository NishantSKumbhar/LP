#Fractional Knapsack - Greedy Method - Coding

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
def fractionalKnapsack(W, arr):
    
    #sorting the array, according to P/W ratio
    arr.sort(key=lambda x:(x.value/x.weight), reverse=True)
    
    #Storing Final value
    finalvalue = 0.0
    
    #Looping through the items
    for item in arr:
        if item.weight<=W:
            W -= item.weight
            finalvalue += item.value
            
        else:
            finalvalue += item.value * W/item.weight
            break
    
    # Returning final value
    return finalvalue
            
#driver code
if __name__ == "__main__":
    
    W = 50
    arr = [Item(60,10), Item(100,20), Item(120,30)]
    
    #Function Calling
    max_val = fractionalKnapsack(W,arr)
    
    #Printing Result
    print(max_val)

#Time Complexity: O(nlogn)
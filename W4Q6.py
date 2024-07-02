# Define a custom check function
def customCheck(P):
    A = 0
    B = False
    Flag = False
    i = 1
    
    while i <= len(P):
        if P[i-1].lower() in 'bcdfghjklmnpqrstvwxyz':  # Check if the letter is a consonant
            if B:
                A = 1
            B = True
        else:
            B = False
        i += 1
    
    if A == 1:
        Flag = True
    
    return Flag

# Main procedure
def main():
    table1 = ["apppe", "assse", "immme", "uhhhho"]  # Placeholder for the actual "Words" dataset
    table2 = []
    table3 = []
    
    count = 0
    while table1:
        X = table1.pop(0)
        table2.append(X)
        
        while table1:
            Y = table1.pop(0)
            if customCheck(X) and customCheck(Y):
                count += 1
            table3.append(Y)
        
        table1.extend(table3)
        table3.clear()
    
    print("Count:", count)

if __name__ == "__main__":
    main()

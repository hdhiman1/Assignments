import pandas as pd

# Load the dataset from the provided PDF file
data = {
    "CardNo": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    "Name": ["Bhuvanesh", "Harish", "Shashank", "Rida", "Ritika", "Akshaya", "Sameer", "Aditya", "Surya", "Clarence", 
             "Kavya", "Rahul", "Srinidhi", "Gopi", "Sophia", "Goutami", "Tauseef", "Arshad", "Abirami", "Vetrivel", 
             "Kalyan", "Monika", "Priya", "Deepika", "Siddharth", "Geeta", "JK", "Jagan", "Nisha", "Naveen"],
    "Gender": ["M", "M", "M", "F", "F", "F", "M", "M", "M", "M", 
               "F", "M", "F", "M", "F", "F", "M", "M", "F", "M", 
               "M", "F", "F", "F", "M", "F", "M", "M", "F", "M"],
    "DateOfBirth": ["7 Nov", "3 Jun", "4 Jan", "5 May", "17 Nov", "8 Feb", "23 Mar", "15 Mar", "28 Feb", "6 Dec", 
                    "12 Jan", "30 Apr", "14 Jan", "6 May", "23 July", "22 Sep", "30 Dec", "14 Dec", "9 Oct", "30 Aug", 
                    "17 Sep", "15 Mar", "17 Jul", "13 May", "26 Dec", "16 May", "22 Jul", "4 Mar", "10 Sep", "13 Oct"],
    "CityTown": ["Erode", "Salem", "Chennai", "Chennai", "Madurai", "Chennai", "Ambur", "Vellore", "Bengaluru", "Bengaluru", 
                 "Chennai", "Bengaluru", "Chennai", "Madurai", "Trichy", "Theni", "Trichy", "Chennai", "Erode", "Trichy", 
                 "Vellore", "Bengaluru", "Nagercoil", "Bengaluru", "Madurai", "Chennai", "Chennai", "Madurai", "Madurai", "Vellore"],
    "Mathematics": [68, 62, 57, 42, 87, 71, 81, 84, 74, 63, 64, 97, 52, 65, 89, 76, 87, 62, 72, 56, 93, 78, 62, 97, 44, 87, 74, 81, 74, 72],
    "Physics": [64, 45, 54, 53, 64, 92, 82, 92, 64, 88, 72, 92, 64, 73, 62, 58, 86, 81, 92, 78, 68, 69, 62, 91, 72, 75, 71, 76, 83, 66],
    "Chemistry": [78, 91, 77, 78, 89, 84, 87, 76, 51, 73, 68, 92, 71, 89, 93, 90, 43, 67, 97, 62, 91, 74, 57, 88, 58, 92, 82, 52, 83, 81],
    "Total": [210, 198, 188, 173, 240, 247, 250, 252, 189, 224, 204, 281, 187, 227, 244, 224, 216, 210, 261, 196, 252, 221, 181, 276, 174, 254, 227, 209, 240, 219]
}

df = pd.DataFrame(data)

# Step 1: Arrange all cards in a single pile called Pile 1
pile1 = df.to_dict('records')
pile2 = []

# Step 2: Initialize variables
A = B = C = D = 0
Y = 100
X = None

# Step 4: Iterate over Pile 1
while pile1:
    # Step 5: Read the top card in Pile 1
    card = pile1.pop(0)
    
    # Step 6-9: Process the card based on the Town/City
    if card['CityTown'] == "Chennai":
        A += 1
        if A < Y:
            Y = A
            X = "Chennai"
    elif card['CityTown'] == "Bengaluru":
        B += 1
        if B < Y:
            Y = B
            X = "Bengaluru"
    elif card['CityTown'] == "Madurai":
        C += 1
        if C < Y:
            Y = C
            X = "Madurai"
    elif card['CityTown'] == "Vellore":
        D += 1
        if D < Y:
            Y = D
            X = "Vellore"
    
    # Step 10: Move the card to Pile 2
    pile2.append(card)

# Output the result
print(f"The variable X is: {X}")

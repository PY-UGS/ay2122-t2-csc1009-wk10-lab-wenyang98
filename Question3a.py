module  = input("Enter a module code: ") #input module code
switch = { #use of dictionary for switch case

    "CSC1006": "Mathematics 2",
    "CSC1007": "Operating Systems",
    "CSC1008": "Data Structures and Algorithms",
    "CSC1009": "OOP",
    "CSC1010": "Computer Networks"
}
print(switch.get(module ,"Invalid Module Code!")) #print out which module
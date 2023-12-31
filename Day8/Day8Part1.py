with open("InputDay8.txt","r") as input_file:
    count = 0
    directions = ""
    nodes = {}
    start_direction = ""
    for line in input_file:
        line = line.strip()
        if count == 0:
            #read in the direction instructions
            directions = line
            print(directions)
        if line != "" and count > 0:
            #this is a node 
            node,children = line.split(" = ")
         
            children = children[1:len(children)-1].split(", ")
            
            print("==New Node==")
            print(f"parent node of {node}")
            print(f"left node of {children[0]}, right node of {children[1]}")
            print("==End of Node==")
            nodes[node] = {"L":children[0],"R":children[1]}
        count += 1
    current_node = "AAA"
    nodes_traveled = 0
    while current_node != "ZZZ":
        
        for direction in directions:
            
            current_node = nodes[current_node][direction]
            
            nodes_traveled += 1
            if current_node == "ZZZ":
                print("quick test")
                break
    print("==Finished Traveling==")
    print(f"arrived at node {current_node}")
    print(f"it took {nodes_traveled}")
print("Email Duplicate Remover")

DELIMITER = ":"
OUTPUT = "output.txt" #this will write a new file
INPUT = "list.txt"

emails_seen = set() # holds the full line
with open(OUTPUT, "w", errors="ignore") as output_file: #ignore errors
    for each_line in open(INPUT, "r"):
        if DELIMITER in each_line: #check if the line contains the delimiter
            email = each_line.lower().split(DELIMITER)[0] #split into email & password
            passw = each_line.strip().split(DELIMITER)[1]
            # print(email)
            
            if email not in emails_seen: # check if only email is a duplicate
                output_file.write(email + DELIMITER + passw + "\n") #write the whole new line
                emails_seen.add(email) #add email to the set

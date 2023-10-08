# Initialize the initial clause
initial_clause = ["~p|q", "~q|r", "~r|s", "p", "~p|~s"]
# target_clause = "~p|~s"
proof_steps = []

def NegateClause(alpha):
    negated_clause = ""
    temp = alpha.split('|')

    for i in range(0, len(temp)):
        if len(temp[i]) == 1:
            temp[i] = '~' + temp[i]
        else:
            temp[i] = temp[i][1]

        if i != len(temp) - 1:
            negated_clause += temp[i] + '|'
        else:
            negated_clause += temp[i]

    return negated_clause

def PL_Resolve(C1, C2):
    new_clause = []
    temp_clause = []

    list_C1 = C1.split('|')
    list_C2 = C2.split('|')

    for i in list_C1:
        for j in list_C2:
            if i == NegateClause(j):
                temp_C1 = list_C1.copy()
                temp_C2 = list_C2.copy()
                temp_C1.remove(i)
                temp_C2.remove(j)

                if i[0] == '~':
                    temp_clause.extend(temp_C2)
                    temp_clause.extend(temp_C1)
                else:
                    temp_clause.extend(temp_C1)
                    temp_clause.extend(temp_C2)

                clause = '|'.join(temp_clause)
                new_clause.append(clause)

    return new_clause

def RobinsonAlgorithm(clauses):
    resolvents = []
    while True:
        new_clauses = []
        to_remove = []
        has_resolution = False
        for i in range(len(clauses) - 1):
            for j in range(i + 1, len(clauses)):
                # j = clauses[i + 1]
                resolvents = PL_Resolve(clauses[i], clauses[j])
                    # if target in resolvents:
                    #     print("Tìm thấy mục tiêu. Biểu thức là đúng.")
                    #     return
                if resolvents:
                    has_resolution = True
                    new_clauses.extend(resolvents)

                    clauses.extend(resolvents)
                    # clauses.remove(clauses[i])
                    # clauses.remove(clauses[j])
                    to_remove.extend(clauses[i])
                    to_remove.extend(clauses[j])
                    proof_steps.extend(clauses)
            #         break
            # if target in new_clauses:
            #     break
        if not clauses:
            print("Không thể thêm các mệnh đề mới. Biểu thức không đúng.")
            return
        print("Tìm thấy mục tiêu. Biểu thức là đúng.")
        return
        # clauses.extend(new_clauses)

# Apply the Robinson algorithm
RobinsonAlgorithm(initial_clause)


# Write the proof steps to a text file
with open("proof_steps.txt", "w") as file:
    for step in proof_steps:
        file.write(step + "\n")
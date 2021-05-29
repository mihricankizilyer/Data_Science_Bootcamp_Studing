# Write the function to return 2 groups in a single list.

employees = ["Mary","Jane","Jessi","Ella","Tom","Jordan"]
def app(employees):
    category = [[],[]]
    for index, employee in enumerate(employess):
        if index % 2 == 0:
            category[0].append(employee)
        else:
            category[1].append(employee)
        return category
app(employees)
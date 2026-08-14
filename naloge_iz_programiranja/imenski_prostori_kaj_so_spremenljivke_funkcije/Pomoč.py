obstojece = [(2, 6), (10, 14), (17, 22)]
nove = [(7,8), (15, 16), (18, 25)]

def sovpad(ovira1, ovira2):
    return ovira2[0] <= ovira1[0] <= ovira2[1] or ovira1[0] <= ovira2[0] <= ovira1[1]

def odstrani_odvecne(obstojece, dodatne):
    ovire = []
    for ovira_o, ovira_d in zip(obstojece, dodatne):
        if not sovpad(ovira_o, ovira_d):
            ovire.append(ovira_d)
    obstojece.append(ovire)

print(odstrani_odvecne(obstojece, nove))
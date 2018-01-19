transportData = open('transport_data.csv', 'r')
newData = open('transport_newdata.csv', 'w')
questionsData =open('transport_quest.csv', 'w')
for line in transportData.readlines():    
    inf=line
    symKey=inf[-2]
    if symKey.isdigit() or symKey=='?':               
        if symKey=='?':
            questionsData.write(str(inf[:-3]) + '\n')
        else:
            newData.write(str(inf))
transportData.close()
questionsData.close()
newData.close()

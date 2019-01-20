import re
file = open('uri.csv' , 'r')
lc = [i for i in file]
file.close()
fileclean1 = [i.strip().split('\n') for i in lc]
 
#remove ['']
fileclean2 = [fileclean1[i] for i in range(len(fileclean1)) if i%2==0]
fileclean3 = [[fileclean2[i][0].replace("\\xe2","").replace("\\x80","").replace("\\x99","").replace("\\xf0","").replace("\\x9f","")] for i in range(len(fileclean2))]
 
# replace @ and # and <
fileclean4 = [[fileclean3[i][0].replace("@","").replace("#","").replace("<","")] for i in range(len(fileclean3))]
 
 
# ignore http and Retweets
fileclean5 = [[fileclean4[i][0]] for i in range(len(fileclean4)) if fileclean4[i][0].find("http") == -1]
fileclean6 = [[fileclean5[i][0]] for i in range(len(fileclean5)) if fileclean5[i][0].find("RT") == -1]
 
 
# remove duplicates
 
fileclean7 = [fileclean6[i] for i in range(len(fileclean6)) if i == 0 or fileclean6[i] != fileclean6[i-1]]
#fileclean7 = [ list(x) for x in set(tuple(x) for x in fileclean6)]
 
#further cleaning
 
fileclean8 = [[fileclean7[i][0].replace('b"',"").replace("b'","").replace("\\","").replace("'","").replace('"',"")] for i in range(len(fileclean7))]
 
#
fileclean9 = [[re.sub('[!@#$:).;,?&]', '', fileclean8[i][0].lower())] for i in range(len(fileclean8))]
fileclean10 = [[ re.sub(' ', ' ', fileclean9[i][0])] for i in range(len(fileclean9))]
 
 
 
filewrite= open('cleanedfile.csv','w')
filewrite.writelines('text'+'\n')
[filewrite.writelines(str(fileclean10[i])[2:-2]+'\n') for i in range(len(fileclean10))]
filewrite.close()
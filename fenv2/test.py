import requests
f = open("data.txt", "w")
books = [["How-to-get-a-good-grade-in-DOS-in-20-minutes-a-day" , "distributed systems" , "20" , "7","1"],["RPCs for Dummies","distributed systems","25","4","2"],["Xen and the Art of Surviving Graduate School","graduate school","10","8", "3"],["Cooking for the Impatient Graduate Student","graduate school","40","3", "4"],["How to finish Project 3 on time" , "distributed systems" , "22" , "7","1"],["Why theory classes are so hard" , "graduate school" , "20" , "7","1"],["Spring in the Pioneer Valley" , "graduate school" , "20" , "7","1"]]

for i in range(7):
 for j in range(5):
     f.write(books[i][j]+"\n")

#Base=" http://127.0.0.1:5000/"
#response= requests.post(Base+"buy/1")
#print("request is post")
#print(response.json())
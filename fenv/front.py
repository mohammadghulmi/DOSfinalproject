import requests

catalog = [" http://127.0.0.1:4000/", " http://127.0.0.1:6000/", " http://127.0.0.1:9000/"]
order = [" http://127.0.0.1:5000/", " http://127.0.0.1:7000/", " http://127.0.0.1:11000/"]
cache = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""]];


global x
x=0
global r
r=0
def buy(id):

    if checkcache(id) == True:
        print(getcache(id))
    else:
            while (True):
                res = ""
                try:
                    res = requests.post(order[0] + "buy/" + id)
                    if res.json():
                        break
                except Exception as e:
                    r = r + 1
                    res = requests.post(order[1] + "buy/" + id)
                    if res.json():
                        break
                    print(r)

                except:
                    r = r + 1
                    res = requests.post(order[2] + "buy/" + id)
                    if res.json():
                        break


            r = r + 1
            print(res.json())
            str = res.json()
            r = r + 1
            addcache(str, id)



def search(topic):

    while (True):
        res = ""
        try:
            res = requests.get(catalog[0] + "search/" + topic)
            if res.json():
                break
        except Exception as e:

            res = requests.get(catalog[1] + "search/" + topic)
            if res.json():
                break
            print(r)

        except:

            res = requests.get(catalog[2] + "search/" + topic)
            if res.json():
                break
            print(r)



    print(res.json())






def lookup(id):
    global r
    if checkcache(id) == True:
        print(getcache(id))
    else:
        while(True):
            res = ""
            try:
                res = requests.get(catalog[0] + "lookup/" + id)
                if res.json():

                    break
            except Exception as e:
                r = r + 1
                res = requests.get(catalog[1] + "lookup/" + id)
                if res.json():

                    break
                print(r)

            except:
                r = r + 1
                res = requests.get(catalog[2] + "lookup/" + id)
                if res.json():

                    break
                print(r)


        r = r + 1


        print(res.json())
        str = res.json()
        r = r + 1
        addcache(str, id)



def addcache(str, id):
    global x
    cache[x % 10][0] = str
    cache[x % 10][1] = id
    x=x+1
    print(x)


def getcache(id):
    j = 0
    for j in range(10):
        if cache[j][1] == str(id):
            return cache[j][0]


def checkcache(id):
    j = 0
    for j in range(10):
        if cache[j][1] == str(id):
            return True
    return False


def update(id):
    j = 0
    for j in range(4):
        try:
            res = requests.put(catalog + "update/" + id)
        finally:
            continue


while True:

    val = input("enter s to search l to lookup b to buy")
    if val == "b":
        while True:
            val = input("enter the product number")
            if val.isdecimal():
                buy(val)
                break
            else:
                print("enter a number")
    elif val == "l":
        while True:
            val = input("enter the product number")
            if val.isdecimal():
                lookup(val)
                break
            else:
                print("enter a number")
    elif val == "s":
        val = input("enter a topic")
        search(val)
    else:
        print("enter a valid input")

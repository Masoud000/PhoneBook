#############################
###  Programmer : Masoud  ###
#############################


phonebook = {}

def print_header():
    print 
    print ("#" * 40).center(80," ")
    print "####   PhoneBook Write By Masoud   #####".center(80," ")
    print ("#" * 40).center(80," ")
    print 

def assign(name,num):
    global phonebook
    if name.lower() not in phonebook or name.title() not in phonebook:
        tmp = {name : num}
        phonebook.update(tmp)
        return 1
    return 0
def prip(name):
    global phonebook
    if name.lower() in phonebook:
        print "%-20s%s" % ("Name","Number")
        print "%-20s%s" % (name.title(),phonebook[name.lower()])
    elif name.title() in phonebook:
        print "%-20s%s" % ("Name","Number")
        print "%-20s%s" % (name.title(),phonebook[name.title()])
    else:
        print "This Person Not Found!!!"
    
def print_pb():
    global phonebook
    print "%-20s%s" % ("Name","Number")
    print "=" * 40
    for i in phonebook:
        print "%-20s%s" % (i,phonebook[i])

def sf(s):
    return tuple(s.split(":"))

def sync():
    global phonebook
    f = open("data.inf")
    inf = f.read()
    f.close()
    if ":" in inf:
        inf = inf.split("\n")
        inf = map(sf,inf)
        del inf[len(inf)-1]
        inf = dict(inf)
        phonebook.update(inf)
        return 1
    return 0

def total_sync():
    global phonebook
    f = open("data.inf","w")
    inf = ""
    for i in phonebook:
        tmp = "%s:%s\n" % (i,phonebook[i])
        inf = inf + tmp
    f.write(inf)
    f.close()
            

def html_generator():
    global phonebook
    web = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PhoneBook</title>
    <style>
        table
        {
            border : 2px solid yellow;
            border-radius : 10px;
            padding : 20px;
            border-spacing : 50px 10px;
        }
        td
        {
            border : 1px solid blue;
            padding : 10px 20px;
            border-radius : 5px;
            margin : 10px;
        }
        tr:nth-child(even)
        {
            color : #1dd3cc;
        }
            
    </style>
</head>
<body>
    <table>
    <tr><td>Name</td><td>Number</td></tr>
    %s
    </table>
    <p>This page was written by MS</p>
</body>
</html>

"""
    text = ""
    for i in phonebook:
        tmp = "<tr><td>%s</td><td>%s</td></tr>\n"
        tmp = tmp % (i,phonebook[i])
        text = text + tmp
    web = web % text
    f = open("phonebook.html","w")
    f.write(web)
    f.close()
    


def menu():
    print """
***Wellcome to this phonebook program***
\tFor selecting items please enter it's number :
\t\t1.print phonebook
\t\t2.add person to phonebook
\t\t3.delete person from phonebook
\t\t4.view person from phonebook
\t\t5.Generate html file
\t\t6.sync
\t\t7.exit
"""


def main():
    global phonebook
    print_header()
    sync()
    menu()
    while True:
        command = raw_input()
        if command == '1':
            print_pb()
        elif command == '2':
            name = raw_input("Enter Name : ")
            num = raw_input("Enter Number : ")
            if assign(name,num):
                print "Successfully add it!"
            else:
                print "Already exists!!!"

        elif command == '3':
            name = raw_input("Enter Name : ")
            if name.lower() in phonebook:
                del phonebook[name.lower()]
                print "it deleted"
            elif name.title() in phonebook:
                del phonebook[name.title()]
                print "it deleted"
            elif name in phonebook:
                del phonebook[name]
                print "it deleted"
            else:
                print "this is not exists!!!"
        elif command == '4':
            name = raw_input("Enter Name : ")
            prip(name)
        elif command == '5':
            html_generator()
            print "Generated successfully!"
        elif command == '6':
            total_sync()
            print "Synchronized!!!"
        elif command == '7':
            print "GoodBye"
            break
        else:
            print "Please Enter Right command !!!"
        

main()



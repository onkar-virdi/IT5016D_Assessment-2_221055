class Ticket:
    def __init__(self, creator, staffid, emailaddress, description, number):
        self.number = number
        self.creator = creator
        self.staffid = staffid
        self.emailAddress = emailaddress
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "open"
        self.password = ''


run = True

tickets = []
closedtickets = []

r = 1

while run:
    command = input("""    N for new ticket
    G to get a ticket
    Q for number of tickets
    O for open tickets
    R for resolved tickets
    """)
    if command == "N":
        desc = input("Write in format: creator staffID email description: ").split(" ")
        tickets.append(Ticket(desc[0], desc[1], desc[2], " ".join(desc[3:]), str(r)))
        r += 1
        if "password change" in tickets[-1].description.lower():
            tickets[-1].password = tickets[-1].staffid[0:2] + tickets[-1].creator[0:3]
            print("New password: "+tickets[-1].password)
            tickets[-1].status = "closed"
            tickets[-1].response = 'Password changed successfully'
            closedtickets.append(tickets.pop(-1))
            r -= 1

    elif command == "G":
        num = input("Ticket number: ")
        found = False
        for i in tickets:
            if i.number == num:
                target = i
                found = True
        if not found:
            for i in closedtickets:
                if i.number == num:
                    target = i
                    found = True
                    tickets.append(closedtickets.pop(closedtickets.index(i)))
        try:
            print(target.number+"\n"+target.staffid+"\n"+target.creator+"\n"+target.emailAddress+"\n"+target.description+"\n"+target.status+"\n"+target.response+"\n")
        except NameError:
            print("invalid ticket number")
        target.response = input('Solution for problem:')
        target.status = 'closed'
        closedtickets.append(target)
        tickets.remove(target)

    elif command == "Q":
        print(len(tickets)+len(closedtickets))

    elif command == "O":
        print(len(tickets))
    elif command == "R":
        print(len(closedtickets))
    else:
        print("Invalid Command")

#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ticketCache = {}
    route = []
    for t in tickets:
        if t.source == "NONE":
            ticketCache['start'] =  t.destination
        else: 
            ticketCache[t.source] =  t.destination
    currentTicket = ticketCache['start']
    route.append(currentTicket)
    while  currentTicket in ticketCache:
        route.append(ticketCache[currentTicket])
        currentTicket = ticketCache[currentTicket]
    return route

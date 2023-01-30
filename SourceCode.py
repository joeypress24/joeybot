from array import *
import copy
from hashlib import new
import json
import sys

# world class to implement value iteration
class World:

    def __init__(self, worldName):
        self.worldName = worldName

        f = open(worldName)
        inputDict = json.load(f)

        # read in values from json file
        self.shape = inputDict.get("shape") # ex: [3, 4]
        self.gamma = inputDict.get("gamma") # ex: 0.9
        self.rl = inputDict.get("rl") # ex: [[[0, 3], 1], [[1, 3], -1]]
        self.tl = inputDict.get("tl") # ex: [[0, 3], [1, 3]]
        self.bl = inputDict.get("bl") # ex: [[1, 1]]

        #self.values = 2D array of size shape set to all 0's
        self.values = [[0 for i in range(self.shape[1])] for j in range(self.shape[0])]

        #self.policy = 2D array of size shape set to all N's
        self.policy = [['N' for i in range(self.shape[1])] for j in range(self.shape[0])]

        for i in self.tl:
            self.policy[i[0]][i[1]] = '.'
        for i in self.bl:
            self.policy[i[0]][i[1]] = '.'

    # run value iteration i times
    def valueIteration(self, i):

        #empty values array of same shape
        # newValues = self.values.copy()

        global num #global for debugging purposes, helps know what iteration we're on
        for num in range(0, i):
            newValues = copy.deepcopy(self.values)

            #loop through it first, using only values
            for r in range(0, self.shape[0]):
                for c in range(0, self.shape[1]):

                    foo = True
                    for i in self.bl:
                        if [r,c] == i:
                            foo = False
                    for i in self.tl:
                        if [r,c] == i:
                            foo = False
                    if(foo == True): #if not in terminating state or blocked state
                        valN = World.calcQ(self, r, c, 'N')
                        valE = World.calcQ(self, r, c, 'E')
                        valS = World.calcQ(self, r, c, 'S')
                        valW = World.calcQ(self, r, c, 'W')

                        maxVal = [(valN, 'N'), (valE, 'E'), (valS, 'S'), (valW, 'W')]
                        maxVal.sort(key = lambda x : x[0])
                        maxVal.reverse()

                        newValues[r][c] = maxVal[0][0]

            # update the values array so we can figure out policy
            self.values = newValues # update values

            # calculate the policy based on the new values array
            for r in range(0, self.shape[0]):
                for c in range(0, self.shape[1]):

                    foo = True
                    for i in self.bl:
                        if [r,c] == i:
                            foo = False
                    for i in self.tl:
                        if [r,c] == i:
                            foo = False

                    if(foo == True): #if not in terminating state or blocked state
                        valN = World.calcQ(self, r, c, 'N')
                        valE = World.calcQ(self, r, c, 'E')
                        valS = World.calcQ(self, r, c, 'S')
                        valW = World.calcQ(self, r, c, 'W')

                        maxVal = [(valN, 'N'), (valE, 'E'), (valS, 'S'), (valW, 'W')]
                        maxVal.sort(key = lambda x : x[0])
                        maxVal.reverse()

                        tiedElements = []
                        tiedElements.append(maxVal[0][1])
                        for i in maxVal:
                            if i[0] == maxVal[0][0] and i[1] != maxVal[0][1]:
                                tiedElements.append(i[1])

                        if(len(tiedElements) > 1): #there is a tie in this case
                            #breaking the tie
                            if('N' in tiedElements):
                                self.policy[r][c] = 'N'
                            elif('S' in tiedElements):
                                self.policy[r][c] = 'S'
                            elif('E' in tiedElements):
                                self.policy[r][c] = 'E'
                            else: #west
                                self.policy[r][c] = 'W'
                        else:
                            self.policy[r][c] = tiedElements[0]


    def calcQ(self, r, c, direction):
        # Q*(s,a) = sum T(s,a,s') [R(s,a,s') + gamma* V*(s')]

        newR, newC = World.getNewState(self, r, c, direction)
        reward = 0
        for i in self.rl:
            if(i[0] == [newR, newC]):
                reward = i[1]

        newValue = .8*(reward + self.gamma*self.values[newR][newC])

        #there are two main cases for direction
        if(direction == 'N' or direction == 'S'):
            newR1, newC1 = World.getNewState(self, r, c, 'E')
            newR2, newC2 = World.getNewState(self, r, c, 'W')
            reward1 = 0
            reward2 = 0
            # get rewards for each direction
            for i in self.rl:
                if(i[0] == [newR1, newC1]):
                    reward1 = i[1]
            for i in self.rl:
                if(i[0] == [newR2, newC2]):
                    reward2 = i[1]
            # update the newValue variable
            newValue += .1*(reward1 + self.gamma*self.values[newR1][newC1])
            newValue += .1*(reward2 + self.gamma*self.values[newR2][newC2])
        elif(direction == 'E' or direction == 'W'):
            newR1, newC1 = World.getNewState(self, r, c, 'N')
            newR2, newC2 = World.getNewState(self, r, c, 'S')
            reward1 = 0
            reward2 = 0
            #get rewards for each direction
            for i in self.rl:
                if(i[0] == [newR1, newC1]):
                    reward1 = i[1]
            for i in self.rl:
                if(i[0] == [newR2, newC2]):
                    reward2 = i[1]
            # update the newValue variable
            newValue += .1*(reward1 + self.gamma*self.values[newR1][newC1])
            newValue += .1*(reward2 + self.gamma*self.values[newR2][newC2])

        return newValue


    # helper function that takes into consideration walls and blocked states
    def getNewState(self, r, c, direction):
        oldRow = r
        oldCol = c
        #make the change
        if(direction == 'N'):
            r = r -1
        if(direction == 'S'):
            r = r +1
        if(direction == 'E'):
            c = c + 1
        if(direction == 'W'):
            c = c - 1

        # at this point we have our "new" row and column value
        #now we check if our new position is valid
        #first check if it's out of bounds
        if(r < 0 or r > self.shape[0]-1 or c < 0 or c > self.shape[1]-1):
            return (oldRow, oldCol)

        # now we need to check if it's a blocked state
        for i in self.bl:
            if([r,c] == i):
                return (oldRow, oldCol)

        # if we made it here, then the new rol and col is valid
        return (r, c)




#helper function for ida*, performing limited DFS
def FLimitDFS(initialBoard, limit, heuristic):
    done = False
    # start with gigantic min
    min = sys.maxsize
    board = initialBoard
    list = [] #model of the stack
    goal = Board()
    global totalNodes
    totalNodes = 0 # keep track of # of nodes

    while(done is False):
        if(board.totalCost <= limit):
            if(board.__eq__(goal)): #isGoal(s)
                return board.moves
            successors = board.generateMoves()
            totalNodes +=1 # add to totalNodes when generateMoves() is called
            for i in successors: #loop through moves and add children to list
                #point successors back to board
                #make a deep copy of the board
                child = copy.deepcopy(board)
                child.moves.append(i)
                child.makeMove(i) #make the move
                #calculate the f-cost and store in child
                totalCost = len(child.moves) + heuristic(child)
                child.totalCost = totalCost

                #add this child to the list
                list.append(child)
        else:
            if(board.totalCost < min):
                min = board.totalCost #update the min if cost > limit

        try:
            board = list.pop()
            #totalNodes += 1
        except:
            done = True

    return min

#bulk logic of ida*
def idaStar(initialBoard, heuristic):
    limit = initialBoard.totalCost
    r = None # any number works here
    while(isinstance(r, list) == False): #if r is not a Board object
        r = FLimitDFS(initialBoard, limit, heuristic)
        if(isinstance(r, int) == True): # if r is an integer
            limit = r

    return r, totalNodes


    def aStar(initialBoard, heuristic):
    board = initialBoard #keeps track of our progress
    closed = dict() # dictionary is better than list for this purpose
    open = PriQue() # priority queue object to store open nodes
    goal = Board() # goal is always a default board
    totalNodes = 0 # keep track of # of nodes

    while(board.__ne__(goal)): #isNotGoal()
        #generate all possible moves in given state
        #add board to closed

        closed[board.key()] = True
        successors = board.generateMoves()
        #totalNodes += 1 # add to totalNodes when generateMoves() is called

        #loop through the list of generated moves
        for i in successors:
            #make a deep copy of the board
            child = copy.deepcopy(board)
            child.moves.append(i)
            child.makeMove(i) #make the move

            #calc the f-cost and store in child
            # length of moves[] in child == CURRENT DEPTH
            totalCost = len(child.moves) + heuristic(child)
            child.totalCost = totalCost

            if(child.key() not in closed):
                #add successors to open priority queue
                open.insert(child)
                #totalNodes+=1

        board = open.dequeue() #get the next (lowest cost) board

    #once finished, we need to return moves arr and # nodes
    #print("Nodes expanded: ", totalNodes)
    return (board.moves, totalNodes)

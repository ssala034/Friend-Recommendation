# Author: Shuaib Salad

import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]

    # YOUR CODE GOES HERE
    people=[]
    account=[]
    profile=[]
    user_id=0
    previous=[]
    
    for i in range(1,len(friends)):
        user_id=int(friends[i].split(' ')[0])
        t=int(friends[i].split(' ')[1])
        if user_id not in people:
            people.append(user_id)
        if t not in people:
            people.append(t)
    people.sort()
        
    for i in range(len(people)):
        account.clear()
        profile.clear()
        user_id = people[i]
        for j in range(1,len(friends)):
            if int(friends[j].split(' ')[0]) == user_id:
                profile.append(int(friends[j].split(' ')[1]))
            if int(friends[j].split(' ')[1]) ==user_id:
                profile.append(int(friends[j].split(' ')[0]))
            previous.append(user_id) 
            if user_id not in account:
                account.append(user_id) 
        account.append(profile[:])
        network.append(tuple(account))

    return network

#Helper function
def index_via_binary_search(network,user):
    '''
    (2Dlist, int)-> int
    Given a 2Dlist representing a friendship network and a user ID.
    The function returns the index of that user in that network.
    Preconditon: user ID is a positive number and the netwrok is sorted. 
    '''
    b=0
    e = len(network)-1
    while b<=e:
        mid= (b+e)//2
        a= network[mid][0]
        if user < a:
            e =mid-1
        elif user > a:
            b= mid+1
        else:
            return mid
    return -1

#Helper function
def combined_listsv2(list1,list2):
    '''
    Given two lists, the function returns a sorted list of all elements in
    list1 and list2.
    Precondition: list1 and list2 are sorted and both cannot be empty'''
    combined=[]
    a=len(list1)
    b=len(list2)
    i=0
    j=0
    while i<a and j<b:
        if list1[i]<list2[j]:
            combined.append(list1[i])
            i=i+1
        else:
            combined.append(list2[j])
            j=j+1
    if i<a:
        while i<a:
            combined.append(list1[i])
            i=i+1
    if j<b:
        while j<b:
            combined.append(list2[j])
            j=j+1
    
    return combined
    
def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    
    # YOUR CODE GOES HERE
    spot1=index_via_binary_search(network,user1)
    spot2=index_via_binary_search(network,user2)
    common_friend1 = network[spot1][1]
    common_friend2 = network[spot2][1]
    total_friends=combined_listsv2(common_friend1,common_friend2)

    t=len(total_friends)
    i=0
    while i<t-1:
        if total_friends[i]==total_friends[i+1]:
            common.append(total_friends[i])
            i=i+1
        i=i+1

    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE

    recommended = 0
    connections = []
    counter = 0
    mutual = 0
    for i in range(len(network)):
        if network[i][0] == user:
            connections = network[i][1]

    for i in range(len(network)):
        counter = 0
        if network[i][0] != int(user) and int(user) not in network[i][1]:
            for j in range(len(connections)):
                if connections[j] in network[i][1]:
                    counter = counter+ 1
            if counter > mutual:
                mutual = counter
                recommended = network[i][0]
            if counter == mutual:
                recommended = min(recommended, network[i][0])
               
    if mutual != 0:
        return recommended
    else:
        return None

def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    counter=0
    a=len(network)
    for i in range(a):
        if len(network[i][1])>=k:
            counter =counter +1
    return counter

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    counter=len(network[0][1])
    a=len(network)
    for i in range(a-1):
        if len(network[i+1][1])> counter:
            counter = len(network[i+1][1])
    return counter
    
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE
    most=maximum_num_friends(network)
    a=len(network)
    for i in range(a):
        if len(network[i][1])== most:
            max_friends.append(network[i][0])

    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
    counter1=0
    counter2=0
    a=len(network)
    for i in range(a):
        counter1=counter1+1
        counter2= counter2+ len(network[i][1])

    b= counter2/counter1
    return b
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE
    a=len(network)
    for i in range(a):
        if len(network[i][1])==(a-1):
            return True
    return False


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE
    flag=False
    while not flag:
        try:
            number= int(input("Enter an integer for a user ID:").strip())
            if index_via_binary_search(network,number)!=-1:
                ID=number
                flag=True
            else:
                print("That user ID does not exist. Try again.")
        except:
            print("That was not an integer. Please try again")
            
    return ID
    

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    

class SocialNetwork:
    def __init__(self):
        '''Constructor; initialize an empty social network
        '''
        self.users = {}

    def list_users(self):
        self.users.keys()
        userslist = list()
        for i in self.users.keys():
            userslist.append(i)
        return userslist

    def add_user(self, user):
        list_of_friends=[]
        self.users[user] = list_of_friends
        return

    def add_friend(self, user, friend):
        self.users[user].append(friend)
        return

    def get_friends(self, user):
        return self.users.get(user)

    def suggest_friend(self, user):
        jacardic = []
        for key in self.users:
            if not user == key:
                poop_list = self.users.get(user) + self.users.get(key)
                total_list = self.users.get(user) + self.users.get(key)
                total_list = set(total_list)
                total_list = list(total_list)
                similar = len(poop_list) - len(total_list)
                total = len(total_list)
                jacardic.append([similar, total])
            print(key)
            print(user)
            print(jacardic)
        list_percentage = []
        n = 0
        for i in jacardic:
            percentage = (jacardic[n][0]) / (jacardic[n][1])
            list_percentage.append(percentage)
            n += 1
        print(list_percentage)
        print(max(list_percentage))
        print(list(self.users.keys()))

            #list of alexs friend
            #go through list of alexs friend
            #compare to list of otherusers friends
            #make a mark everytime similar friend
            #get alexs values
        #get values of first of alexs friends
        #get values of second of alexs
        #add length of list of alexs friends and length of list of otherusers friends
        #subtract number of similar to give total
        #divide similar by total (last two steps)


        # '''Suggest a friend to the user
        #
        # See project specifications for details on this algorithm.
        #
        # Arguments:
        #     user (str): The username of the user to find a friend for
        #
        # Returns:
        #     str: The username of a new candidate friend for the user
        # '''
        pass  #FIXME

    def to_dot(self):
        result = []
        result.append('digraph {')
        result.append('    layout=neato')
        result.append('    overlap=scalexy')
        for user in self.list_users():
            for friend in self.get_friends(user):
                result.append('    "{}" -> "{}"'.format(user, friend))
        result.append('}')
        return '\n'.join(result)


def create_network_from_file(filename):
    '''Create a SocialNetwork from a saved file

    Arguments:
        filename (str): The name of the network file

    Returns:
        SocialNetwork: The SocialNetwork described by the file
    '''
    network = SocialNetwork()
    with open(filename) as fd:
        for line in fd.readlines():
            line = line.strip()
            users = line.split()
            network.add_user(users[0])
            for friend in users[1:]:
                network.add_friend(users[0], friend)
    return network


def main():
    network = create_network_from_file('simple.network.txt')
    print(network.to_dot())
    print(network.suggest_friend('francis'))


if __name__ == '__main__':
    main()
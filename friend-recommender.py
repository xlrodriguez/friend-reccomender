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
        self.users[user] = ''
        print(self.users)
        return

    def add_friend(self, user, friend):
        [user].append(friend)
        return

    def get_friends(self, user):
        self.users.get(user)
        pass

      # FIXME

    def suggest_friend(self, user):
        # for i in self.users:
            #nested loops


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
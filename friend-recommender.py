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
        list_of_friends = []
        self.users[user] = list_of_friends
        return

    def add_friend(self, user, friend):
        self.users[user].append(friend)
        return

    def get_friends(self, user):
        return self.users.get(user)

    def how_many_followers(self, user):
        num_followers = 0
        for key in self.users:
            if user in self.users.get(key):
                num_followers += 1
        return num_followers

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
        list_percentage = []
        n = 0
        for i in jacardic:
            percentage = (jacardic[n][0]) / (jacardic[n][1])
            list_percentage.append(percentage)
            n += 1
        name_sim_friend = self.return_name_of_similar_friend(list_percentage)
        return self.suggest_most_followed(name_sim_friend, user)

    def find_max_index(self, listz):
        for i, x in enumerate(listz):
            if x == (max(listz)):
                max_index = i
                return max_index

    def suggest_most_followed(self, name_sim_friend, user):
        list_followers = []
        for friend in self.users.get(name_sim_friend):
            list_followers.append(self.how_many_followers(friend))
        a = len(list_followers)
        while a != 0:
            most_followed = self.users.get(name_sim_friend)[self.find_max_index_pt_2(list_followers)]
            if most_followed in self.users.get(user):
                del list_followers[self.find_max_index_pt_2(list_followers)]
                a -= 1
            else:
                return most_followed

    def return_name_of_similar_friend(self, listz):
        user_list = list(self.users.keys())
        return user_list[self.find_max_index(listz)]

    def find_max_index_pt_2 (self, list_followers):
        for i, x in enumerate(list_followers):
            if x == (max(list_followers)):
                max_index_pt_2 = i
        return max_index_pt_2

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
    network = create_network_from_file('twitter.network.txt')
    print(network.to_dot())
    print(network.suggest_friend('GWtweets'))


if __name__ == '__main__':
    main()

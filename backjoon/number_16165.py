N, M = map(int, input().split())
teams = {}
members = {}

for i in range(N):
    team_name = input()
    team_member = int(input())
    teams[team_name] = []

    for j in range(team_member):
        name = input()
        teams[team_name].append(name)
        members[name] = team_name

'''
print(temas)

{'twice': ['jihyo', 'dahyeon', 'mina', 'momo', 'chaeyoung', 'jeongyeon', 'tzuyu', 'sana', 'nayeon'], 
'blackpink': ['jisu', 'lisa', 'rose', 'jenny'], 
'redvelvet': ['wendy', 'irene', 'seulgi', 'yeri', 'joy']}

'''
'''
print(members)

{'jihyo': 'twice', 'dahyeon': 'twice', 'mina': 'twice', 'momo': 'twice', 'chaeyoung': 'twice', 'jeongyeon': 'twice', 'tzuyu': 'twice', 'sana': 'twice', 'nayeon': 'twice', 
'jisu': 'blackpink', 'lisa': 'blackpink', 'rose': 'blackpink', 'jenny': 'blackpink', 
'wendy': 'redvelvet', 'irene': 'redvelvet', 'seulgi': 'redvelvet', 'yeri': 'redvelvet', 'joy': 'redvelvet'}
'''


for i in range(M):
    name = input()
    q = int(input())

    if q:
        print(members[name])
    else:
        for member in sorted(teams[name]):
            print(member)


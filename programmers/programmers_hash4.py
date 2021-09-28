'''
문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

'''

from collections import defaultdict
from operator import itemgetter

def solution(genres, plays):

    play_list_zip = list(zip(genres, plays))

    genre_play_dict = defaultdict(lambda: 0)
    # dictionary 같은 키 값이면 value값 더해주
    for category, count in play_list_zip:
        genre_play_dict[category] += count
    # itemgetter를 이용해서 리스트 정렬 (itemgetter(1) -> 배열 첫번째 기준으로 정렬하겠다)
    # genre_rank output -> ["pop", "classic"]
    genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), key=itemgetter(1), reverse=True)]
    # final_dict output -> {'classic': [(400, 0), (500, 2), (500, 3)], 'pop': [(600, 1), (2500, 4)]})
    final_dict = defaultdict(lambda: [])
    for i, genre_play_tuple in enumerate(zip(genres, plays)):
        final_dict[genre_play_tuple[0]].appeㅜnd((genre_play_tuple[1], i))

    answer = []
    '''
    output  (밑에 두개의 리스트가 동시에 나오는게 아니라 한줄씩 출력)
    [(2500, 4), (600, 1)]
    [(500, 2), (500, 3), (400, 0)]
    '''
    for genre in genre_rank:
        one_genre_list = sorted(final_dict[genre], key=itemgetter(0), reverse=True)
        if len(one_genre_list) > 1:
            answer.append(one_genre_list[0][1])
            answer.append(one_genre_list[1][1])

        else:
            answer.append(one_genre_list[0][1])

    print(answer)
    
    return answer


if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [400, 600, 500, 500, 2500]
    solution(genres, plays)
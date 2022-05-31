def solution(cacheSize, cities):
    answer = 0

    cache_list = list()

    for city in cities:
        city = city.lower()
        # Miss
        if city not in cache_list:

            if len(cache_list) < cacheSize:
                cache_list.append(city)
            elif cacheSize != 0:
                cache_list.pop(0)
                cache_list.append(city)

            answer += 5
        else:
            cache_list.pop(cache_list.index(city))
            cache_list.append(city)

            answer += 1

    return answer
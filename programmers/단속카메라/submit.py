def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = [routes[0][1]]

    for entry, exit in routes[1:]:
        if camera[-1] < entry:
            camera.append(exit)

    return len(camera)

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) # 2
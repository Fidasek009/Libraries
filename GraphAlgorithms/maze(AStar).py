from AStar import Maze


WALL = 'W'
PATH = 'P'
START = 'S'
FINISH = 'F'
FOUNDPATH = 'O'


def drawMaze(maze: list[list[bool]], path: list[tuple[int]]) -> str:
    s=""
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x]:
                s += 'W'
            elif (y, x) in path:
                s += 'O'
            else:
                s += 'P'
        s += '\n'
    return s


def coolMaze(maze: str) -> str:
    s = ""
    coolChars = {
        WALL: '⬛',
        PATH: '⬜',
        START: '❌',
        FINISH: '✅',
        FOUNDPATH: '⏺ '
    }
    
    for char in maze:
        if char in coolChars.keys():
            s += coolChars[char]
        else: s+='\n'

    return s


def main():
    maze: list[list[bool]] = []
    start: tuple[int]
    end: tuple[int]

    # load maze
    while True:
        inp = input()
        if inp == '':
            break
        else:
            line = []
            for x in range(len(inp)):
                line.append(inp[x] == WALL)
                if inp[x] == START:
                    start = (len(maze), x)
                elif inp[x] == FINISH:
                    end = (len(maze), x)
            maze.append(line)
    
    m = Maze(maze, diagonalMovement=False)
    path: list[tuple[int]] = m.astar(start, end)
    print(coolMaze(drawMaze(maze, path)))



if __name__ == '__main__':
    main()



"""
INPUT EXAMPLES:

WWWWWWWW
SPPPPPPW
WWWWWWPW
WPPPPPPW
WPWWWWWW
WPPPPPPF
WWWWWWWW


SPPPPWPPPP
PPPPPWPPPP
PPPPWWWPPP
PPPPWPPPPP
PPPPPPPPPP
PPPPWWWWPP
PPPPWPPPPP
PPPPWPPPPP
PPWWWPPPPP
PPPPPPPPPF

"""

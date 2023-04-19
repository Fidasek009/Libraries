from GraphAlgorithms import Graph

WALL = 'W'
PATH = 'P'
START = 'S'
FINISH = 'F'
FOUNDPATH = 'O'
 
class Maze:
    graph: Graph
    maze: list[list[chr]]
    height: int
    width: int
    start: int
    finish: int

    def __init__(self, maze: list[list[chr]]) -> None:
        self.height = len(maze)
        self.width = len(maze[0])
        self.maze = maze
        self.graph = Graph(self.height*self.width)

        # build graph
        for i in range(self.height):
            for j in range(self.width):
                if maze[i][j] != WALL:
                    vertex = i*self.width+j # number of current vertex

                    # find START/FINISH
                    if maze[i][j] == START: self.start = vertex
                    elif maze[i][j] == FINISH: self.finish = vertex
                    
                    # connecting paths
                    # look right
                    if j+1 < self.width and maze[i][j+1] != WALL:
                        self.graph.add_edge(vertex, vertex+1)
                    # look down
                    if i+1 < self.height and maze[i+1][j] != WALL:
                        self.graph.add_edge(vertex, vertex+self.width)


    def findPath(self) -> list[int]:
        return self.graph.BFS(self.start, self.finish)
    

    def drawPath(self) -> str:
        s = ""
        path = self.findPath()[1:-1] # find path and strip START + FINISH

        for i in range(self.height):
            for j in range(self.width):
                vertex = i*self.width+j # number of current vertex
                if vertex in path:
                    s += FOUNDPATH
                else:
                    s += self.maze[i][j]
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
    maze: list[list[chr]] = []

    # load maze
    while True:
        inp = input()
        if inp == '':
            break
        else:
            maze.append([char for char in inp])
    
    # create graph out of maze
    mazeObj = Maze(maze)

    # find shortest path with BFS and draw it out
    print(coolMaze(mazeObj.drawPath()))

    
if __name__ == "__main__":
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

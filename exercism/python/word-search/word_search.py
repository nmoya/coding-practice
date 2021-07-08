from typing import List, Optional


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise ValueError("Point value is required")

    def __radd__(self, other):
        return self.__add__(other)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"{self.x}, {self.y}"


class Direction:
    def __init__(self, name, offset_x, offset_y):
        self.name = name
        self.offset = Point(offset_x, offset_y)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.offset)

    def __repr__(self):
        return self.name


DIR_N = Direction("DIR_N", 0, -1)
DIR_NE = Direction("DIR_NE", 1, -1)
DIR_E = Direction("DIR_E", 1, 0)
DIR_SE = Direction("DIR_SE", 1, 1)
DIR_S = Direction("DIR_S", 0, 1)
DIR_SW = Direction("DIR_SW", -1, 1)
DIR_W = Direction("DIR_W", -1, 0)
DIR_NW = Direction("DIR_NW", -1, -1)
ADJACENTS = [DIR_N, DIR_NE, DIR_E, DIR_SE, DIR_S, DIR_SW, DIR_W, DIR_NW]


class Puzzle:
    def __init__(self, puzzle: List[str]):
        self.puzzle = puzzle
        self.nrows = len(puzzle)
        # Assume it will always be a square
        self.ncols = len(puzzle[0])

    def lines(self):
        return self.puzzle

    def get(self, coord: Point) -> str:
        if coord.x < 0:
            return None
        if coord.y < 0:
            return None
        if coord.x >= self.ncols:
            return None
        if coord.y >= self.nrows:
            return None
        return self.puzzle[coord.y][coord.x]


class Letter:
    def __init__(self, letter: str, coordinate: Point, adjacents):
        self.letter: str = letter
        self.coordinate: Point = coordinate
        self.adjacents: dict = adjacents

    def __repr__(self):
        return self.letter


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = Puzzle(puzzle)
        self.graph = self.build_graph()

    def build_graph(self):
        vertices = {}
        for y, line in enumerate(self.puzzle.lines()):
            for x, letter in enumerate(line):
                coord = Point(x, y)
                if vertices.get(coord) is None:
                    vertices[coord] = Letter(letter, coord, {})
                adjacents = {}
                for direction in ADJACENTS:
                    adj_coord: Point = coord + direction.offset
                    adj_vertex: Optional[letter] = vertices.get(adj_coord)
                    if adj_vertex:
                        adjacents[direction] = adj_vertex
                    else:
                        adj_letter: Optional[str] = self.puzzle.get(adj_coord)
                        if adj_letter:
                            adj_vertex = Letter(adj_letter, adj_coord, {})
                            vertices[adj_coord] = adj_vertex
                        adjacents[direction] = adj_vertex
                vertices[coord].adjacents = adjacents
        return vertices

    def search_rest(self, vertex: Letter, rest_word: str, direction: Direction, path: List[Letter]):
        if len(rest_word) == 0:  # 1 letter words
            return path
        first_letter = rest_word[0]
        if vertex is None:
            return None
        if vertex.letter != first_letter:
            return None
        if len(rest_word) == 1:  # Found the last letter
            path.append(vertex)
            return path
        else:
            same_direction_adjacent = vertex.adjacents[direction]
            path.append(vertex)
            return self.search_rest(same_direction_adjacent, rest_word[1:], direction, path)

    def search_start(self, word):
        if len(word) == 0:
            return None
        first_letter = word[0]
        start_letters = [vertex for vertex in self.graph.values() if vertex.letter == first_letter]
        for start in start_letters:
            for direction, adjacent in start.adjacents.items():
                result = self.search_rest(adjacent, word[1:], direction, [start])
                if result is not None:
                    return result
        return None

    def search(self, word):
        path = self.search_start(word)
        if path is None:
            return None
        else:
            return (path[0].coordinate, path[-1].coordinate)


if __name__ == "__main__":
    puzzle = WordSearch(["abc", "def", "ghi"])
    path = puzzle.search("eh")
    print(path)

class MarsRover:
    _AVAILABLE_DIRECTIONS: str = "NESW"

    _x_coord: int
    _y_coord: int
    _direction: str
    _obstacles: list[str]
    _obstacle_found: bool

    def __init__(self, x: int, y: int, direction: str, obstacles: list[str]) -> None:
        self._x_coord = x
        self._y_coord = y
        self._direction = direction
        self._obstacles = obstacles
        self._obstacle_found = False

    def get_state(self) -> str:
        return f"O:{self._x_coord}:{self._y_coord}:{self._direction}" if self._obstacle_found else f"{self._x_coord}:{self._y_coord}:{self._direction}"

    def execute(self, commands: str) -> None:
        for command in commands:
            if command == "M":
                if self._direction == "E":
                    self._obstacle_found = f"{self._x_coord + 1}:{self._y_coord}" in self._obstacles
                    self._x_coord = self._x_coord + 1 if not self._obstacle_found and self._x_coord < 9 else self._x_coord
                elif self._direction == "S":
                    self._obstacle_found = f"{self._x_coord}:{self._y_coord + 1}" in self._obstacles
                    self._y_coord = self._y_coord + 1 if not self._obstacle_found and self._y_coord < 9 else self._y_coord
                elif self._direction == "W":
                    self._obstacle_found = f"{self._x_coord - 1}:{self._y_coord}" in self._obstacles
                    self._x_coord = self._x_coord - 1 if not self._obstacle_found and self._x_coord > 0 else self._x_coord
                elif self._direction == "N":
                    self._obstacle_found = f"{self._x_coord}:{self._y_coord - 1}" in self._obstacles
                    self._y_coord = self._y_coord - 1 if not self._obstacle_found and self._y_coord > 0 else self._y_coord
            elif command == "L":
                current_direction = self._AVAILABLE_DIRECTIONS.index(self._direction)
                self._direction = self._AVAILABLE_DIRECTIONS[-1] if current_direction == 0 else self._AVAILABLE_DIRECTIONS[current_direction - 1]
            elif command == "R":
                current_direction = self._AVAILABLE_DIRECTIONS.index(self._direction)
                self._direction = self._AVAILABLE_DIRECTIONS[0] if current_direction == 3 else self._AVAILABLE_DIRECTIONS[current_direction + 1]

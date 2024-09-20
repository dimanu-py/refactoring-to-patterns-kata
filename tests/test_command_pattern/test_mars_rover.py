import pytest
from expects import expect, equal

from src.refactoring_to_patterns.command_pattern.mars_rover import MarsRover


class TestMarsRover:

    def test_accept_an_initial_state(self):
        mars_rover = MarsRover(0, 0, "N", [])

        expect(mars_rover.get_state()).to(equal("0:0:N"))

    @pytest.mark.parametrize(
        "initial_x, initial_y, initial_direction, commands, expected_state",
        [
            (0, 0, "E", "M", "1:0:E"),
            (0, 0, "S", "M", "0:1:S"),
            (1, 0, "W", "M", "0:0:W"),
            (0, 1, "N", "M", "0:0:N")
        ]
    )
    def test_move_once_cell_forward(self, initial_x, initial_y, initial_direction, commands, expected_state):
        mars_rover = MarsRover(initial_x, initial_y, initial_direction, [])

        mars_rover.execute(commands)

        expect(mars_rover.get_state()).to(equal(expected_state))

    @pytest.mark.parametrize(
        "initial_x, initial_y, initial_direction, commands, expected_state",
        [
            (0, 0, "N", "M", "0:0:N"),
            (0, 0, "W", "M", "0:0:W"),
            (9, 0, "E", "M", "9:0:E"),
            (0, 9, "S", "M", "0:9:S")
        ]
    )
    def test_wrap_around_edges_of_the_plateau(self, initial_x, initial_y, initial_direction, commands, expected_state):
        mars_rover = MarsRover(initial_x, initial_y, initial_direction, [])

        mars_rover.execute(commands)

        expect(mars_rover.get_state()).to(equal(expected_state))

    @pytest.mark.parametrize(
        "command, expected_state",
        [
            ("L", "0:0:N"),
            ("LL", "0:0:W"),
            ("LLL", "0:0:S"),
            ("LLLL", "0:0:E"),
            ("R", "0:0:S"),
            ("RR", "0:0:W"),
            ("RRR", "0:0:N"),
            ("RRRR", "0:0:E")
        ]
    )
    def test_rotate_left_and_right(self, command, expected_state):
        mars_rover = MarsRover(0, 0, "E", [])

        mars_rover.execute(command)

        expect(mars_rover.get_state()).to(equal(expected_state))

    @pytest.mark.parametrize(
        "initial_x, initial_y, initial_direction, obstacles, commands, expected_state",
        [
            (0, 0, "E", ["3:0"], "MMM", "O:2:0:E"),
            (0, 0, "S", ["0:3"], "MMM", "O:0:2:S"),
            (9, 0, "W", ["7:0"], "MMM", "O:8:0:W"),
            (0, 9, "N", ["0:7"], "MMM", "O:0:8:N"),
        ]
    )
    def test_stop_and_report_if_an_obstacle_is_found(self, initial_x, initial_y, initial_direction, obstacles, commands, expected_state):
        mars_rover = MarsRover(initial_x, initial_y, initial_direction, obstacles)

        mars_rover.execute(commands)

        expect(mars_rover.get_state()).to(equal(expected_state))

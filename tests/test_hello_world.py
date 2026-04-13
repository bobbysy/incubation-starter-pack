"""Tests for hello_world module."""

from hello_world.hello_world import greet, main


class TestGreet:
    """Tests for the greet function."""

    def test_greet_with_world(self) -> None:
        """Test greet with 'World' name."""
        assert greet("World") == "Hello, World!"

    def test_greet_custom_name(self) -> None:
        """Test greet with custom name."""
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_empty_name(self) -> None:
        """Test greet with empty name."""
        assert greet("") == "Hello, !"


class TestMain:
    """Tests for the main function."""

    def test_main_runs_without_error(self) -> None:
        """Test that main runs without raising an exception."""
        # main() prints to stdout, so we just verify it doesn't raise
        main()

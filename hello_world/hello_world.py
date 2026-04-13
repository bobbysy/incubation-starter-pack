"""Hello world module."""


def greet(name: str) -> str:
    """Return a greeting message.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"


def main() -> None:
    """Main entry point."""
    print(greet("World"))


if __name__ == "__main__":
    main()

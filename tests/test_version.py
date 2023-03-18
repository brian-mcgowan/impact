from importlib.metadata import version

from impact import __version__


def test_version():
    assert __version__ == version("impact")

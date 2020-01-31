__import__("pkg_resources").declare_namespace(__name__)

try:
    from ._version import version as __version__
except ImportError:
    pass

def hello_world():
    print('Greetings starshine, the earth says hello')

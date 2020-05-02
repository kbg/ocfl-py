"""Python implementation of OCFL."""
import sys
from .object import *
from .version import *
from .store import *
from .digest import *
from .disposition import get_dispositor
from .bagger import bag_as_source, bag_extracted_version, BaggerError

__version__ = '0.0.5'

if sys.version_info < (3, 6):  # pragma: no cover
    raise Exception("Must use python 3.6 or greater (sorry 2.7, you were a good buddy)!")  # pragma: no cover

'''This module makes randopass accessible without a nested import.'''

from randopass.randopass import getPass, getVersion

__version__ = getVersion()

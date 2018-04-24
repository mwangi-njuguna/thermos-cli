
"""The create command."""

from json import dumps

from .base import Base


class Create(Base):
    """Make base folder application structure"""

    def run(self):
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))

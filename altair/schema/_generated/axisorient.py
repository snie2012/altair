# This file auto-generated by altair.schema.parser.write_files().
# do not modify directly.

import traitlets as T


class AxisOrient(T.Enum):
    def __init__(self, default_value=T.Undefined, **metadata):
        super(AxisOrient, self).__init__(['top', 'right', 'left', 'bottom'],
                                    default_value=default_value,
                                    **metadata)
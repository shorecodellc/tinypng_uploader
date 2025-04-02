#kevin fink
#kevin@shorecode.org
#Fri Oct 18 09:45:28 AM +07 2024
#tpu_filepaths.py

import os
import platform
from dataclasses import dataclass, field

@dataclass
class Files:
    current_platform: str = field(init=False)
    filepaths: list = field(default_factory=lambda: [
        'logging/tpu.log', 'data/output', 'data/input', 'data/input_thumbs', 
    ])
    win_filepaths: list = field(default_factory=list)

    def __post_init__(self):
        self.current_platform = platform.system()
        if self.current_platform == 'Windows':
            for f in self.filepaths:
                f = f.replace('/', '\\')
                f = os.path.dirname(os.path.abspath(__file__)) + '\\' + f
                self.win_filepaths.append(f)
        else:
            for idx, f in enumerate(self.filepaths):
                f = os.path.dirname(os.path.abspath(__file__)) + '/' + f
                self.filepaths[idx] = f

    def get_files_list(self) -> list:
        if self.current_platform == 'Windows':
            return self.win_filepaths
        else:
            return self.filepaths
        
    def get_file_by_index(self, idx: int) -> str:
        if self.current_platform == 'Windows':
            return self.win_filepaths[idx]
        else:
            return self.filepaths[idx]

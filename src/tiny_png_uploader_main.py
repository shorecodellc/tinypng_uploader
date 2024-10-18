#kevin fink
#kevin@shorecode.org
#Fri Oct 18 09:45:28 AM +07 2024
#

import sys
from  import
from  import

files = Files()
filepaths = files.get_files_list()
log_fp = filepaths[0]

logger = set_logging('', log_fp)

if __name__ == '__main__':
    sys.exit(0)


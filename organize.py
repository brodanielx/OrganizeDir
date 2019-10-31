import os
import sys

from pathlib import Path


home = '/Users/danielnilsson-cole'
full_test_path = '/Users/danielnilsson-cole/dev/projects/OrganizeDir/testdir'
short_test_path = '/OrganizeDir/testdir'
fake_test_path = '/Users/danielnilsson-cole/dev/projects/OrganizeDir/testd'

path_does_not_exist_message = """\
    The path you provided does not exist.
    Please provide the full path.
    ex: '/Users/user/dev/projects/dir/'
    """ 



def organize(path):
    isExist = os.path.exists(path)

    if not isExist:
        print(path_does_not_exist_message)
    else:
        os.chdir(path)

        for dirpath, dirnames, filenames in os.walk(path):
            file_extensions = [os.path.splitext(filename)[1] for filename in filenames]
            pass
    
    pass







if __name__ == "__main__":
    # organize(sys.argv)

    organize(full_test_path)
    # organize(short_test_path)
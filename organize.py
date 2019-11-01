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
    if not isExist(path):
        print(path_does_not_exist_message)
    else:
        os.chdir(path)

        for dirpath, dirnames, filenames in os.walk(path):
            if dirpath == path:
                file_extensions = get_distinct_file_extensions_from_filenames(filenames)
                break

        makedirs(file_extensions)
    
    pass



def isExist(path):
    return os.path.exists(path)


def get_distinct_file_extensions_from_filenames(filenames):
    file_extensions = get_file_extensions(filenames)
    cleaned_file_extensions = clean_file_extensions(file_extensions)
    return get_distinct_values_from_list(cleaned_file_extensions)


def get_file_extensions(filenames):
    file_extensions = [get_file_extension(filename) for filename in filenames]
    if '' in file_extensions:
        file_extensions.remove('')
    return file_extensions

def get_file_extension(filename):
    return os.path.splitext(filename)[1]


def clean_file_extensions(file_extensions):
    return [clean_file_extension(file_extension) for file_extension in file_extensions]

def clean_file_extension(file_extension):
    return file_extension.replace('.', '').lower()


def get_distinct_values_from_list(list_param):
    distinct_values = []
    [distinct_values.append(item) for item in list_param 
        if item not in distinct_values]
    return distinct_values

def makedirs(dirs):
    for dir in dirs:
        makedir(dir)

def makedir(dir):
    try:
        os.mkdir(dir)
    except OSError:
        print('OSError')






if __name__ == "__main__":
    # organize(sys.argv)

    organize(full_test_path)
    # organize(short_test_path)
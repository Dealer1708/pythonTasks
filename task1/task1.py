import os

path = "file_dir/"
file_dir = os.walk(path)
root_folders = []
files_dict = {}
folders = []
folder_depths = {}



def get_directory_size(path="."): 
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path)
    return total

def sort_by_size(dict):
    for i in folders:
            # print(i)
            dict[i] = get_directory_size(f"{i}/")
    sorted_folders = sorted(dict, reverse=True)
    f = []
    for j in sorted_folders:
        j = j.split("/")
        # print(j)
        f.append(j[-1])
    print("Sorted by size:",*f)

def sort_by_name():
    f = []
    for i in folders:
        i = i.split("/")
        f.append(i[-1])
    print("Sorted by name:",*sorted(f))

def sort_by_depth():
    print("Sorted by depth:", *sorted(folder_depths))



for i in os.walk(path):
    for j in i[1]:
        folder_depths[j] = 0
    break

for i in file_dir:
    # print(i[0])
    splitted = i[0].split("/")
    if splitted[1] == '':
        continue
    # print(splitted)
    # print(folder_depths[splitted[1]])
    # print(len(splitted[2::]))
    if folder_depths[splitted[1]] < len(splitted[2::]):
        folder_depths[splitted[1]] = len(splitted[2::])
    else:
        continue

    folders.append(i[0])
    files_dict[i[0]] = 0

# print(folder_depths)
# print(folder_depths)
# print(folders)

sort_by_name()
sort_by_size(files_dict)
sort_by_depth()
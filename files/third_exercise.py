import os
import sys


class ThirdWork:
    def __init__(self):
        pass

    def sorted_files(self):
        folder_path = "/Users/sergeibiryukov/Netology/files_learning/files"
        files = os.listdir(folder_path)
        filename = os.path.basename(sys.argv[0])

        files_sorted = sorted(files, key=lambda f: sum(1 for _ in open(os.path.join(folder_path, f))))

        with open("result.txt", "w") as result_file:
            for file_name in files_sorted:
                if file_name != filename:
                    result_file.write(f"\n{file_name} \n")
                num_lines = sum(1 for _ in open(os.path.join(folder_path, file_name)))
                if file_name != filename:
                    result_file.write(str(num_lines) + "\n")
                with open(os.path.join(folder_path, file_name), "r") as input_file:
                    for line in input_file:
                        if file_name != filename:
                            result_file.write(line)


third_work = ThirdWork()
third_work.sorted_files()

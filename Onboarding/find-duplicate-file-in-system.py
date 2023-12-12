class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_files = {}

        for path in paths:
            info = path.split(" ")
            directory = info[0].rstrip("/")
            files = info[1:]

            for file in files:
                file_info = file.split("(")
                file_name = file_info[0]
                content = file_info[1][:-1]
                file_path = directory + "/" + file_name

                if content in content_files:
                    content_files[content].append(file_path)
                else:
                    content_files[content] = [file_path]

        duplicate_groups = [files for files in content_files.values() if len(files) > 1]
        return duplicate_groups
        
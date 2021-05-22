from pathlib import Path


RESULTS_DIRECTORY = 'results'
BROKEN_FILE_NAME = 'broken.txt'
OUTPUT_FILE_NAME = 'output.txt'
LINKS_FILE_NAME = 'links.txt'


class FileOperations:

    def __init__(self, link):

        self.directory_name = link.get_domain()
        self.directory_path = f'{RESULTS_DIRECTORY}/{self.directory_name}'

        self.broken_file_name = BROKEN_FILE_NAME
        self.output_file_name = OUTPUT_FILE_NAME
        self.links_file_name = LINKS_FILE_NAME

        self.create_directory()

    def create_directory(self):
        Path(self.directory_path).mkdir(parents=True, exist_ok=True)
        print(f'Created directory {self.directory_path}')

    def write_in_broken(self, line):
        return self.write_line(self.broken_file_name, line)

    def write_in_output(self, line):
        return self.write_line(self.output_file_name, line)

    def write_in_links(self, line):
        return self.write_line(self.links_file_name, line)
        
    def write_line(self, filename, line):

        file_path = f'{self.directory_path}/{filename}'

        if self.is_line_exists_in_file(file_path, line):
            return True

        f = open(file_path, 'a')
        f.write(f'{line}\n')  # python will convert \n to os.linesep
        f.close()

    def is_line_exists_in_file(self, file_path, line):

        if not self.is_file_exists(file_path):
            return False

        with open(file_path) as f:
            file_content = f.read()
            if line in file_content:
                return True

        return False

    def is_file_exists(self, file_path):

        fyle = Path(file_path)

        if fyle.is_file():
            return True

        return False

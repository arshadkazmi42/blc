BROKEN_FILE_NAME = 'broken.txt'
OUTPUT_FILE_NAME = 'output.txt'


class FileOperations:

    def __init__(self, link):

        self.directory_name = link.get_domain()

        self.broken_file_name = BROKEN_FILE_NAME
        self.output_file_name = OUTPUT_FILE_NAME

    def write_in_broken(self, line):
        return self.write_line(self.broken_file_name, line)

    def write_in_output(self, line):
        return self.write_line(self.output_file_name, line)
        
    def write_line(self, filename, line):

        if is_line_exists(file_path, line):
            return True

        f = open(filename, 'a')
        f.write(f'{line}\n')  # python will convert \n to os.linesep
        f.close()

    def is_line_exists_in_file(self, filename, line):

        if not is_file_exists(filename):
            return False

        with open(filename) as f:
            file_content = f.read()
            if line in file_content:
                return True

        return False

    def is_file_exists(self, filename):

        fyle = Path(file_path)

        if fyle.is_file():
            return True

        return False

from abc import ABC, abstractmethod


class FileHandler(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def read(self):
        pass


class TxtFileHandler(FileHandler):
    def read(self):
        with open(self.file_path, "r", encoding="utf-8") as file_object:
            content = file_object.read()
        return content

class CsvFileHandler(FileHandler):
    def read(self):
        with open(self.file_path, "r", encoding="utf-8") as file_object:
            import csv
            reader = csv.reader(file_object)
            content = [row for row in reader]
        return content

class JsonFileHandler(FileHandler):
    def read(self):
        with open(self.file_path, "r", encoding="utf-8") as file_object:
            import json
            content = json.load(file_object)
        return content


def print_file_content(file_reader: FileHandler):
    content = file_reader.read()
    print("\n Dosya İçeriği:")
    print(content)


print_file_content(TxtFileHandler("sample.txt"))
print_file_content(CsvFileHandler("sample.csv"))
print_file_content(JsonFileHandler("sample.json"))
class FileManager:
    def __init__(self,file_name:str):
        self.file_name = file_name

    def read_file(self):
        lines = []
        try:
            file = open(self.file_name, "r", encoding="utf-8")
            lines = [line for line in file]
            file.close()
        finally:
            return lines

    def update_file(self,text_data:str):
        file = open(self.file_name,"a",encoding="utf-8")
        file.write(text_data)
        file.close()

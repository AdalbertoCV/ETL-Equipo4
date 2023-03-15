from src.extractors.txt_extractor import TXTExtractor
from os.path import join
import luigi, os, json

class TXTTransformer(luigi.Task):

    def requires(self):
        return TXTExtractor()

    def run(self):
        result = []
        for file in self.input():
            with file.open() as txt_file:
                txt_file.readline()
                lines = []
                line = ""
                while 1:
                    char = txt_file.read(1)         
                    if char ==';':
                        lines.append(line)
                        line = ""
                    else:
                        if not char:
                            break
                        else:
                            line = line + str(char)   
                for l in lines:
                    line_split = l.split(",")
                    result.append(
                        {
                            "description": line_split[2],
                            "quantity": line_split[3],
                            "price": line_split[5],
                            "total": float(line_split[3]) * float(line_split[5]),
                            "invoice": line_split[0],
                            "provider": line_split[6],
                            "country": line_split[7]
                        }
                    )
        with self.output().open('w') as out:
            out.write(json.dumps(result, indent=4))

    def output(self):
        project_dir = os.path.dirname(os.path.abspath("loader.py"))
        result_dir = join(project_dir, "result")
        return luigi.LocalTarget(join(result_dir, "txt.json"))
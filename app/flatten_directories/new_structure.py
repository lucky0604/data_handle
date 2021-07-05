import os
from shutil import copyfile

def flattern_directory(path):
    dirs = os.listdir(path)
    for i in dirs:
        if not os.path.exists(os.path.join('./output/B.Fraction.MR.1', i)):
            os.makedirs(os.path.join('./output/B.Fraction.MR.1', i))
        for root, directories, files in os.walk(os.path.join('./input/B.Fraction.MR.1', i)):
            for filename in files:
                output_name = '-'.join(os.path.join(root, filename).split('/')[2:])
                copyfile(os.path.join(root, filename), './output/B.Fraction.MR.1/' + i + '/' + output_name)



if __name__ == '__main__':
    flattern_directory('./input/B.Fraction.MR.1')
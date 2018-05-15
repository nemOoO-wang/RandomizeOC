from InsertCode import tweek_file
import glob


Work_Directory = '/Users/Nemo/Desktop/XCodeTest/Origin/MingYaDianZhu/MingYa/entrance'
dir_list = glob.glob(Work_Directory+'/**/*.m', recursive=True)
for m_file_path in dir_list:
    tweek_file(m_file_path)

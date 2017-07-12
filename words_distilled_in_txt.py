#-*- coding:UTF-8 -*-
import os,collections,re
text_path = '/mnt/d/bash/'#input('请输入要进行提取的文件的文件路径：\n')
while not (os.path.exists(text_path)):
    print('你输入的文件或文件路径不存在！')
    text_path = input('请重新输入文件路径和文件名：\n')
text_path_listdir = os.listdir(text_path)
write_path = '/mnt/d/bash_words/'#input('请输入存储位置的路径：\n')

while not (os.path.exists(write_path)):
    if input('你输入的路径不存在，是否创建这个路径？\n输入yes or no\n')=='yes':
        os.mkdir(write_path,777)
    else:
        write_path = input('请重新输入存储路径：\n')

def pick_up(text_path,writh_path): 
    print('正在读取文件......')
    text_file = open(text_path,'r')
    print('文件读取完毕！\n正在读取文件内容......')
    text_str = text_file.read()
    #print('文件内容读取完毕！\n正在导入提取模块......')
    print('模块导入完毕\n正在进行提取......')
    words = re.findall('[A-Za-z]+[\']?[a-z]*',text_str)
    print('文件提取完毕！\n正在对提取内容进行清洗......')
    words = eval(str(words).lower())
    print('正在进行词频分析')
    words_counter = collections.Counter(words)
    print('清洗完毕!\n准备创建存储文件......')
    print(text_path)
    #write_path = re.match('/(\w+/)+',text_path).group(0).rstrip('/') + '_words'
    file_name = re.search('/[^/]*\.',text_path).group(0).rstrip('.').lstrip('/') + '_words.txt'
    
    write_file = write_path + file_name
    print('正在创建文件！')
    write_file = open(write_file,'w+')
    print('存储文件创建完毕！\n正在向存储文件写入提取内容......')
    write_file.write(str(words_counter))
    print('刷新缓存......')
    write_file.flush()
    print('提取内容存储完毕！')
    write_file.close()
file_name_distinguish = input('是否只对特定文件进行提取，yes or no：')
if file_name_distinguish == 'yes':
    file_name_feature = input('输入文件名特征：')
if __name__ == '__main__': 
    if file_name_distinguish == 'yes':
        for i in text_path_listdir: 
            if file_name_feature in i:
                pick_up(text_path+i,write_path)
    else:
        for i in text_path_listdir:
            pick_up(text_path+i,write_path)   
    print('程序结束！')

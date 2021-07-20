import multiprocessing
import os


def copy_file(queue, file_name, old_folder_name, new_folder_name):
    f_read = open("../" + old_folder_name + "/" + file_name, 'rb')
    f_write = open("../" + new_folder_name + "/" + file_name, 'wb')
    while True:
        content = f_read.read()
        if content:
            f_write.write(content)
        else:
            break
    f_read.close()
    f_write.close()
    # print("文件复制完毕！")
    queue.put(file_name)


def main():
    # 获取要复制的文件夹名称
    old_folder_name = input('请输入要复制的文件夹名称：')
    # 创建新的文件夹名称
    new_folder_name = old_folder_name + "_副本"
    # 创建新的文件夹
    try:
        os.mkdir("../" + new_folder_name)
    except Exception as ret:
        print("文件夹已存在！")
        pass
    # 获取文件夹下所有文件的名称
    file_names = os.listdir("../" + old_folder_name)
    # 创建线程池
    pool = multiprocessing.Pool(3)
    # 创建队列
    queue = multiprocessing.Manager().Queue()
    # 向线程池中添加任务
    for file_name in file_names:
        pool.apply_async(copy_file, args=(queue, file_name, old_folder_name, new_folder_name))
        print(file_name)

    print("----")
    pool.close()
    # pool.join()
    all_file_nums = len(file_names)
    while True:
        get_file_name = queue.get()
        if get_file_name in file_names:
            file_names.remove(get_file_name)

        copy_rate = 1 - len(file_names) / all_file_nums
        print("\r%.2f...(%s)" % (copy_rate, file_name) + " " * 50, end="")
        if copy_rate >= 1:
            break


if __name__ == '__main__':
    main()

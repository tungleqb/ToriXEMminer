import subprocess
import multiprocessing
def command1():
  # Lệnh hoặc công việc bạn muốn chạy ở lệnh đầu tiên
  subprocess.run(['python', '/content/ToriXEMminer/miner.py', '--gpu=true'])

def command2():
  # Lệnh hoặc công việc bạn muốn chạy ở lệnh thứ hai
  subprocess.run(['nohup','/content/ToriXEMminer/xengpuminer', '-b', '1024'])

if __name__ == '__main__':
  # Tạo hai tiến trình riêng biệt cho mỗi lệnh
  process1 = multiprocessing.Process(target=command1)
  process2 = multiprocessing.Process(target=command2)

  # Bắt đầu chạy các tiến trình
  process1.start()
  process2.start()

  # Chờ cho đến khi các tiến trình hoàn thành
  process1.join()
  process2.join()

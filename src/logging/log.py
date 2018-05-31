import datetime


def open_log_file():
    return open("logs/console.log", "a+")


def close_log_file(file):
    file.close()


def save_info(data):
    file = open_log_file()
    file.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " - " + data + "\n")
    close_log_file(file)
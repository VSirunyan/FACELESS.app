import socket
import json
import os


def main():
    host = '127.0.0.1'
    port = 55555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    script_dir = os.path.dirname(__file__)
    testcases_path = os.path.join(script_dir, "testcases.json")

    with open(testcases_path, "r") as content:
        testcases = json.load(content)

    for testcase in testcases:
        data_package = json.dumps(testcase)
        s.sendall(data_package)

        print('Received', repr(data_package))

        status = s.recv(1024)
        if status != "OK":
            raise Exception("No response from server")

    s.close()


if __name__ == "__main__":
    main()

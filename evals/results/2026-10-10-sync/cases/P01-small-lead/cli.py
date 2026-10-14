import argparse

p = argparse.ArgumentParser(description="导出报告")
p.add_argument("--format", default="csv")
if __name__ == "__main__":
    p.parse_args()

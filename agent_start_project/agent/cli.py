import argparse


class CLIParser:

    def __init__(self, parser: argparse.ArgumentParser):
        self.parser = parser
        self.init_parser()

    def init_parser(self):
        self.parser.add_argument(
            "--rules",
            "-r",
            nargs="+",
            required=True,
            help="Path(s) to TASK rule directories"
        )
        self.parser.add_argument(
            "--mcp",
            "-m",
            nargs="+",
            required=True,
            help="URL(s) to MCP endpoint(s) (FastAPI)"
        )
        self.parser.add_argument(
            "--tasklist",
            "-t",
            nargs="+",
            required=True,
            help="Path(s) to tasklist file(s) (txt or md) to process"
        )

    def parse_args(self):
        return self.parser.parse_args()

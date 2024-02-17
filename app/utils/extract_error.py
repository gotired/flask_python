"""Erro Utility Module"""


class Error:
    """Error Utility class"""

    @staticmethod
    def extract_location(traceback_info) -> dict:
        """Extract error location from traceback"""
        lines = traceback_info.split("\n")
        for line in lines:
            if 'File "' in line and not (
                "site-packages" in line
                or "dist-packages" in line
                or "Frameworks" in line
            ):
                parts = line.split(",")
                filename = parts[0].strip().split(" ")[-1].split("app")[-1].strip('"')
                line_number = parts[1].strip().split(" ")[-1]
                return {"location": filename, "line": line_number}
        return {"location": None, "line": None}

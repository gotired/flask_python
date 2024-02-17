"""Response Schema Model Module"""


class Response:
    """Response Schema Model."""

    def __init__(self, data=None, detail=None) -> None:
        self.response = {"data": data, "detail": detail}

    def success(self):
        """for successful response"""
        return self._add_status("success")

    def failure(self):
        """for unsuccessful response"""
        return self._add_status("failure")

    def _add_status(self, status):
        return {**self.response, "status": status}

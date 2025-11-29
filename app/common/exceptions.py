class DatabaseException(Exception):
    """
    Exception chung cho các lỗi DB
    """
    def __init__(self, message="Database error", code=500):
        self.message = message
        self.code = code
        super().__init__(message)

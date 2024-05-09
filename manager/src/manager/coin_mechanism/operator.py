class CoinMechanismOperator:
    _instance = None
    _is_initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # Initialize the coin mechanism operator
        if not self._is_initialized:
            # Initialization code here.
            self._is_initialized = True

    def accept_coin(self, coin):
        # Code to accept the coin
        pass

    def reject_coin(self, coin):
        # Code to reject the coin
        pass

    def check_status(self):
        # Code to check the status of the coin mechanism
        pass
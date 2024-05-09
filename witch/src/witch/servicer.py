from .rpc.coin_system_pb2 import SystemState
from .rpc.witch_intuitions_pb2 import IntuitionResponse, IntuitiveExpression, IntuitiveAction
from .rpc.witch_intuitions_pb2_grpc import WitchIntuitionsServicer

class WitchServicer(WitchIntuitionsServicer):
    """Provides methods that implement functionality of witch intuitions server."""

    def TransferIntuitions(self, request_iterator, context):
        print("TransferIntuitions")
        prev_intuition_requests = []
        for new_intuition_request in request_iterator:
            result = IntuitionResponse(
                sender='vessel',
                state=SystemState.RUNNING,
                expression = IntuitiveExpression.BLANK,
                action = IntuitiveAction.NONE,
                strength = 0,
            )
            yield result
            prev_intuition_requests.append(new_intuition_request)
from .rpc.coin_system_pb2 import SystemState
from .rpc.vessel_instructions_pb2 import VesselResult
from .rpc.vessel_instructions_pb2_grpc import VesselInstructionsServicer

class VesselServicer(VesselInstructionsServicer):
    """Provides methods that implement functionality of vessel instructions server."""

    def TransferInstructions(self, request_iterator, context):
        print("TransferInstructions")
        prev_instructions = []
        for new_instruction in request_iterator:
            result = VesselResult(
                sender='vessel',
                state=SystemState.RUNNING,
                message=f'Received message from {new_instruction.sender}: {new_instruction.input}'
            )
            yield result
            prev_instructions.append(new_instruction)
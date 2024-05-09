from .rpc.vessel_instructions_pb2 import VesselInstruction, VesselAction
from .rpc.coin_system_pb2 import SystemState

def make_instruction(instruction):
    return VesselInstruction(
        sender='manager',
        priority=0,
        state=SystemState.RUNNING,
        action=VesselAction.NONE,
        strength=0,
        input=instruction
    )

def generate_instructions():
    instructions = [
        make_instruction('First instruction'),
        make_instruction('Second instruction'),
        make_instruction('Third instruction'),
    ]
    for instruction in instructions:
        print(f'Sending instruction: {instruction.input}')
        yield instruction

def transfer_instructions(stub):
    responses = stub.TransferInstructions(generate_instructions())
    for response in responses:
        print(
            f"Received message from {response.sender}: ({response.state}, {response.message})"
        )
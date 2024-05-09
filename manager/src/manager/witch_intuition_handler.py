from .rpc.witch_intuitions_pb2 import IntuitionRequest, IntuitionResponse
from .rpc.coin_system_pb2 import SystemState

def make_request(intuition):
    return IntuitionRequest(
        sender='manager',
        priority=0,
        state=SystemState.RUNNING,
        message=intuition
    )

def generate_requests():
    requests = [
        make_request('First request'),
        make_request('Second request'),
        make_request('Third request'),
    ]
    for request in requests:
        print(f'Sending request: {request.message}')
        yield request

def transfer_intuitions(stub):
    responses = stub.TransferIntuitions(generate_requests())
    for response in responses:
        print(
            f"Received message from {response.sender}: ({response.expression}, {response.action}, {response.strength})"
        )
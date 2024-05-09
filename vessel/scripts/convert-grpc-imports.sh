# Convert src/vessel/rpc/vessel_instructions_pb2.py imports from absolute to relative
sed -i '' 's/^import coin_system_pb2 as coin__system__pb2$/from . &/' src/vessel/rpc/vessel_instructions_pb2.py

# Convert src/vessel/rpc/vessel_instructions_pb2_grpc.py imports from absolute to relative
sed -i '' 's/^import vessel_instructions_pb2 as vessel__instructions__pb2$/from . &/' src/vessel/rpc/vessel_instructions_pb2_grpc.py
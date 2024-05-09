# Convert src/vessel/rpc/witch_intuitions_pb2.py imports from absolute to relative
sed -i '' 's/^import coin_system_pb2 as coin__system__pb2$/from . &/' src/witch/rpc/witch_intuitions_pb2.py

# Convert src/vessel/rpc/witch_intuitions_pb2_grpc.py imports from absolute to relative
sed -i '' 's/^import witch_intuitions_pb2 as witch__intuitions__pb2$/from . &/' src/witch/rpc/witch_intuitions_pb2_grpc.py
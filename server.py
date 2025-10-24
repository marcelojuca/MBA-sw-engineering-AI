import grpc
from concurrent import futures
import hello_pb2  # Data classes for the protobuf file "hello.proto"
import hello_pb2_grpc  # Service stubs and servicer classes for the protobuf file "hello.proto"

class Greeter(hello_pb2_grpc.GreeterServicer):

    # Unary RPC
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f"Hello, {request.name}!")

    # Server streaming
    def SayHelloStream(self, request, context):
        for i in range(5):
            yield hello_pb2.HelloReply(message=f"Hello {request.name} #{i+1}")

    # Client streaming
    def RecordHello(self, request_iterator, context):
        count = 0
        for request in request_iterator:
            print(f"Received: {request.name}")
            count += 1
        return hello_pb2.HelloCount(count=count)

    # Bidirectional streaming
    def ChatHello(self, request_iterator, context):
        for request in request_iterator:
            yield hello_pb2.HelloReply(message=f"Echo: {request.name}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
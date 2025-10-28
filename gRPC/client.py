import grpc
import generated.hello_pb2 as hello_pb2  # Data classes for the protobuf file "hello.proto"
import generated.hello_pb2_grpc as hello_pb2_grpc  # Service stubs and servicer classes for the protobuf file "hello.proto"

def run():
    # Connect to server (insecure for demo)
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)

        # 1. Unary RPC
        print("--- Unary RPC ---")
        response = stub.SayHello(hello_pb2.HelloRequest(name="Alice"))
        print("Response:", response.message)

        # 2. Server streaming
        print("\n--- Server Streaming ---")
        stream = stub.SayHelloStream(hello_pb2.HelloRequest(name="Bob"))
        for reply in stream:
            print("Stream reply:", reply.message)

        # 3. Client streaming
        print("\n--- Client Streaming ---")

        def generate_requests():
            for name in ["Carol", "Dave", "Eve"]:
                yield hello_pb2.HelloRequest(name=name)

        count = stub.RecordHello(generate_requests())
        print(f"Total names sent: {count.count}")

        # 4. Bidirectional streaming
        print("\n--- Bidirectional Streaming ---")

        def generate_chat():
            for name in ["Frank", "Grace"]:
                print(f"Client sending: {name}")
                yield hello_pb2.HelloRequest(name=name)

        for reply in stub.ChatHello(generate_chat()):
            print("Server reply:", reply.message)

if __name__ == '__main__':
    run()
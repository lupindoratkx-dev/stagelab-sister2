from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import argparse, functools, threading, webbrowser

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="Preview StageLab locally")
    parser.add_argument("--port",type=int,default=8000)
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    handler=functools.partial(SimpleHTTPRequestHandler,directory=str(root))
    try:
        server=ThreadingHTTPServer(("127.0.0.1",args.port),handler)
    except OSError as error:
        raise SystemExit(f"Cannot open port {args.port}: {error}. Try: python start.py --port 8001")
    url=f"http://127.0.0.1:{server.server_port}/"
    print(f"StageLab: {url}\nPress Ctrl+C to stop.")
    threading.Timer(.7,lambda:webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

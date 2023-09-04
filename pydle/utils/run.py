## run.py
# Run client.
import asyncio
from . import _args


def main():
    client, connect = _args.client_from_args('pydle', description='pydle IRC library.')

    # Python 3.10+
    try:
        loop = asyncio.get_event_loop()
    except Exception:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    asyncio.ensure_future(connect(), loop=loop)
    loop.run_forever()


if __name__ == '__main__':
    main()

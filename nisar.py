import platform
arc = str(platform.uname().machine)
if 'arm' in arc:
          __import__("t").main()
elif 'aarch' in arc:
              __import__("t").main()
else:
        exit(f' Unknow device machine {arc}')

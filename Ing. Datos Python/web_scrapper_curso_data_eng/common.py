importyaml

__config=None

defconfig():
global__config
ifnot__config:
withopen('config.yaml',mode='r')asf:
__config=yaml.load(f,Loader=yaml.FullLoader)
return__config

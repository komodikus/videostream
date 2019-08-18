import configparser
import ast

config_path = "settings.ini"


def create_config(path=config_path):
    config = configparser.ConfigParser()
    config['Settings'] = {
        'urls': ['rtsp://b1.dnsdojo.com:1935/live/sys2.stream', 'rtsp://b1.dnsdojo.com:1935/live/sys3.stream',
               '0'],
        'filter': 'default',
    }
    with open(config_path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(section, setting, path=config_path):
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )
    print(msg)
    if setting == "urls":
        return ast.literal_eval(value)
    return value



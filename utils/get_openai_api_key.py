import os
import openai
from dotenv import load_dotenv, find_dotenv


def get_openai_key():
    # 读取本地/项目的环境变量。
    # find_dotenv()寻找并定位.env文件的路径
    # load_dotenv()读取该.env文件，并将其中的环境变量加载到当前的运行环境中

    _ = load_dotenv(find_dotenv())
    return os.environ['OPENAI_API_KEY']


openai.api_key = get_openai_key()

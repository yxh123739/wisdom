import time
from wake import start_wake
from gpt import get_answer
from chatgpt import ChatGptManager
import azure_manager

def main(prompt):
    try:
        start = time.time()
        answer = gpt.ask(prompt)
        end = time.time()
        print('cost time:',end-start,'s')
        manager.azure_speak(answer)
    except Exception as e:
        manager.azure_speak('我不知道你在说什么，你可以换个方式问我')


def do_end(prompt):
    end_words = ['再见', '拜拜', 'bye', 'Goodbye']
    if prompt.replace('。','') in end_words:
        return True
    for word in end_words:
        if word in prompt:
            return True
    return False

def do_shutdown(prompt):
    if prompt.replace('。','') == '关机':
        return True
    return False

if __name__ == "__main__":
    
    lans = ['zh-Cn','en-US']
    spe_model = ['zh-cn-XiaoyanNeural','en-US-SaraNeural']
    index = input('请选择语言：1.中文 2.英文')
    index = int(index)-1
    manager = azure_manager.AzureManager(voice=spe_model[index],lan=lans[index])
    gpt = ChatGptManager(proxy='127.0.0.1:10810')
    init = False
    while True:
        if not init:
            wake = start_wake()
            if wake:
                init = True
                res = manager.azure_speak('你好，我在，有什么可以帮助您的吗？')
            else:
                continue
        prompt = manager.azure_listen()
        if do_end(prompt):
            res = manager.azure_speak('再见,有需要随时叫我')
            init = False
            continue
        elif do_shutdown(prompt):
            res = manager.azure_speak('好的，再见')
            break
        main(prompt)
        

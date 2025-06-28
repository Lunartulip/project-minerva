import requests
import json
import os

class DeepseekClient:
    def __init__(self, api_key=None):
        # 如果没有提供 API 密钥，将尝试从环境变量中读取
        self.api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise ValueError("API key is required. Please set it in the environment variable or pass it directly.")

        # 服务器URL - 修正为正确的聊天完成API端点
        self.base_url = "https://api.deepseek.com/v1/chat/completions"

    def generate_text(self, prompt, temperature=0.3, max_tokens=4096):
        """
        调用 Deepseek API 来生成文本
        :param prompt: 输入的提示词
        :param temperature: 控制生成文本的多样性
        :param max_tokens: 控制最大生成的 token 数量
        :return: 返回生成的文本
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # 请求体 - 修正为正确的消息格式
        payload = {
            "model": "deepseek-chat",  # 或者使用其他可用的模型名称
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        response = requests.post(self.base_url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            # 修正响应解析方式
            return response.json()["choices"][0]["message"]["content"]
        else:
            print(f"Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None

# 使用示例
if __name__ == "__main__":
    # 设置 Deepseek API 密钥
    deepseek_client = DeepseekClient(api_key="sk-45b8xxxx0ac04ae0b721e63754f2a314")
    
    prompt = "Please provide an analysis of the stock market trends in 2023."
    output = deepseek_client.generate_text(prompt)

    if output:
        print("Generated Text:", output)

from flask import Flask, request, jsonify
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

app = Flask(__name__)

# 配置 Deepseek
llm = ChatOpenAI(
    model_name="deepseek-chat",
    openai_api_key="sk-9f070948aadf4a729f31da1e51a7552d",
    openai_api_base="https://api.deepseek.com/v1"
)

@app.route('/')
def index():
    return "欢迎来到聊天应用！请使用 /api/chat 路径进行聊天。"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')

    if not user_input:
        return jsonify({'reply': '请输入有效的消息'}), 400

    try:
        messages = [HumanMessage(content=user_input)]
        response = llm.invoke(messages)
        return jsonify({'reply': response.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)

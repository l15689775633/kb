from fastapi.testclient import TestClient
from unittest.mock import patch

# 导入你的代码中的相关模块
from your_module import app, KnowledgeCreate, UnifiedResponseModel, KnowledgeRead, UserPayload, get_login_user, session_getter, create_knowledge_hook, settings, Knowledge

# 创建测试客户端
client = TestClient(app)

# 测试函数
def test_create_knowledge():
    # 模拟登录用户
    mock_login_user = UserPayload(user_id=1)
    with patch('your_module.get_login_user', return_value=mock_login_user):
        # 模拟知识库创建数据
        mock_knowledge = KnowledgeCreate(
            name='test_knowledge',
            model='text-embedding-ada-002',
            description='测试知识库',
            is_partition=False,
            collection_name='test_collection',
            index_name='test_index',
            user_id=1
        )
        # 模拟数据库会话
        with patch('your_module.session_getter', return_value=None):
            # 模拟创建知识库钩子函数
            with patch('your_module.create_knowledge_hook', return_value=None):
                # 发送 POST 请求
                response = client.post('/api/v1/knowledge/create', json=mock_knowledge.dict())

                # 断言响应状态码
                assert response.status_code == 201

                # 断言响应数据
                assert response.json() == UnifiedResponseModel(
                    code=200,
                    msg='success',
                    data=KnowledgeRead(
                        knowledge_id=None,  # 假设知识库 ID 在数据库中自动生成
                        name='test_knowledge',
                        model='text-embedding-ada-002',
                        description='测试知识库',
                        is_partition=False,
                        collection_name='test_collection',
                        index_name='test_index',
                        user_id=1,
                        created_at=None,
                        updated_at=None
                    )
                ).dict()

                # 断言数据库操作
                # 假设 `session_getter` 返回一个模拟的数据库会话对象，可以在这里添加断言
                # 例如：
                # assert session.add.called_with(mock_knowledge)
                # assert session.commit.called_once()
                # assert session.refresh.called_with(mock_knowledge)

                # 断言钩子函数调用
                # 假设 `create_knowledge_hook` 返回一个模拟的钩子函数对象，可以在这里添加断言
                # 例如：
                # assert create_knowledge_hook.called_with(request, mock_knowledge, mock_login_user)
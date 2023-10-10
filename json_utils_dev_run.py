from json_utils import JsonFile



import unittest


import unittest
import os
import json

class TestJsonFile(unittest.TestCase):
    # 在每个测试方法执行前运行，用于设置测试环境
    def setUp(self):
        # 创建一个JsonFile对象，文件名为"test.json"
        self.json_file = JsonFile("test.json")
        # 创建一些测试数据
        self.test_data = {"name": "Test", "age": 30}

    # 测试读取方法
    def test_read(self):
        # 先将测试数据写入到文件中
        with open("test.json", "w") as f:
            json.dump(self.test_data, f)
        # 调用读取方法，应该返回True
        self.assertTrue(self.json_file.read())
        # 检查读取到的数据是否正确
        self.assertEqual(self.json_file.data, self.test_data)

    # 测试写入方法
    def test_write(self):
        # 将测试数据设置为JsonFile对象的数据
        self.json_file.data = self.test_data
        # 调用写入方法，应该返回True
        self.assertTrue(self.json_file.write())
        # 从文件中读取数据，检查是否正确
        with open("test.json", "r") as f:
            data = json.load(f)
        self.assertEqual(data, self.test_data)

    # 测试修改方法
    def test_modify(self):
        # 先将测试数据设置为JsonFile对象的数据
        self.json_file.data = self.test_data
        # 调用修改方法，应该返回True
        self.assertTrue(self.json_file.modify("name", "New Test"))
        # 检查数据是否被正确修改
        self.assertEqual(self.json_file.data["name"], "New Test")

    # 测试验证方法
    def test_validate(self):
        # 定义一个简单的模式
        schema = {"type" : "object",
                  "properties" : {
                      "name" : {"type" : "string"},
                      "age" : {"type" : "number"}
                  }}
        # 先将测试数据设置为JsonFile对象的数据
        self.json_file.data = self.test_data
        # 调用验证方法，应该返回True
        self.assertTrue(self.json_file.validate(schema))

    # 测试格式化方法
    def test_format(self):
        # 先将测试数据设置为JsonFile对象的数据
        self.json_file.data = self.test_data
        # 调用格式化方法，应该返回True
        self.assertTrue(self.json_file.format())


# 如果这个文件是作为主程序运行，而不是被导入，那么执行以下代码
if __name__ == "__main__":
  # 使用unittest模块的main函数来运行所有的测试用例
  unittest.main()

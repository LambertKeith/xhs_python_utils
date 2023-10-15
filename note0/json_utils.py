import json
import jsonschema

class JsonFile:
  # 初始化方法，接受一个文件名作为参数
  def __init__(self, filename):
    self.filename = filename # 保存文件名
    self.data = None # 保存数据
    self.schema = None # 保存模式

  # 读取方法，从文件中读取数据，并转换为python对象
  def read(self):
    try:
      # 打开并读取文件
      with open(self.filename, "r") as f:
        self.data = json.load(f)
      return True # 返回成功标志
    except FileNotFoundError:
      # 文件不存在时打印提示信息并返回失败标志
      print("File not found")
      return False
    except json.JSONDecodeError:
      # 文件格式错误时打印提示信息并返回失败标志
      print("Invalid JSON format")
      return False

  # 写入方法，将数据转换为json格式的字符串，并写入到文件中
  def write(self):
    try:
      # 转换数据为json格式的字符串
      data_str = json.dumps(self.data)
      # 打开并写入文件
      with open(self.filename, "w") as f:
        f.write(data_str)
      return True # 返回成功标志
    except TypeError:
      # 数据类型错误时打印提示信息并返回失败标志
      print("Invalid data type")
      return False

  # 修改方法，接受一个键和一个值作为参数，修改或添加数据中的键值对
  def modify(self, key, value):
    # 判断数据是否是字典类型
    if isinstance(self.data, dict):
      # 修改或添加键值对
      self.data[key] = value
      return True # 返回成功标志
    else:
      # 数据不是字典类型时打印提示信息并返回失败标志
      print("Data is not a dictionary")
      return False

  # 验证方法，接受一个模式作为参数，检查数据是否符合模式
  def validate(self, schema):
    try:
      # 保存模式
      self.schema = schema
      # 使用jsonschema库进行验证
      jsonschema.validate(self.data, self.schema)
      return True # 返回成功标志
    except jsonschema.ValidationError:
      # 验证错误时打印提示信息并返回失败标志
      print("Validation error")
      return False

  # 格式化方法，将数据按照一定的规则进行排版和缩进，并写入到文件中
  def format(self, indent=4):
    try:
      # 转换数据为json格式的字符串，并指定缩进参数
      data_str = json.dumps(self.data, indent=indent)
      # 打开并写入文件
      with open(self.filename, "w") as f:
        f.write(data_str)
      return True # 返回成功标志
    except TypeError:
      # 数据类型错误时打印提示信息并返回失败标志
      print("Invalid data type")
      return False


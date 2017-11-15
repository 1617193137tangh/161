＃！/ usr / bin / python
＃ -  *  - 编码：UTF-8  -  *  -

班 学生：
   '所有学生的基类'
   stucount =  0
   pristucount =  0
   midstucount =  0

 
   def  __init__（self，name，stu_no，class_no，gender）：
      self .name = name
      self .stu_no = stu_no
      self .class_no = class_no
      自我 .gender =性别
      Student.stucount + =  1
   
   def  displaycount（self）：
       打印（Student.pristucount + Student.midstucount）
 
   def  displayStudent（self）：
       打印（“名称：”，自我 .name和   “Stu_no： ”，自 .stu_no，“Class_no： ”，自 .class_no， “性别：”，自 .gender）


班级 prinmaryStudent（Student）：
    '小学生的基类'

    def  __init__（self，name，stu_no，class_no，gender）：
        self .name = name
        self .stu_no = stu_no
        self .class_no = class_no
        自我 .gender =性别
        Student.pristucount + =  1

    def  prinmaryname（self）：
        打印（“ prinmartstuname是”，名称）

    def  prinmaryclass_no（self）：
        打印（“ princlassclass_no是”，class_no）

    def  displaypristucount（self）：
       打印（Student.pristucount）


班级 MiddleStudent（学生）：
    '中学生的基类'
    midstucount =  0

    
    def  __init__（self，name，stu_no，class_no，gender）：
        self .name = name
        self .stu_no = stu_no
        self .class_no = class_no
        自我 .gender =性别
        Student.midstucount + =  1
    高清 化学（个体经营）：
        打印（名称，“可以化学”）
        
    def  Pyhics（self）：
        打印（名称，“可以phhics ”）

    def  displaymidstucount（self）：
       print（Student.midstucount）

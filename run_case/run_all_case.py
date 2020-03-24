import pytest
'''
测试文件以tets_开头(以_test结尾也可以)
测试类以Test开头，并且不能带有init方法
测试函数以test_开头
断言使用基本的assert即可
'''

#如何去运行测试用例，test开头的函数就可以,判断
if __name__=='__main__':
    #单个文件运行,运行添加对应文件的路径，路径要用相对路径
    #pytest.main(['../test_case/test_case_01.py'])
    #多个文件运行，对应添加多个文件的路径
    #pytest.main(['../test_case/test_case_01.py','../test_case/test_case_02.py'])
    #运行整个目录，添加目录的路径
    '''
    1、生成html的报告
    '--html=../report/report.html' 
    2、生成xml格式的报告
    --junitxml=../report/report.xml
    3、生成allure的报告
        1、生成allure结果目录，json格式
        '--alluredir','../report/reportallure/'
        2、生成allure报告
            1、安装一个allure工具
            
            allure generate ./reporttallure/ -o ./reporthtml/ --clean
            
    '''
    pytest.main(['../test_case','--alluredir','../report/reportallure/'])



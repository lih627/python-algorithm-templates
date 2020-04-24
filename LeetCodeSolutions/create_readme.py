#!/usr/bin/env python
# Created by Bruce yuan on 18-1-22.
import requests
import os
import json
import time


def _update_dict(org_dict, item_id, extension_name, url, complete_info, complete_items):
    try:
        if extension_name == 'py':
            org_dict[item_id].python = '[Python]({})'.format(url)
            complete_info.solved['python'] += 1
        elif extension_name == 'cpp':
            org_dict[item_id].cpp = '[CPP]({})'.format(url)
            complete_info.solved['c++'] += 1
        elif extension_name == 'sh':
            org_dict[item_id].shell = '[Shell]({})'.format(url)
            complete_info.solved['shell'] += 1
        elif extension_name == 'sql':
            org_dict[item_id].sql = '[Sql]({})'.format(url)
            complete_info.solved['sql'] += 1
        complete_items.add(item_id)
    except Exception:
        return


class Config:
    """
    some config, such as your github page
    这里需要配置你自己的项目地址
    １．　本地仓库的的路径
    ２．　github中的仓库leetcode解法的路径
    """
    # local_path = '/Users/lihao/Code/python-algorithm-templates/LeetCodeSolutions'
    # solution of leetcode
    local_path = os.getcwd()
    github_leetcode_url = 'https://github.com/lih627/python-algorithm-templates/tree/master/LeetCodeSolutions/'
    # solution of pat,　暂时还没写
    leetcode_url = 'https://leetcode.com/problems/'


class Question:
    """
    this class used to store the inform of every question
    """

    def __init__(self, id_,
                 name, url,
                 lock, difficulty):
        self.id_ = id_
        self.title = name
        # the problem description url　问题描述页
        self.url = url
        self.lock = lock  # boolean，锁住了表示需要购买
        self.difficulty = difficulty
        # the solution url
        self.python = ''
        # self.java = ''
        # self.javascript = ''
        self.cpp = ''
        self.shell = ''
        self.sql = ''

    def __repr__(self):
        """
        没啥用，我为了调试方便写的
        :return:
        """
        return str(self.id_) + ' ' + str(self.title) + ' ' + str(self.url)


class TableInform:
    def __init__(self):
        # raw questions inform
        self.questions = []
        # this is table index
        self.table = []
        # this is the element of question
        self.table_item = {}
        self.locked = 0

    def get_leetcode_problems(self):
        """
        used to get leetcode inform
        :return:
        """
        # we should look the response data carefully to find law
        # return byte. content type is byte
        content = requests.get('https://leetcode.com/api/problems/algorithms/').content
        # get all problems
        self.questions = json.loads(content)['stat_status_pairs']
        print("get all problems")
        difficultys = ['Easy', 'Medium', 'Hard']
        for i in range(len(self.questions) - 1, -1, -1):
            question = self.questions[i]
            name = question['stat']['question__title']
            url = question['stat']['question__title_slug']
            id_ = str(question['stat']['frontend_question_id'])
            if int(id_) < 10:
                id_ = '000' + id_
            elif int(id_) < 100:
                id_ = '00' + id_
            elif int(id_) < 1000:
                id_ = '0' + id_
            lock = question['paid_only']
            if lock:
                self.locked += 1
            difficulty = difficultys[question['difficulty']['level'] - 1]
            url = Config.leetcode_url + url + '/description/'
            q = Question(id_, name, url, lock, difficulty)
            self.table.append(q.id_)
            self.table_item[q.id_] = q
        return self.table, self.table_item

    def update_table(self):
        # the complete inform should be update
        complete_info = CompleteInform()
        self.get_leetcode_problems()
        # the total problem nums
        complete_info.total = len(self.table)
        complete_info.lock = self.locked

        # oj_algorithms = Config.local_path + '/' + oj
        # 查看os.walk看具体返回的是什么东西
        files = os.listdir(Config.local_path)
        # 存入完成题目的字符串信息 如'LeetCode_0001'
        complete_items = set()
        for item in files:
            if item.startswith('LeetCode'):
                str_item = str(item)
                item_name = str_item[:len('LeetCode_0000')]
                extension_name = str_item[len('LeetCode_0000.'):]
                item_id = str_item[9: 13]
                # print(extension_name)
                # complete_info.complete_num += 1
                folder_url = os.path.join(Config.github_leetcode_url, item)
                _update_dict(org_dict=self.table_item,
                             item_id=item_id,
                             extension_name=extension_name,
                             url=folder_url,
                             complete_info=complete_info,
                             complete_items=complete_items)
                # try:
                #     if extension_name == 'py':
                #         self.table_item[item_id].python = '[Python]({})'.format(folder_url)
                #     elif extension_name == 'sh':
                #         self.table_item[item_id].shell = '[Shell]({})'.format(folder_url)
                # except Exception as e:
                #     continue
        complete_info.complete_num = len(complete_items)
        readme = Readme(complete_info.total,
                        complete_info.complete_num,
                        complete_info.lock,
                        complete_info.solved)
        readme.create_leetcode_readme([self.table, self.table_item])
        print('-------the complete inform-------')
        # print(complete_info.solved)
        print('the total complete num is: {}'.format(
            complete_info.complete_num))


class CompleteInform:
    """
    this is statistic inform
    """

    def __init__(self):
        self.solved = {
            'python': 0,
            'c++': 0,
            'shell': 0,
            'sql': 0
        }
        self.complete_num = 0
        self.lock = 0
        self.total = 0

    def __repr__(self):
        return str(self.solved)


class Readme:
    """
    generate folder and markdown file
    update README.md when you finish one problem by some language
    """

    def __init__(self, total, solved, locked, others=None):
        """

        :param total: total problems nums
        :param solved: solved problem nums
        :param others: 暂时还没用，我想做扩展
        """
        self.total = total
        self.solved = solved
        self.others = others
        self.locked = locked
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.msg = '# LeetCode Solutions\n' \
                   '> Until {}, solved **{}** / **{}** problems ' \
                   'while **{}** are still locked.\n'.format(
            self.time, self.solved, self.total, self.locked, **self.others)

    def create_leetcode_readme(self, table_instance):
        """
        create REAdME.md
        :return:
        """
        file_path = Config.local_path + '/README.md'
        # write some basic inform about leetcode
        with open(file_path, 'w') as f:
            f.write(self.msg)
            f.write('\n----------------\n')

        with open(file_path, 'a') as f:
            f.write('| ID | Title | Difficulty | Solutions|\n')
            f.write('|:---:' * 4 + '|\n')
            table, table_item = table_instance
            # print(table)
            # for i in range(2):
            #     print(table_item[table[i]])
            # exit(1)
            for index in table:
                item = table_item[index]
                if item.lock:
                    _lock = ':lock:'
                else:
                    _lock = ''
                data = {
                    'id': item.id_,
                    'title': '[{}]({}) {}'.format(item.title, item.url, _lock),
                    'difficulty': item.difficulty,
                    'python': item.python,
                    'shell': item.shell,
                    'c++': item.cpp,
                    'sql': item.sql
                }
                line = '|{id}|{title}|{difficulty}|{python} {c++} {shell} {sql}|\n'.format(**data)
                f.write(line)
            print('README.md was created.....')

            file_path = Config.local_path + '/../LeetCodeList.md'
            # write some basic inform about leetcode
            with open(file_path, 'w') as f:
                f.write(self.msg)
                f.write('\n----------------\n')

            with open(file_path, 'a') as f:
                f.write('| ID | Title | Difficulty | Solutions|\n')
                f.write('|:---:' * 4 + '|\n')
                table, table_item = table_instance
                for index in table:
                    item = table_item[index]
                    if item.lock:
                        _lock = ':lock:'
                    else:
                        _lock = ''
                    data = {
                        'id': item.id_,
                        'title': '[{}]({}) {}'.format(item.title, item.url, _lock),
                        'difficulty': item.difficulty,
                        'python': item.python,
                        'shell': item.shell,
                        'c++': item.cpp,
                        'sql': item.sql
                    }
                    line = '|{id}|{title}|{difficulty}|{python} {c++} {shell} {sql}|\n'.format(**data)
                    f.write(line)
                print('README.md was created.....')


def main():
    table = TableInform()
    # table.update_table('leetcode-algorithms')


if __name__ == '__main__':
    table = TableInform()
    table.update_table()

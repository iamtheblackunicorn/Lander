"""
Lander by Alexander Abraham.
Licensed under the MIT license.
Project link:
https://github.com/iamtheblackunicorn/Lander
"""
import re
import os
import sys
import json
import shutil
import requests
import argparse
from re import sub
from re import findall
from argparse import ArgumentParser
class Compiler:
    """
    A class to compile the files to an HTML file and inject the content.
    """
    def __init__(self, config_name, template_name, verbose):
        """
        Defining some class-wide variables needed to compile sensible HTML.
        These variables are needed to run the methods below.
        """
        self.config = config_name
        self.template = template_name
        self.pattern = r'\{\{\s(.*)\s\}\}'
        self.verbose = verbose
        self.build_dir = 'build'
        self.o_file_name = 'index.html'
    def get_data(self, template):
        """
        Fetching the template variables from the supplied template.
        """
        contents = open(self.template, 'r').read()
        line_list = contents.split('\n')
        var_names = []
        for line in line_list:
            line_chars = list(line)
            char_list = []
            for char in line_chars:
                char_list = char_list + [char]
                joined_string = ''.join(char_list)
                if findall(self.pattern,joined_string):
                    var_names = var_names + [[line_list.index(line),findall(self.pattern,joined_string)[0]]]
                    char_list = []
                else:
                    pass
        return var_names
    def load_config(self, config):
        """
        Fetching the JSON configuration
        variables from the configuration file.
        """
        contents = open(self.config, 'r').read()
        return json.loads(contents)
    def build_variable_dictionary(self, config, template):
        configuration_settings = self.load_config(self.config)
        variable_list = self.get_data(self.template)
        result = {}
        for config_key in configuration_settings:
            for variable_info in variable_list:
                if config_key == variable_info[1]:
                    if type(configuration_settings[config_key]) == list and configuration_settings[config_key][0] == 'extern':
                        external_resource_file_name = configuration_settings[config_key][1]
                        contents = open(external_resource_file_name, 'r').read()
                        result[config_key] = [contents, variable_info[0]]
                    else:
                        result[config_key] = [configuration_settings[config_key],variable_info[0]]
        return result
    def find_and_replace_in_template(self, config, template):
        """
        Actually injects the data from the configuration file
        and the content file(s) into the template.
        """
        variable_dictionary = self.build_variable_dictionary(self.config, self.template)
        file_contents = open(self.template, 'r').read()
        file_contents_list = file_contents.split('\n')
        intermediate_result_list = []
        result = file_contents_list
        for key in variable_dictionary:
            variable_contents = variable_dictionary[key][0]
            variable_contents_line = variable_dictionary[key][1]
            line = file_contents_list[variable_contents_line]
            if findall(self.pattern, line):
                new_string = sub(self.pattern,variable_contents,line)
                intermediate_result_list = intermediate_result_list + [[variable_contents_line,new_string]]
            else:
                pass
        for x in intermediate_result_list:
            line_number =  x[0]
            new_line = x[1]
            result[line_number] = new_line
        return '\n'.join(result)
    def compile_result(self):
        """
        Dumps the HTML code string from [find_and_replace_in_template]
        into another HTML file.
        """
        new_file_name = self.o_file_name
        try:
            compiled = open(new_file_name, 'w')
            compiled = open(new_file_name, 'a')
            if self.verbose == True:
                print(self.find_and_replace_in_template(self.config, self.template))
            else:
                pass
            compiled.write(self.find_and_replace_in_template(self.config, self.template))
            compiled.close()
            os.makedirs(self.build_dir)
            shutil.move(self.o_file_name, self.build_dir)
        except Exception as error:
            print(str(error))
            sys.exit()
class Tools:
    """
    A class that makes
    some tools for Lander
    available.
    """
    def download_file(self,file_URL):
        """
        This method downloads a file
        from a remote URL.
        """
        request = requests.get(file_URL)
        with open(file_URL.split('/')[-1], 'w') as remote_file:
            remote_file.write(request.text)
    def init_project(self,dir_name):
        """
        This method initializes an empty project with some boilerplate.
        """
        config_file = 'https://raw.githubusercontent.com/iamtheblackunicorn/Lander/main/example/config.json'
        template_file = 'https://raw.githubusercontent.com/iamtheblackunicorn/Lander/main/example/template.html'
        content_file = 'https://raw.githubusercontent.com/iamtheblackunicorn/Lander/main/example/content.txt'
        file_list = [
            config_file,
            template_file,
            content_file
        ]
        try:
            os.makedirs(dir_name)
            os.chdir(dir_name)
            for file in file_list:
                self.download_file(file)
            os.chdir('..')
        except Exception as error:
            print(str(error))
            sys.exit()
class CLI:
    """
    A command-line interface class for Lander.
    """
    def __init__(self):
        """
        App variables.
        """
        self.name = 'Lander'
        self.version = '1.0'
    def version_info(self):
        """
        Prints out version info.
        """
        print(self.name + ' v.' + self.version)
    def run(self):
        """
        The actual command-line interface of Lander.
        """
        parser = ArgumentParser()
        parser.add_argument('--version', help='displays version info', action='store_true')
        parser.add_argument('--verbose', help='display code before compilation', action='store_true')
        parser.add_argument('--config', help='configuration file')
        parser.add_argument('--init', help='initialize a new project with some boilerplate')
        parser.add_argument('--template', help='the template to use')
        args = parser.parse_args()
        if args.version:
            self.version_info()
        elif args.init:
            Tools().init_project(args.init)
        elif args.config and args.template and args.verbose:
            Compiler(args.config, args.template, True).compile_result()
        elif args.config and args.template:
            Compiler(args.config, args.template, False).compile_result()
        else:
            print('Try using the "--help" flag.')
            sys.exit()
def main():
    """
    Main entry-point for the Python
    interpreter.
    """
    CLI().run()
if __name__ == '__main__':
    """
    Only invoked when Lander
    is called as a stand-alone tool.
    """
    main()

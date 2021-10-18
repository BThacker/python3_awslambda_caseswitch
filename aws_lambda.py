# Lamba handler and logic switching
# 2021 Brandon Thacker
# Entry and execution switch for python handler lambda

import json


def lambda_handler(event, context):
    global global_event_regions, global_event_account_name
    event_step = event['execution_step']
    entry_point = execute_event(event_step)
    entry_point()
    return {  #         <---- RETURN THIS RIGHT AWAY 
        'statusCode': 202,
        'body': json.dumps('Execution Accepted')
    }


def execute_event(switch_value):
    switcher = {
        'example_class': lambda: run_example_class,
        'example_class_2': lambda: run_example_class_2
    }
    return switcher.get(switch_value, lambda: "Invalid arg")()


# importing modules during execution is more efficient for lambda execution
def run_example_class():
    from aws_modules import example_class
    example_class_report = example_class.Example_Class()
    example_class_report.run_report()


def run_example_class_2():
    from aws_modules import example_class_2
    example_class_2_report = example_class_2.Example_Class_2()
    example_class_2_report.run_report()

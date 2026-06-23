def lambda_handler(event, context):
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)

    total = num1 + num2

    return {
        "Sum": total
    }
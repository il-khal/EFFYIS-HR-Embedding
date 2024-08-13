import runpod


def process_input(input):
    name = input['name']
    greeting = f'Hello {name}'

    return {
        "greeting": greeting
    }

def handler(event):
    return process_input(event['input'])


if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})
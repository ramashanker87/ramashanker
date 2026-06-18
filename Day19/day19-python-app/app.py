from flask import Flask, jsonify, request
from pathlib import Path
from datetime import datetime

app = Flask(__name__)

EBS_FILE = Path('/data/ebs/messages.txt')
EFS_FILE = Path('/data/efs/messages.txt')


def append_message(path: Path, message: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a') as file:
        file.write(f'{datetime.utcnow().isoformat()}Z - {message}\n')


def read_messages(path: Path):
    if not path.exists():
        return []
    return path.read_text().splitlines()


@app.route('/')
def home():
    return jsonify({
        'message': 'Day 19 persistent storage lab',
        'write_ebs': '/write?target=ebs&message=hello-ebs',
        'write_efs': '/write?target=efs&message=hello-efs',
        'read': '/read'
    })


@app.route('/write', methods=['GET', 'POST'])
def write():
    target = request.args.get('target', 'efs')
    message = request.args.get('message', 'default-message')

    if target == 'ebs':
        append_message(EBS_FILE, message)
    elif target == 'efs':
        append_message(EFS_FILE, message)
    else:
        return jsonify({'error': 'target must be ebs or efs'}), 400

    return jsonify({'status': 'written', 'target': target, 'message': message})


@app.route('/read')
def read():
    return jsonify({
        'ebs_messages': read_messages(EBS_FILE),
        'efs_messages': read_messages(EFS_FILE)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

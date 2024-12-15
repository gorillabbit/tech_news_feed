"""Slackに投稿する"""

from slack_sdk import WebClient


def post_to_slack(file_path: str, title: str, description: str, token: str) -> dict:
    """Slackにファイルをアップロードする"""
    client = WebClient(token=token)
    return client.files_upload_v2(
        channels="C0852SF0VGD",
        file=file_path,
        title=title,
        initial_comment=description,
    )

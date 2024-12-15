from slack_sdk import WebClient

def post_to_slack(file_path, title, description, token):
    client = WebClient(token=token)
    response = client.files_upload_v2(
        channels="C0852SF0VGD",
        file=file_path,
        title=title,
        initial_comment=description
    )
    return response

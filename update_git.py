from github import Github
import time
import config


def update_md(anglis):
    g = Github(config.GIT_TOKEN)
    repo = g.get_repo("JackMcKechnie/Irghiz")
    contents = repo.get_contents("Anglicisms.md")
    content = contents.decoded_content
    print("")
    for angli in anglis:
        if bytes(angli[0], encoding="utf-8") not in content:
            append = b"| " + bytes(angli[0].title(), encoding='utf8') + b" | " + bytes(angli[1], encoding='utf8') + b" |\n"
            content = content + append

    print(content.decode("utf-8"))
    commit_message = str(time.strftime("%d/%m/%Y %H:%M:%S")) + " Update"
    repo.update_file(contents.path, commit_message, content, contents.sha)


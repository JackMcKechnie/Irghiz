from github import Github

g = Github("08ec4107eef97328a237c5e14bef914bc62acd5d")

repo = g.get_repo("JackMcKechnie/Irghiz")

contents = repo.get_contents("test.txt")
content = contents.decoded_content + b" \nhello"
print(content)
repo.update_file(contents.path, "Commit message", content, contents.sha)
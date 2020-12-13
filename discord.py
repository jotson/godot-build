import json
import requests
import version
import config


def post_changelog():
    '''
    Post latest changelog to discord
    '''
    log = version.get_changelog()
    print('Posting changelog to discord...\n')

    color = 38377
    title = log.split('\n')[0].replace('# ', '')
    description = '\n'.join(log.split('\n')[1:]).lstrip()

    discord_json = {
        "content": "A new build has just been uploaded!",
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": color,
            }
        ]
    }

    response = requests.post(
        get_discord_webhook('discord-announce'),
        data=json.dumps(discord_json),
        headers={ 'Content-Type': 'application/json' }
    )

    if response.status_code < 200 or response.status_code > 299:
        raise ValueError('Discord error %s:\n%s' % (response.status_code, response.text))


def post_commit_message(title, message):
    '''
    Post commit message to Discord
    '''
    color = 38377

    discord_json = {
        "content": "**New commit: " + title + "**"
    }

    if message:
        discord_json["embeds"] = [
            {
                "description": message,
                "color": color,
            }
        ]


    response = requests.post(
        get_discord_webhook('discord-git'),
        data=json.dumps(discord_json),
        headers={ 'Content-Type': 'application/json' }
    )

    if response.status_code < 200 or response.status_code > 299:
        raise ValueError('Discord error %s:\n%s' % (response.status_code, response.text))


def get_discord_webhook(name):
    webhook = None
    with open(config.BUILDDIR + "/." + name, "r") as f:
        webhook = f.readline().rstrip()

    return webhook
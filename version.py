import subprocess
import configparser
import config


def get_version():
    cfg = configparser.ConfigParser()
    cfg.read(config.VERSION_FILE)

    return int(cfg['version']['version'])


def get_status():
    cfg = configparser.ConfigParser()
    cfg.read(config.VERSION_FILE)

    status = cfg['version']['status']
    status = status.replace('"', '') # Godot does strings differently

    return status


def get_commit():
    cfg = configparser.ConfigParser()
    cfg.read(config.VERSION_FILE)

    commit = cfg['version']['commit']
    commit = commit.replace('"', '') # Godot does strings differently

    return commit


def get_public_version():
    version = get_version()
    status = get_status()

    return '%s-%s' % (version, status)


def increment_version():
    cfg = configparser.ConfigParser()
    cfg.read(config.VERSION_FILE)

    version = int(cfg['version']['version']) + 1
    cfg['version']['version'] = str(version)

    with open(config.VERSION_FILE, 'w') as configfile:
        cfg.write(configfile)


def get_latest_commit():
    output = subprocess.check_output(['git', 'log', '-1', '--oneline', 'HEAD'])
    commit = output.split()[0].decode('utf-8')

    return commit


def get_latest_commit_message():
    output = subprocess.check_output(['git', 'log', '-1', '--format=%s'])
    title = output.decode('utf-8').strip()

    output = subprocess.check_output(['git', 'log', '-1', '--format=%b', '--shortstat'])
    message = output.decode('utf-8').strip()

    return (title, message)


def get_branch():
    output = subprocess.check_output(['git', 'status', '--short', '--branch'])
    branch = output.decode('utf-8').split('...')[0].replace('## ', '')

    return branch


def set_commit(commit):
    cfg = configparser.ConfigParser()
    cfg.read(config.VERSION_FILE)

    # Godot does strings differently
    cfg['version']['commit'] = '"%s"' % commit

    with open(config.VERSION_FILE, 'w') as configfile:
        cfg.write(configfile)


def tag_git():
    subprocess.check_output(['git', 'tag', 'v%s' % get_public_version(), get_commit() ])


def get_last_tag():
    tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0', '@^'])

    return tag.decode('utf-8').strip()


def get_commits_since_last_tag():
    SEP = "~~~"

    tag = get_last_tag()

    output = subprocess.check_output(['git', 'log', '--format=%s%n%b' + SEP, '%s..HEAD' % tag])
    output = output.decode('utf-8').strip()
    output = output.replace("\n\n", "\n")
    lines = output.split(SEP)
    
    updates = ""
    fixes = ""
    private = ""
    for line in lines:
        inner_lines = line.strip().split("\n");
        line = ""
        for inner in inner_lines:
            if inner.startswith("- "):
                inner = "; " + inner[2:]
            line += inner
        
        if len(line) == 0:
            continue

        if line.find("#private") >= 0:
            private += "- " + line + "\n"
        elif line.lower().startswith("fix"):
            fixes += "- " + line + "\n"
        else:
            updates += "- " + line + "\n"
    
    if len(updates) > 0:
        output = "New and updated:\n\n" + updates.strip()

    if len(fixes) > 0:
        if len(output) > 0:
            output += "\n\n"
        output += "Fixes:\n\n" + fixes.strip()

    if len(private) > 0:
        if len(output) > 0:
            output += "\n\n"
        output += "Private:\n\n" + private.strip()

    return output


def generate_changelog():
    ver = get_public_version()
    commits = get_commits_since_last_tag()

    with open(config.CHANGELOG, 'w') as changelog:
        changelog.write('# v%s\n\n' %ver)
        changelog.write(commits)


def get_changelog():
    with open(config.CHANGELOG, 'r') as changelog:
        lines = changelog.readlines()

    log = ''.join(lines)

    return log

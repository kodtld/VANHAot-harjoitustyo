from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/Login_Screen.py")
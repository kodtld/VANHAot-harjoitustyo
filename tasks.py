from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/Login_Screen.py")

@task
def test(ctx):
    ctx.run("python3 -m pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage report -m")
"""
    Created by Marios Papazogloy

    For now the project will be CLI Only
"""


if __name__ == "__main__":
    import app.scheduler as scheduler
    app = scheduler.Scheduler()
    app.run()
    
else:
    print('Please do not use the program outside of its location or as a secondary script.')
    raise SystemExit
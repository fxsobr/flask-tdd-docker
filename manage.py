from flask.cli import FlaskGroup

from sistema import app, db

cli = FlaskGroup(app)


@cli.command('recriar_db')
def recriar_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
